# Capture lifetime while lighting is disabled

Specification R47/R48/R49. Existing implementation authority applies; the user
requires direct controls and no repeated host lighting/capture experiments.

41 COMPLETE: release capture/GPU/preview input for lighting pause, output pause and
global disable; fresh image acquisition after resume. Static startup bridge is
one file read and uses no WGC session. Independent gamma/Awake policy preserved.
Hosted Windows lifecycle/source/preview/rest/GPU checks passed for
Ambient054a6b95b25495a9e8b9d8228f1605c48757b4df, CI42332547954. The output
fixture now supplies fresh input after resume instead of expecting cached colours
to survive pause. Actual native Awake remains independent during pause. No
blockers/deferrals or required refactoring remain in41.

42 ACTIVE: final0.9.6 normal release, package/installed provenance, one
activation through existing startup scripts, read-only status and unchanged
private settings verification. No Computer Use, screenshots, recovery commands
or pause/resume experiments on the user's desktop. Prior0.9.5 retained.

Yellow border: Ambilight exit did not remove it; stopping this chat's retained
Computer Use helper91732 did, confirmed by user. Do not attribute that border to
Ambilight or recreate the Computer Use session. Ambilight remains stopped until
the verified final build is ready for its single activation.

Scratch E:/Temp/openrgb-pause-20261107, cleanup transaction
e5cd037e3594b07500e3b101a2015e2d. Retained evidence
D:/Tools/OpenRGB/validation/20261107/pause-capture.
