# Office Awake 0.9.3

Authorization: already_authorized. Authoritative requirements: R38–R41 in
office-integration-specification.md, including Automatic in the Awake submenu.

- Stage35 ACTIVE: automatic/manual native feature and tray controls integrated.
  CI input fca2cda after run42246410270 compiled and passed real Qt tray/dialog
  checks, then identified the test's QThread-created hidden HWND preventing its
  private-desktop binding. The fixture now binds a native thread before Qt;
  rerun pending. Manual system-only requests also retain sleep protection while
  the display is off, as required by unchecked Keep screen on.
  Acceptance blockers: actual Windows behavior/menu checks, candidate/live owner
  and preserved-state verification. Internal, resolved by inspecting successful
  CI and exercising the resulting candidate. Stage36 depends on these results.
- Stage36 NOT STARTED: one normal0.9.3 release, independent package verification,
  installed/cold startup readback, rollback and cleanup. No tracked deferrals.

Scratch: E:/Temp/openrgb-awake-20261106. Native candidate on
D:/Tools/OpenRGB/candidates/1.1-office.0.9.3 needs local small-file/runtime I/O;
delete after last consumer. Exact-root cleanup transaction
e61c4b344c92e8e631f07050c38ad089 covers both. Retained acceptance evidence belongs
in D:/Tools/OpenRGB/validation/20261106/awake-0.9.3. Preserve0.9.2 rollback.
