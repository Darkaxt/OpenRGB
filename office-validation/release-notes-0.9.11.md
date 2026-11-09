# Office Ambilight 1.1-office.0.9.11

Fix the lighting widget opening with clipped or missing content and needing a
second opening. The tray screen, hidden child layouts, final viewport and window
bounds are now prepared before the first show and acrylic clip. Layout sizing
uses explicit measured bounds instead of Qt's top-level two-thirds-screen cap.
Changing the material tint no longer replaces a stylesheet during presentation.

Native first-frame and reopen checks passed at100% and150% scaling, including
the right-hand master slider, footer, bounded scrolling and stable geometry.
Existing native acrylic, rounded corners, pin/collapse/anchor, product icons and
intensity behavior are preserved. No periodic repaint, delay or automatic reopen.

Ambient source3588c395e11f8723fc8e1857e58b6f67b73a64b1;
successful hosted Windows verification42646493749. Source-bound native captures
show the complete first frame without a corrective QWidget repaint. No user
desktop capture, lighting experiment or Wallpaper Engine restart was performed.
