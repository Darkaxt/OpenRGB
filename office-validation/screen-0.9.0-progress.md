# Office Screen integration: current delivery checkpoint

Authorized: user "go ahead", monthly upstream-LightBulb task update, and later
explicit "kill Lightbulb if you must". Specification R29-R34. Stage 31 ACTIVE
(reopened for a native shutdown defect); stage 32 BLOCKED on that fix/verification.
Final target is a normal verified 0.9.1 patch release. No tracked deferrals.

LightBulb feature is integrated in the native Qt application: exact two root
pause menus, official bulb, imported settings, independent RGB/screen owners,
solar/manual scheduling, transitions, smoothing, exclusions, hotkeys and preview.
Source reference f74285784be7bc191872c06b1b5e644eb209b98b; MIT/source map included.
Source/settings/captures remain private where required; no desktop input was sent.

Verified Screen acceptance before delivery: source-derived contracts and Windows
native UI/lifecycle checks; exact imported settings; actual renders at three sizes
and 100/150/200%; both-display gamma readback and exact restoration; independent
pause choices and native mode rest/resume; one applied RGB brightness factor;
registered native hotkey handler; actual foreground exclusion while RGB capture
continues; deadlines/offset persistence through restart; complete full-day preview;
real main-display capture and native editor Save/restore preserving all 314 LEDs.
This evidence remains applicable to unchanged Screen/capture/controller code.
Local retained evidence: D:/Tools/OpenRGB/validation/20261106/screen-0.9.0.

The monthly-openrgb-upstream-maintenance heartbeat is updated and read back.
It includes all three upstreams and native LightBulb adaptations, preserving
monthly timing, target/current status, quiet no-change behavior and verified release.

Delivery found a genuine native defect: stopping candidate PID88724 returned
0xc0000005 after journal owner_stop_complete. Windows dump/WinDbg show a sender
locking a freed NetworkClientInfo::client_send_mutex (offset A8; CV F8, running148).
NetworkServer.cpp admitted accept(-1) because SOCKET is unsigned on Windows and
its '<0' check was false; invalid socket destruction skipped sender join. Native
cleanup ran concurrently with that late invalid client. This is inherited native
SDK code, not gamma teardown. Retained dump crash-88724.dmp SHA256
f6cff79a813cbf4fdd23fc60eaec11573525a0f26f80cfecce76f94b738d7e99
and crash-analysis.log/crash-thread.log substantiate the diagnosis.

Native fix 56a094a924391d7a0478adc1f3efdd27080b5da2 rejects INVALID_SOCKET,
closes failed/unclaimed admissions, joins connection workers, and joins sender
ownership independently of socket validity with its condition predicate changed
under the queue mutex. Native build 42220324884 is RUNNING (watch session90136).
Ambient 691b57b474ace5d1fd98ee08300849d27eaf3dc3 pins that exact native source;
Windows plugin build 42220395237 PASSED. No other feature code changed.
Native regression covers absent/idle/disconnecting clients and real process exit.
Old-artifact smoke 42220382962 passed: it does not reproduce this timing-sensitive
race reliably. Improved wire check f49bdb44327 uses native graceful exit after
actual SDK to simulated Govee traffic; old-artifact run 42221086999 is RUNNING
(watch20830). Inspect original outcomes, do not duplicate or abandon them.

0.9.0 source029eac300c7 / plugin322da9f was normally published and independently
retrieved (ZIP cb779509b0c1d094958eae62324516d67ef4b16f96af0b28f8d2126c54e6ed26),
but failed local shutdown acceptance. It is now explicitly marked PRERELEASE and
not latest, with honest failure notes; do not call it the delivered outcome or
rewrite its tag. Final 0.9.1 must supersede it through the established normal channel.

Current live owner restored to stable 0.8.0, PID90352 at checkpoint (recheck exact
PID/start identity). Existing sign-in binding remains 0.8.0; no startup retirement
or final shortcut migration occurred. Preserve all private topology/settings.
Standalone LightBulb PID43020 was stopped through broker request
8db7d944cd9142bab7f0d0d30cd3f61e after exact path, native start639294986079909296
and version2.7.2+a23b129 checks. Initial request stopped nothing because WMI
truncated that timestamp by six ticks. Original settings/startup/app were preserved.
Both display ramps already read neutral after its exit; no reset was needed.
Integrated screen settings remain enabled in private office-screen.json for the
next candidate. Rollback is captured in office-screen-migration.json; retain the
original standalone app and Office0.8.0 package. Never restart competing gamma.

Scratch E:/Temp/openrgb-screen-20261106, cleanup transaction
11b910937fb4789e44c311568123550e remains open for required build/package inputs.
Earlier D candidates were stopped and transactionally removed immediately after
last use: cc6cbbd412d6a9a81def355b8f39875f (86,452,263 bytes) and
3a585c49949a9020edfb5def40bd503f (86,456,426 bytes), no residuals. Temporary native
DLL/runtime I/O used D: intentionally. No local native build tree/new helper.
Unavoidable OS crash dump C:/Users/darka/AppData/Local/CrashDumps/OpenRGB.exe.88724.dmp
was hash-verified against the retained D: copy; clean that task-attributed original
and the spent D: symbols cache through the helper when their consumers are done.
Existing owner runtime-temp is independent of task scratch.

Next: inspect native build and old-artifact wire outcomes. Run improved graceful
wire verification against the new compiled source via the supported reuse flow.
Retrieve exact native/plugin receipts; package and install a new0.9.1 candidate;
verify real host shutdown/cold start and unchanged Screen/gamma/map behavior.
Close stage31 only on passing evidence. Resume stage32: final commit/package,
normal0.9.1 release, independent download/check, actual installed activation,
quiet existing sign-in/shortcut, exact standalone startup retirement, readbacks,
final specification reconciliation and transactional scratch cleanup.
