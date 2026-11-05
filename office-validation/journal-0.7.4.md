# Office Ambilight 0.7.4 diagnostic journal delivery

Release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.7.4

Core package source: `0cf15d067797785aec0cf422007b5a376b029fbe`.
Ambient source: `ab7286b20969db720c4d9d7b699432bbc431ccd7`.
Ambient Windows build/test run: `42055069171` (passed).
Native ABI-compatible OpenRGB source remains `82f150a276a800c01b6a5aed1de71520b9d138b4`.

The independently downloaded normal release ZIP has SHA-256
`bb16a06889360b53c053b83ca53e74b62f070bd678a45b64c4a5573e0c465988`.
All 112 installed payload files match that download. The published tag resolves
to the core package source; the plugin/panel provenance matches the final CI
artifact. This document records delivery afterward and does not retag the release.

The installed native owner appends to
`D:/Tools/OpenRGB/state-integration/logs/office-ambience-events.jsonl`.
Records include UTC/monotonic time, Windows uptime, process/thread/session/build,
capture and GPU lifecycle, errors, source/rest/session/display changes, device
availability and low-frequency health. Retention is eight 4 MiB segments. Tests
cover abrupt ExitProcess persistence without destructors, append across restart,
concurrent callbacks, rotation and observable I/O failure. Write-through logging
does not guarantee survival of an incomplete write during sudden power loss.

Live installed evidence verified actual capture stage/first-frame/health records
with the final source revision and prior sessions retained. Saved settings hash
stayed `0f393259b7143cd056474139ba6172c3efe1b9bcef5e1652bd7cf003ce31985a`.
Primary display was DISPLAY29, 5120x2160 after the NVIDIA driver update. Six
controllers were online at activation, four at the final read-only preview;
physical light output was not re-confirmed by the user during this logging task.
The final 12.42-second sample measured 14.90 Hz and 0.279% whole-machine CPU;
this is a short observation rather than a sustained performance benchmark.

The existing sign-in task returned zero and reused the sole owner, PID 19700,
without opening a panel. Startup binding and desktop shortcut point to 0.7.4.
Candidate and obsolete 0.7.3 binaries were transactionally removed after consumer
migration (171,599,016 logical bytes), along with spent E: task scratch
(487,816,409 logical bytes). Only 0.7.4 remains under releases. Recovery packages
and original crash dumps/symbols remain intentionally retained.

Local evidence: `D:/Tools/OpenRGB/validation/20261105/journal/`: final-delivery,
final-activation, final-journal, final-capture, final-performance, CI receipt and
cleanup receipts. Driver-update observations are separate: the new journal was
activated after installation, so it does not claim to have journaled that update.
The earlier empty generic OpenRGB log and historical DirectX deadlock cause remain
unresolved; no crash attribution or capture-policy change is inferred from them.
