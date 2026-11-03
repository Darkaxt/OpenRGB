/* SPDX-License-Identifier: GPL-2.0-or-later */
#pragma once
#include <hidapi.h>
#include "RGBController.h"

// The Q6 HE ISO may already run SRGBmods' QMK protocol 1.0.6 instead of
// Keychron's newer A8 extension. Lighting only; no VIA/keymap/EEPROM writes.
class RGBController_KeychronSignal : public RGBController
{
public:
    static RGBController_KeychronSignal* Detect(hid_device_info* info);
    ~RGBController_KeychronSignal();
    void SetupZones();
    void DeviceUpdateMode();
    void DeviceUpdateLEDs();
    void DeviceUpdateZoneLEDs(int zone);
    void DeviceUpdateSingleLED(int led);

private:
    RGBController_KeychronSignal(hid_device* handle, const char* path);
    bool SetDirect(bool enabled);
    hid_device* dev;
    bool direct_enabled = false;
};
