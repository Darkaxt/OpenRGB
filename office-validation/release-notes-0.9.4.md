Fix nighttime lighting resuming when Windows clears its screensaver state.

After an automatic screensaver is observed, Office Ambilight now keeps every
mapped light black and releases Awake until Windows reports new session input
on a usable normal desktop. Display wake/topology changes, a return to the Default
desktop and wallpaper capture alone cannot turn the lights back on.

The resume gate survives app restart in separate private runtime state. Input or
storage query failures keep lighting off and appear in diagnostics. No input
contents are recorded, no input hooks are installed, and the selected power plan,
screensaver settings, saved RGB topology and screen adjustments are preserved.

Existing Awake controls and manual pause menus are retained. Output resumes using
a fresh captured frame after valid activity. The prior0.9.3 release is retained
for rollback.
