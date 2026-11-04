# Office 0.7.0 integrated verification

Authoritative requirements: `office-integration-specification.md`, stages 14–18.
Private mappings, pairing state and IPC credentials are excluded from this record.

## Responsive preview and topology

The installed baseline starved output in synchronous PNG compression on the
lighting event thread while five obsolete hidden panels kept asking for images.
One bounded native preview worker now copies a downsampled image under the GPU
lock, releases that lock, encodes the owned image separately and coalesces demand.
Unchanged images share a generation cache. Hidden panels stop image polling and
new interactive panels use a same-user singleton. Genuine black/static frames
remain valid. The native owner remains the only capture/RGB writer.

Windows run 41903597071 (Ambient 600a8f5) passed the production sampler, stalled
encoder, coalescing, lifecycle and real Qt widget checks. Installed preview demand
at five requests/second held 14.88 FPS with 29.54 input FPS, median request 8.61 ms,
GPU sampling 0.54 ms and CPU 0.90% of the 32-logical-CPU host. Metadata demand held
14.80 FPS with median request 2.83 ms. Later lifecycle build b848749 held 14.78 FPS
under the same preview demand, median request 8.40 ms, GPU 0.54 ms and total CPU
0.72%. Measurements cover native submission, not physical LED latency.

Normal/150% installed exports confirm grey context outlines below cyan selection
and synchronized Preview/Topology spatial blur. Production pixel tests also cover
100%/150%/200%. The entire private saved map/settings file remained byte-identical.

## Screensaver and automatic rest

An independent read-only probe established that Ctrl+Alt+L launches WPXSCR~1.SCR
with WindowsScreenSaverClass on Default, spanning both displays. Windows' SPI
screensaver flag remains false. The owner now recognizes that actual fullscreen
saver directly, as well as the separate Screen-saver desktop. It never switches
the user's desktop or captures secure lock-screen imagery.

Windows run 41912140012 at Ambient 970e2c8 passed real private-desktop enumeration
and manual-saver tool-window regression checks. During the user-started saver,
the installed owner selected mode screensaver, advanced input frames from 1 to 47,
held approximately 15 FPS after source startup, and submitted a maximum channel
value of 1/255 across all six controllers. It returned to fresh wallpaper capture.
The user confirmed both the near-black saver output and wallpaper restoration.
Observed first frames were 2.20 seconds into saver selection and 1.64 seconds into
wallpaper restoration; those are observed capture boundaries, not guarantees.

The user also confirmed lights off while Windows was locked and resumption after
unlock, with a noticeable recovery delay. Separate installed-owner event checks
verified lock/off/unlock/fresh capture and display-sleep/off/wake/fresh capture
without locking Windows or changing physical display power. All 314 outputs were
black in rest. Lock/sleep overrides calibration, identify and standby preview,
releases capture and discards stale source colours. Settings/maps remain unchanged.
Actual OS display-sleep notification handling is covered by production event tests;
independent physical panel power state while Windows still reports awake is not
inferred. The automatic separate-desktop capture path has enumeration coverage;
the physical user acceptance above used the Ctrl+Alt+L ordinary-desktop path.

Evidence retained under `D:/Tools/OpenRGB/validation/20261104/gui-0.7.0` includes
CI logs, signed cleanup manifests, performance samples, installed lifecycle-event
results, live source/colour counters and app-owned normal/high-DPI render exports.

## Tray contrast and conservative media borders

The global transparent QWidget theme leaked into QMenu. Explicit opaque menu,
item, selection, disabled-text and separator colours now override that inheritance.
Production Qt render checks cover 100%, 150% and 200% scaling.

Windows run 41919043899 at Ambient fd38160 verifies the combined implementation.
The GPU checks exercise 4:3, 16:9, 16:10 and common cinema formats, transitions to
unbarred imagery, unsupported ratios, asymmetric dark edges, uniformly dark input,
genuine black and the disabled setting. Credible paired near-black margins must
have adjacent positive content evidence. One GPU detection pass supplies every
LED's transformed rectangle; saved normalized topology is never rewritten.

The first GPU regression exposed an inlined nested-loop early-return issue:
both 4:3 edges independently passed, but the ratio loop lost the matching crop.
Accumulating matte evidence without those inner early returns fixed the actual
GPU regression. The installed combined build with border detection enabled and
five preview requests per second held 14.92 output FPS, 29.98 input FPS, median
GPU processing 0.665 ms, request 10.41 ms and total CPU 0.92% (32 logical CPUs).
The diagnostic setting change was reverted with the owner stopped; exact saved
bytes were restored, then the owner restarted and all six controllers/314 LEDs
and the original configuration hash were read back. The readiness helper briefly
encountered a Windows endpoint-file publication sharing race; actual endpoint
readiness was subsequently confirmed. Final release/delivery remains pending.

## Static input and changed output

Final Ambient cf06cbb passed hosted Windows run 41924410667. The production GPU
path compares every cropped LG RGB pixel with the retained input using a compute
shader and reads back only a four-byte change flag. Identical callbacks return
before mip generation, matte detection, blur, LED extraction or preview revision.
Single-pixel changes, including outside mapped regions, are detected; pixels on
another monitor do not invalidate the LG. No approximate image fingerprint or
full-resolution CPU bitmap is used. Map/settings changes explicitly resample the
retained image without waiting for another capture callback.

Output adaptation runs until final byte values settle. Only changed LEDs update
controller buffers and only affected controllers submit batched output. First
delivery/reconnection force full state, including black. Windows production
tests cover exact settling, one changed LED without unrelated-device writes,
source/resize invalidation, rest, genuine black and reconnection. The shader
compile diagnostic caught reserved HLSL identifiers before the successful build;
an older map test was corrected to use production retained-map invalidation.

Installed dynamic demand at five preview requests/sec measured 29.59 callbacks/sec,
15.03 changed images/sec, 14.55 skipped duplicates/sec and 14.38 output-clock
ticks/sec over 23.09 seconds (reported clock median 14.96 Hz). Median GPU work was
0.862 ms, preview request 11.14 ms, total CPU 0.85% on 32 logical CPUs, and working
set 92.5 MiB. Hardware latency/ACKs are not included in these measurements.

Wallpaper Engine was temporarily paused with its documented pause command and
resumed in a finally block with play. After settling, the last 65.92 seconds had
zero input callbacks, zero sampling passes, zero LED writes and zero owner device
submissions, while 977 output-clock ticks continued servicing events. The user
confirmed the Govee strip and bars held steady colours without flashes. Resumed
readback showed all six controllers, 314 LEDs, fresh wallpaper capture and a
15.12 Hz clock. The private saved map remained byte-identical throughout.

The Govee driver independently resends cached B0 data after 30 seconds of silence,
checked every ten seconds. H6609/H8048 do not re-enter streaming via B1. This is a
conservative cadence observed reliable in the static test, not a measured minimum
refresh requirement; these UDP refreshes are excluded from owner submission
counters. Native APIs still send a full device frame when the hardware protocol
requires it. Normal/150% installed exports verify separate clock/device-update
labels without changing the saved topology. Final delivery remains in stage 16.
