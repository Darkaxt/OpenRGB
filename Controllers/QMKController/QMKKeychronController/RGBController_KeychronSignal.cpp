/* SPDX-License-Identifier: GPL-2.0-or-later
 * Protocol: SRGBmods QMK_Community_Module, signalrgb.h / signalrgb.c.
 * Q6 HE ISO LED order is the firmware's sequential RGB matrix index.
 */
#include <algorithm>
#include <array>
#include "LogManager.h"
#include "RGBController_KeychronSignal.h"

namespace
{
constexpr unsigned int NA = 0xFFFFFFFF;
const char* const key_names[] = {
    "Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Print Screen", "Scroll Lock", "Pause", "Previous Track", "Play/Pause", "Next Track", "Stop",
    "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+", "Backspace", "Insert", "Home", "Page Up", "Num Lock", "Num /", "Num *", "Num -",
    "Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "Delete", "End", "Page Down", "Num 7", "Num 8", "Num 9",
    "Caps Lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ISO #", "Enter", "Num 4", "Num 5", "Num 6", "Num +",
    "Left Shift", "ISO <", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Right Shift", "Up", "Num 1", "Num 2", "Num 3",
    "Left Ctrl", "Left Windows", "Left Alt", "Space", "Right Alt", "Right Windows", "Fn", "Right Ctrl", "Left", "Down", "Right", "Num 0", "Num .", "Num Enter"
};
static_assert(sizeof(key_names) / sizeof(key_names[0]) == 109, "Q6 HE ISO LED count");
unsigned int matrix[] = {
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,NA,13,14,15,16,17,18,19,
    20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,51,52,53,NA,54,55,56,57,58,59,NA,
    60,61,62,63,64,65,66,67,68,69,70,71,72,73,NA,NA,NA,74,75,76,77,
    78,79,80,81,82,83,84,85,86,87,88,89,90,NA,NA,91,NA,92,93,94,NA,
    95,96,97,NA,NA,98,NA,NA,NA,99,100,101,102,NA,103,104,105,106,107,NA,108
};

bool Query(hid_device* dev, unsigned char command, std::array<unsigned char, 32>& reply)
{
    // Drain VIA's additional echo from the preceding transaction.
    while(hid_read_timeout(dev, reply.data(), reply.size(), 0) > 0) {}
    unsigned char request[33] = {0, command};
    if(hid_write(dev, request, sizeof(request)) != sizeof(request)) return false;
    // Required boundary: HID API's bounded read, matching the existing QMK driver.
    const int length = hid_read_timeout(dev, reply.data(), reply.size(), 1000);
    return length == 32 && reply[0] == command;
}
}

RGBController_KeychronSignal* RGBController_KeychronSignal::Detect(hid_device_info* info)
{
    if(info->product_id != 0x0B61 || info->interface_number != 1) return nullptr;
    hid_device* handle = hid_open_path(info->path);
    if(!handle) return nullptr;
    std::array<unsigned char, 32> reply{};
    const bool protocol = Query(handle, 0x22, reply) && reply[1] == 1 && reply[2] == 0 && reply[3] == 6;
    const bool count = protocol && Query(handle, 0x27, reply) && reply[1] == 109;
    if(!count)
    {
        hid_close(handle);
        return nullptr;
    }
    return new RGBController_KeychronSignal(handle, info->path);
}

RGBController_KeychronSignal::RGBController_KeychronSignal(hid_device* handle, const char* path) : dev(handle)
{
    name = "Keychron Q6 HE ISO (SRGBmods firmware)";
    vendor = "Keychron";
    description = "QMK SignalRGB protocol 1.0.6; temporary direct lighting";
    version = "1.0.6";
    location = path;
    type = DEVICE_TYPE_KEYBOARD;
    mode direct;
    direct.name = "Direct";
    direct.flags = MODE_FLAG_HAS_PER_LED_COLOR;
    direct.color_mode = MODE_COLORS_PER_LED;
    modes.push_back(direct);
    mode hardware;
    hardware.name = "Hardware";
    hardware.color_mode = MODE_COLORS_NONE;
    modes.push_back(hardware);
    active_mode = 0;
    SetupZones();
}

RGBController_KeychronSignal::~RGBController_KeychronSignal()
{
    Shutdown();
    if(direct_enabled) SetDirect(false);
    hid_close(dev);
}

void RGBController_KeychronSignal::SetupZones()
{
    for(const char* key : key_names)
    {
        led item;
        item.name = key;
        item.value = static_cast<unsigned int>(leds.size());
        leds.push_back(item);
    }
    zone keyboard;
    keyboard.name = "Keyboard";
    keyboard.type = ZONE_TYPE_MATRIX;
    keyboard.leds_count = keyboard.leds_min = keyboard.leds_max = 109;
    keyboard.matrix_map.Set(6, 21, matrix);
    zones.push_back(keyboard);
    SetupColors();
}

bool RGBController_KeychronSignal::SetDirect(bool enabled)
{
    unsigned char request[33] = {0, static_cast<unsigned char>(enabled ? 0x25 : 0x26)};
    if(hid_write(dev, request, sizeof(request)) != sizeof(request))
    {
        LOG_WARNING("[Keychron SRGBmods] Mode write failed");
        return false;
    }
    direct_enabled = enabled;
    return true;
}

void RGBController_KeychronSignal::DeviceUpdateMode()
{
    SetDirect(active_mode == 0);
}

void RGBController_KeychronSignal::DeviceUpdateLEDs()
{
    if(active_mode != 0 || (!direct_enabled && !SetDirect(true))) return;
    for(size_t first = 0; first < colors.size(); first += 9)
    {
        const size_t count = std::min<size_t>(9, colors.size() - first);
        unsigned char packet[33] = {0, 0x24, static_cast<unsigned char>(first), static_cast<unsigned char>(count)};
        for(size_t i = 0; i < count; i++)
        {
            packet[4 + i * 3] = RGBGetRValue(colors[first + i]);
            packet[5 + i * 3] = RGBGetGValue(colors[first + i]);
            packet[6 + i * 3] = RGBGetBValue(colors[first + i]);
        }
        if(hid_write(dev, packet, sizeof(packet)) != sizeof(packet))
        {
            LOG_WARNING("[Keychron SRGBmods] RGB write failed at LED %u", static_cast<unsigned int>(first));
            return;
        }
    }
    std::array<unsigned char, 32> reply{};
    while(hid_read_timeout(dev, reply.data(), reply.size(), 0) > 0) {}
}

void RGBController_KeychronSignal::DeviceUpdateZoneLEDs(int) { DeviceUpdateLEDs(); }
void RGBController_KeychronSignal::DeviceUpdateSingleLED(int) { DeviceUpdateLEDs(); }
