# Office 0.9.0 Screen integration

Authorization: 2026-11-06 user "go ahead" after source-based LightBulb integration
design and exact tray correction. Additional user request extends existing monthly
maintenance to upstream LightBulb. Specification: R29-R34, stage 31 ACTIVE;
stage 32 NOT STARTED. No release has been published for this work.

Source reference: Tyrrrz/LightBulb f74285784be7bc191872c06b1b5e644eb209b98b.
Installed standalone: 2.7.2+a23b129. Read actual upstream source, tests, native
interop, settings, tray and license. Imported current saved targets remain 6600K,
100/85%, automatic solar times, 3-hour transition, fullscreen pause; all seven
current hotkeys are unset. Private coordinates/exclusions stay local.

Implemented, not yet accepted: native Screen policy/owner on existing worker,
Screen settings/UI, exact root pause menus and bulb icon, independent persistent
pause deadlines, gamma baseline preservation/readback and imported settings.
The source-derived pure policy diagnostic passes. Full Windows integration,
rendered UI, actual gamma/RGB handoff, migration and final delivery remain required.

Automation monthly-openrgb-upstream-maintenance updated and read back through the
supported app view and local definition. It includes all three upstreams, exact
native adaptation pins, current main-display capture, independent gamma/RGB owners,
and verified full release. Timing/status/target and quiet-on-no-change behavior
are preserved. No extra maintenance run was triggered.

Scratch: E:/Temp/openrgb-screen-20261106. Cleanup transaction
11b910937fb4789e44c311568123550e is open/registered for the exact root. Only small
policy diagnostic compilation runs locally; full Windows build uses hosted CI.
No D: temporary build tree, new dependency tree or new background helper.
Packaged candidate D:/Tools/OpenRGB/candidate-screen-0.9.0 used D: for native
runtime/DLL I/O. After its verified whole-process exit, transaction
cc6cbbd412d6a9a81def355b8f39875f removed that exact spent candidate (86,452,263
bytes, 136 reviewed members, no exclusions/residuals). Stable 0.8.0 is restored,
PID 100128 at this checkpoint; recheck process/start identity before acting.

Windows build 42214176828 found one separator lambda outside its local scope.
Corrected at Ambient 8798eb8432220dc36ec304efad964fbf3b729cde; original follow-up
build 42214684494 completed successfully, all required production Windows checks
passed. CI artifact 13501121030 SHA256
495e873210ce3d47062ba269c2b80a8eb73d7c48ba4b815e56ed927c4b6b6efc.
Candidate package 5c122994517e2b446c3a0098c48f969501e7e95f9f33a64bb3fe57c6cb161861
passed provenance/private-state/corrupt-package rejection checks, not final release.
Packaging/migration Python/PowerShell parse checks pass.
check_screen.py is prepared for real owner/import/independent pause/gamma readback
and restoration verification; it does not write gamma or interact with desktop UI.

Real candidate imported every saved source setting and rejected gamma ownership
while standalone LightBulb ran. Actual app-owned renders cover all 24 views,
four Screen tabs and exact root/11-choice pause menus at 100%, 150%, 200%; native
editor Save/restore preserved the entire RGB configuration. Evidence retained
locally at D:/Tools/OpenRGB/validation/20261106/screen-0.9.0/ui-rest-* and
competing-owner-guard.json. These are honest rest-state renders (actual_preview
false): Windows reports input desktop Screen-saver / automatic-screensaver rest.
Original export session 35056 was gracefully ended after this concrete source
unavailability was diagnosed; fallback 0.8.0 readiness passed. Supported rest-state
export session 41592 then completed successfully. No desktop input was sent.

Rendered inspection found Qt interpreting '&' as a tab mnemonic. Replaced caption
with 'Day and night' at Ambient 322da9f6b57d5cbef6110f6475059bf935155394.
Build 42216299806 is currently running, observed by gh watch session 1391. This
caption change still needs its current build/render check. Native support change
also ensures a guard-only test never enables gamma after standalone has exited.

External acceptance blocker: R30/R32/R34 real gamma handoff/readback/restoration,
live RGB brightness-follow/capture, restart persistence and migration are unverified
because the screen saver is active and standalone LightBulb PID 43020 still owns
gamma (recheck on resume). A pending user input asks them to dismiss the screen
saver and exit LightBulb gracefully. Do not automate desktop takeover, force-stop
the elevated standalone, or enable a competing writer. Resolution: available
interactive desktop and standalone exited. Stage 31 acceptance and stage 32 final
release/activation depend on that boundary. Source/CI/UI success is not completion.

Next: finish the current build and corrected-caption render/package preparation;
then, once the real external boundary is available, capture migration rollback,
activate screen management and run check_screen.py, persistence/lifecycle and live
capture checks. Close stage 31 only after all acceptance passes. Final normal
0.9.0 release, independent retrieval, activation/startup migration and cleanup are
still required; no release or startup retirement has occurred.
