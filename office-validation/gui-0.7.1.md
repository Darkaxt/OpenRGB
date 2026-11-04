# Office 0.7.1 draft-blur verification

The reported slider-at-10 image stayed sharp because the slider was an unsaved
draft while native preview used the applied blur, observed as zero. Preview and
Topology now send a read-only blur override through the existing authenticated
IPC and bounded GPU preview worker. This does not save settings, extract LEDs or
change actual lighting. The overlay continues to display submitted LED colours.

The preview cache includes image revision and blur. Old replies are rejected if
the slider has changed; zero is rendered from the retained original texture,
avoiding double filtering. PNG encoding remains outside the capture/output lock.
At large radii the old sparse mip-zero taps created sharp offset ghost images.
The same shared filter now integrates each tap's footprint through the existing
GPU mip chain. LED extraction receives that correction when blur is applied.

Windows run 41930768086 at Ambient 12df9829570818f3ebb18751e9a45f2194705bad
passed production GPU, lifecycle, layout, widget and IPC checks. Coverage includes
static draft 0/10/0, exact restoration, matching applied/draft results, suppression
of repeated encodes, dense stripe smoothing, read-only widget requests and stale
reply rejection. Earlier run 41929673789 passed the draft wiring; direct visual
inspection then exposed the sparse-filter ghosts corrected in the final run.

Installed acceptance paused Wallpaper Engine through its documented CLI, compared
the same retained source at blur 0/10/0, and resumed playback in finally. Mean RGB
differences were 22.66/14.42/18.74; zero restored the exact original PNG. Sampling
passes, LED writes and owner submissions did not advance during those requests;
settings/revision and actual colours stayed unchanged. All six controllers/314
LEDs were online. The private map file retained its original SHA-256.

Five preview requests/sec over 21.74 seconds held 14.91 output-clock Hz, median
reported 14.97 Hz, 15.00 changed input FPS and 13.02 skipped duplicates/sec. Median
GPU processing was 0.541 ms, request latency 8.37 ms, total CPU 0.77% on 32 logical
CPUs, RSS 82.7 MiB. These are native/API observations, not physical LED latency.

Actual raw/blurred preview images, acceptance JSON, performance samples and app
renders are retained under `D:/Tools/OpenRGB/validation/20261105/gui-0.7.1`.
No private topology, pairing state or IPC credentials are included here. The user
authorized terminating the old panel's draft when replacing the program; its
saved settings were preserved.

Delivery: normal release `v1.1-office.0.7.1` is published from completed source
`ccdeeaa5ddfd54619146e66d37b2da9f86a08e02`. Independently downloaded ZIP SHA-256
`6a02898989881dae52e04843854724ba146b7bfb01a5ead2047d9bc7f8aed787` matches the
published checksum and GitHub digest. Tag source and all 108 installed payload
members were read back; native/plugin/panel provenance and rejection of corrupted
plugin/panel before installation passed on the downloaded package.

Official owner PID 115236 and panel PID 117828 use the installed 0.7.1 directory.
All six controllers report online with actual preview and 14.92 Hz output clock.
The desktop shortcut was migrated and read back; final native exports cover all
pages and the corrected Preview hint. Saved topology remained byte-identical.

Reviewed cleanup removed both spent candidate installations, obsolete official
0.7.0 and the task scratch. Final tickets cd83eb87, 3d8f0a83 and b4e8bb24 applied
without residuals; the earlier candidate ticket 769ba570 also applied. Only
`D:/Tools/OpenRGB/releases/1.1-office.0.7.1` remains under releases. Published
recovery ZIPs and required validation evidence remain; live owner/panel scratch
stays bound to persistent state-integration/runtime-temp. Stage 20 is complete.
