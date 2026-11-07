Disabling RGB lighting now releases live capture and GPU/preview input instead
of merely suppressing controller output. Capture stays stopped throughout the
pause, including across restart. Re-enabling lighting follows the existing
rest/input gates and acquires fresh imagery.

Gamma adjustments and Awake remain independent. A live-preview request while
lighting is disabled returns an explicit paused state. The static startup bridge
still reads the existing Windows wallpaper image once and uses no desktop
capture session.

Hosted Windows verification covers the production pause/resume/source lifecycle,
independent native Awake requests, preview behavior, GPU sampling and rest gates.
Delivery verification uses only app-owned readiness and read-only status; no
desktop screenshots or live lighting/capture experiments are required.
