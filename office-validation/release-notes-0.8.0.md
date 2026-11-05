Office Ambilight now runs its interface, tray and OpenRGB device engine in one
application. Opening the shortcut reveals the existing process; sign-in stays
quiet. Capture and lighting output have their own event thread so interface
work does not stall them.

- Devices adds native hardware profiles, discovery, identity, mode controls,
  hardware zones and supported driver options in the existing Office style.
- Explicit per-device hardware effects survive reconnect/restart. Rest and
  temporary tests return to the selected owner afterward.
- Existing topology, wallpaper/app policy, preview blur, brightness following,
  screensaver/lock rest and diagnostics are retained.
- Window, tray and shortcut reuse the genuine OpenRGB icon.
- Topology saves preserve untouched settings and display aliases.

Windows native/plugin regressions and actual application renders passed,
including 150/200% scaling. Live checks verified all six office controllers,
profile Save/Load, rescan, native ownership persistence, unchanged saved map and
fresh main-display capture. A hidden-UI sample measured approximately 15 FPS,
0.37% total CPU and 99 MB working set; usage varies with capture/UI demand.

The Windows x64 ZIP includes the unified application and runtime. Private state
is excluded. Continue using the supplied Office launcher with your existing state
directory; the obsolete OfficeControl executable is no longer needed.
