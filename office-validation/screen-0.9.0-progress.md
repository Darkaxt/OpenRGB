# Office 0.9.0 Screen integration

Authorization: 2026-11-06 user "go ahead"; native LightBulb integration and exact
tray. Additional request extends monthly maintenance. Authoritative specification:
office-integration-specification.md R29-R34. Stage 31 COMPLETE; stage 32 ACTIVE.
No blockers or tracked deferrals. Final release/delivery still pending.

Upstream LightBulb pin f74285784be7bc191872c06b1b5e644eb209b98b; MIT attribution,
official bulb and source map included. Ambient 322da9f6b57d5cbef6110f6475059bf935155394
passed completed Windows build 42216299806. CI artifact 13501626674 SHA256
8f9bdbf8a3d9af79caab9b633c9e38d9a019765480f0e9b3d13dcb5eaea2fd08.
Native compiled source a185a351, successful run 42113774830, remains unchanged;
only allowed packaging/support/docs changes exist in the native repository.

Verified integrated behavior:
- Complete imported settings match the untouched standalone file; current targets
  6600K day/night, 100/85%, automatic solar/3-hour transitions, fullscreen pause,
  seven unset shortcuts. Private location/exclusions remain local.
- Actual Screen controls and exact root tray/11 pause choices rendered at all
  three required sizes and 100/150/200% scaling. Current corrected-caption build
  additionally rendered with real main-display preview. Real editor Save/restore
  retained the complete six-device/314-LED configuration.
- Both displays pass actual gamma temperature/brightness readback and exact
  baseline restoration. Independent pause choices, native effect rest/resume,
  applied brightness factor once, stale screen draft rejection, original settings
  restoration and source hash preservation pass.
- Actual native display/resume/time message paths preserve the single factor;
  registered hotkey handler toggles Screen independently; actual foreground
  executable exclusion leaves RGB capture running.
- Pause deadlines/offsets survive process restart and restore correctly. Full-day
  preview completed and traversed both targets. Graceful native exit restored
  exact original display ramps. Live capture remains main-display wallpaper/app.
- Resource observation: requested 15fps yielded 14.88 output fps, median GPU
  .912ms, metadata request 3.31ms, process working set 103MiB, 1.67% total CPU;
  original saved RGB settings unchanged. This is current-workload evidence.
- Monthly upstream automation updated through supported tool and read back;
  timing/status/target preserved, includes all three upstream source pins and
  compatible native LightBulb adaptations, quiet when no actionable changes.

Evidence: D:/Tools/OpenRGB/validation/20261106/screen-0.9.0. Includes live-screen,
screen-runtime, preview-and-exit, private persistence, current-live UI, earlier
DPI renders, gamma exit readbacks and performance. Private records/captures are
never release inputs. No desktop input/foreground takeover was performed.

User dismissed screen saver and expressly authorized killing LightBulb. Initial
broker request 4ec551eefdfa42328faa0cab61dc1c18 stopped nothing: WMI creation time
truncated native timestamp by six ticks. Correct native identity was reread;
broker request 8db7d944cd9142bab7f0d0d30cd3f61e verified PID43020, native start
639294986079909296, installed path/version a23b129 and observed exact process exit.
Settings and startup were unchanged. Gamma already read neutral on both displays,
so no additional gamma reset was performed. Migration rollback captured privately
at state-integration/office-screen-migration.json. Preserve standalone application
and the 0.8.0 package for rollback. Do not restart a competing gamma writer.

Current candidate: D:/Tools/OpenRGB/candidate-screen-0.9.0-r2, owner PID88724 at
checkpoint (recheck pid/start identity). Screen management enabled and validated;
imported settings restored, both manual pauses cleared, source settings untouched.
Sign-in binding remains 0.8.0 until final delivery. Standalone startup still exists.

Scratch: E:/Temp/openrgb-screen-20261106, cleanup transaction
11b910937fb4789e44c311568123550e. Candidate native DLL/runtime I/O uses D:;
r2 cleanup transaction 3a585c49949a9020edfb5def40bd503f must apply immediately after
final owner replaces it. Earlier exact candidate was stopped and transactionally
removed (cc6cbbd412d6a9a81def355b8f39875f, 86,452,263 bytes, no residuals).
No local native build tree or new background helper. Existing owner has its own
persistent runtime-temp under state-integration, independent of task scratch.

Next: commit/push verified sources, produce final 0.9.0 package from the exact
clean commits and successful CI receipts, check it, publish normal existing-channel
release, independently retrieve/hash/provenance-check delivered assets, install
final release, verify cold start/gamma/RGB, switch existing quiet sign-in/shortcut,
retire exact standalone startup through Migrate-LightBulb.ps1, read back delivery,
then close stage 32 and clean spent candidates/scratch. No further approval needed.
