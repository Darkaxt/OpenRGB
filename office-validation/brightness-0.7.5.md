# Main-display brightness following

R26 uses read-only GetDeviceGammaRamp on Windows' actual primary display. The
linear slope of the strongest channel supplies a scalar output factor, excluding
colour-temperature attenuation. Nonlinear ramps are rejected; same-display read
failure retains the last valid factor, while a display change resets it. This
does not read physical backlight or HDR tone-mapping brightness.

The manual brightness baseline stays in GPU sampling. The display factor is
applied afterward, before existing smoothing and changed-LED submission. A static
retained colour row therefore changes intensity without another capture/sample.
Identify/calibration bypass dimming, and rest always forces black. A toggle and
live read status are available under Control → Advanced options → Output balance.
Existing files acquire the default only in memory until an explicit user Save.

Windows CI 42087443347 passed on ambient source
3b73d9bf98446fceabaa80338612097e52e87e47, covering actual native output retention,
follow disable, Identify reference colours, smoothing, rest, reconnect, mapping,
GPU sampling, panel controls and authenticated control boundaries. Pure gamma
tests cover unity, LightBulb endpoint jitter, temperature attenuation, nonlinear
rejection, same-display read failure and display identity changes.

After the user dismissed the automatic saver, candidate owner 52532 agreed with
independent GDI readback at factor 0.8434081926529612 on primary DISPLAY2. Earlier
independent readings changed from 0.86073 to 0.84755 as LightBulb dimmed. Actual
wallpaper preview and fresh frames were verified, with all six controllers online.
The saved settings SHA256 remains
0f393259b7143cd056474139ba6172c3efe1b9bcef5e1652bd7cf003ce31985a.
No LightBulb or gamma writes were performed. A 100-read diagnostic measured
1.006 ms median for both displays; native following reads one display at 1 Hz.
A 6.64-second live sample measured 14.92 Hz output, 1.301 ms median GPU processing,
0.684% whole-machine CPU and 85.3 MB working set. These are observations of the
current wallpaper/load, not a universal resource bound or physical LED feedback.

Normal published release v1.1-office.0.7.5 targets core commit
e08914ab7fafcb9075194df47145dfadb85b7d5a. The independent download matches its
checksum and GitHub asset digest:
79a9c6de1a6b47a209a25e11da8b4436592108f0549d74f10ebf16759201f44a.
All 116 installed payload members match, including accepted native/plugin/panel
binaries. Official owner 34204 reads 0.8433775544593891, matching independent GDI,
with fresh wallpaper frames and all six controllers online. Existing quiet
sign-in scheduling reuses that owner with task result 0, and startup/shortcut
bindings point to 0.7.5. Settings remain byte-identical. Candidates, old installed
0.7.4 and expendable scratch were transactionally removed; only 0.7.5 remains
under releases. Published recovery ZIPs remain retained. Stages 27/28 COMPLETE.
