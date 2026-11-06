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

Windows build 42214176828 found one separator lambda outside its local scope.
Corrected at Ambient 8798eb8432220dc36ec304efad964fbf3b729cde; original follow-up
build 42214684494 is running, observed by gh run watch session 51202. No acceptance
or release claim. Packaging/migration Python/PowerShell parse checks pass.
check_screen.py is prepared for real owner/import/independent pause/gamma readback
and restoration verification; it does not write gamma or interact with desktop UI.

Next: inspect that Windows build, retrieve its exact CI artifact and reusable
native a185a351 artifact through download_ci.py, package clean sources using
package_release.py, check_package.py, install_package.py. Render the actual
candidate, verify gamma-owner rejection while standalone runs, then arrange its
graceful exit for live gamma handoff. Close stage 31 only after complete acceptance.
Preserve live 0.8.0 and standalone LightBulb until verified candidate handoff is
ready. Final release remains required.
