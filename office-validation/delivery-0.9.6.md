# Office Ambilight 1.1-office.0.9.6 delivery

R47/R48/R49 and stages41/42 are satisfied. The separate yellow-border incident
was traced to the retained Computer Use helper, whose stop removed the border
while Ambilight was already closed. No desktop-control tool was used for this
delivery.

- Published normal release: https://github.com/Darkaxt/OpenRGB/releases/tag/v1.1-office.0.9.6
- Root source/tag: e39b30063eff7a91e8f5b0e8ea568c0a5d333875.
- Ambient source: 054a6b95b25495a9e8b9d8228f1605c48757b4df.
- Hosted Windows CI42332547954 passed lifecycle, preview, rest, GPU, static
  image and independent Awake/gamma checks. Disabled lighting creates no source
  acquisition; resume requires fresh input. Existing static bridge reads a file.
- Published ZIP SHA256: 6df47cfdbf820dc4073860313d1c9fd4bd191db5733ba054f230b8c42d988817.
  Independently downloaded ZIP, checksum and GitHub asset digest agree.
- Package provenance and private-state exclusion passed; invalid plugin/runtime
  digests were rejected before installation. All149 installed members match.
- Installed D:/Tools/OpenRGB/releases/1.1-office.0.9.6; one normal existing
  sign-in task activation, one native owner. Loaded plugin digest
  344d27065d97af0737c3becd1980c7102dd6dc33bf06e11c30a9a4d9178f3373.
- Read-only IPC confirmed capture policy matching current enabled preferences,
  valid gamma and required wireless devices H6609/H8048/Secretlab. No live
  pause/resume or capture-recovery experiment. Natural-use logs remain available.
- All saved lighting/screen/Awake/rest settings and OS screensaver/power plan
  preserved; startup Interactive/Limited/IgnoreNew/PT0S unchanged.
- Prior0.9.5 remains the rollback installation. No pending blockers/deferrals.
- Disposable verification downloads/checks removed through reviewed cleanup
  transaction e5cd037e3594b07500e3b101a2015e2d; no residuals.

Private retained receipts and CI logs:
D:/Tools/OpenRGB/validation/20261107/pause-capture.
No credentials, raw screenshots or private settings are included here.
