# Lighting intensity mixer

Authoritative specification R50/R51/R52/R53/R54. User requested a global fullscreen
intensity and then a BetterTrumpet-style controller whose individual rows are
physical light-emitting devices, not apps. Existing release authorization applies.

43 COMPLETE: source497848b32682c1b523b78c34dda7a28ded59b3fc,
CI42399208049 passed. Actual sliders -> production save -> native output,
master/device/fullscreen policy, offline reconnect, durable persistence and stale
edit protection verified. User feedback incorporated: master/device rows only
in tray, fullscreen policy in main Output, greenish palette and modern matching
context menus. App-owned flyout/menu/Output renders and measured hit targets
reviewed at100/150/200%. Earlier offline fixture assertion was corrected to
respect its missing owner; no production behavior was weakened. No blockers,
deferrals or required refactoring. Existing0.9.6 owner remains untouched so far.

44 ACTIVE: final normal0.9.7 package/release, independent retrieval,
installed module/startup/read-only verification and cleanup. No host UI automation,
capture recovery, fullscreen simulation or pause/resume experiment.

Design reference: user screenshot and inspected D:/Projects/BetterTrumpet
FlyoutWindow.xaml/.xaml.cs, DeviceView.xaml, VolumeSlider.cs, FlyoutViewModel.cs.
Native420px Qt flyout; user revised the palette to greenish teal, mint sliders,
existing app fonts and matching modern rounded context menus. Master at top and
one row per physical device; fullscreen setting lives in the main Output card.
Source6cda656 contains this cohesive feedback update. Hosted app-owned renders
and metrics cover expanded/collapsed/offline, context menu and Output card at
100/150/200%. No new host app activation has occurred.
User explicitly reaffirmed single-click mixer and double-click full app. The
production tray handler implements that mapping. Qt6.8.3's Windows tray source
confirms that the release following DoubleClick is ignored, so it cannot reopen
the mixer after opening the panel. Primary source:
https://github.com/qt/qtbase/blob/v6.8.3/src/plugins/platforms/windows/qwindowssystemtrayicon.cpp

Scratch E:/Temp/openrgb-intensity-20261107, cleanup transaction
5499a7f65381ea1ec0c0534adf5150fc. Durable current evidence will be retained under
D:/Tools/OpenRGB/validation/20261107/intensity-mixer.
