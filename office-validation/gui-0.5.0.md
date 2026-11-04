# Office Ambilight 0.5.0 — corresponding-page reconciliation

The retained Ambient `design-reference/VISUAL-PARITY-CHECKLIST.md` is the failed
0.4.0 baseline. This document records its resolution without rewriting that
historical evidence. Final delivery status is recorded at the end.

Reference: modern EDAmbilight `ss-*` family, including the user's Settings image.
Evidence root: `D:/Tools/OpenRGB/validation/20261104/gui-0.5.0`.
Native renders cover 1000×700, 1440×900 and 1920×1080, plus 150% scaling.
`preflight-views` and `rotation-views` are earlier iterations; `refined-views`
exposed an export-only shutdown dialog and is not a successful exporter result.
Use the final versioned exports and their JSON receipt for acceptance.

## Shared shell and controls

| Item | Resolution |
|---|---|
| A01 | Exact 80 logical-pixel rail and zero surrounding margin. |
| A02 | Recovered brightness symbol replaces RGB text. |
| A03 | Concentric rings, illumination and sonar; reduced-motion preference. |
| A04 | Actual recovered Material Symbols, not substitute platform icons. |
| A05 | 26px symbols with small uppercase labels below. |
| A06 | Narrow cyan active bar and horizontal gradient. |
| A07 | Keyboard focus is a separate dotted neutral outline. |
| A08 | Rail separators and bottom package version. |
| A09 | Page-specific headings, including separate Help and Diagnostics. |
| A10 | Compact 48px header with rules and tracked subtitle. |
| A11 | Help destination, with diagnostics separately accessible. |
| A12 | Save/reload footer only on Control and Topology. |
| A13 | Restrained navy radial illumination and fine scanline depth. |
| B01 | Original Orbitron outlines, renamed Office Display under OFL. |
| B02 | Original Rajdhani outlines, renamed Office Body under OFL. |
| B03 | Eyebrow, helper, label and numerical readout hierarchy. |
| B04 | Custom-painted double-bezel cards replace QGroupBox captions. |
| B05 | Gradient surfaces and inset highlights. |
| B06 | 20px rounding and fine cyan corner accents. |
| B07 | Transparent label backgrounds; no dark strips. |
| B08 | Real custom-painted circular slider handles, pointer-to-value tested. |
| B09 | Compact cyan editable readouts and vector step buttons. |
| B10 | Pill switches with real checkbox mouse/keyboard behavior. |
| B11 | Recessed fields and vector cyan chevrons. |
| B12 | Compact icon actions with primary/secondary/disabled states. |
| B13 | Recovered icons in card headings and actions. |
| B14 | Quiet narrow scrollbars without platform arrow blocks. |
| B15 | Hover/press/focus feedback and visible-only sonar; Reduce interface motion. |
| B16 | Shared card padding and consistent label/control spacing. |

## Corresponding pages

| Item | Resolution |
|---|---|
| C01 | Tall Status; three upper and four lower cards; Devices below. |
| C02 | Status spans the two control rows. |
| C03 | Native painted status dot, short state/helper and bottom enable switch. |
| C04 | Cyan FPS readout above slider and measured output rate. |
| C05 | Compact WGC engine and LG source policy, with Help link. |
| C06 | Algorithm top-right with black-bar switch immediately below. |
| C07 | Separate fixed-depth and adaptive-depth cards. |
| C08 | Strategy-dependent enabled states initialized on first display. |
| C09 | EMA and scene-cut readouts/sliders, with mode under Advanced. |
| C10 | Saturation primary; brightness/luminance under Advanced. |
| C11 | Core dashboard fits normal viewport; compact windows scroll intentionally. |
| C12 | Actual device controls on dashboard, plus topology note. |
| C13 | Typed device metadata, enable switch, expandable Zones and topology links. |
| C14 | Preset chips and Advanced options disclosure. |
| C15 | Blur/adaptation/output/standby grouped under Advanced; explicit test/return. |
| D01 | Device tree, Grid config and Selected zone cards at left. |
| D02 | Grid readout/slider, Show grid and Snap controls together. |
| D03 | Framed canvas with shared bezel and bottom toolbar. |
| D04 | Grid has minimum visual spacing; actual LG preview remains unobscured. |
| D05 | Reload, Auto layout, Reset, Fit, Calibrate and Save below canvas. |
| D06 | Recovered toolbar symbols, plus Undo/Redo with accessible names. |
| D07 | Auto layout rearranges draft; Reset reloads saved map with discard protection. |
| D08 | Compact Zone inspector and separate Effect center. |
| D09 | Center X/Y side-by-side, with small placement chips. |
| D10 | Compact rotation/reverse row, edge choice and identify action. |
| D11 | Separate device/zone hierarchy and selected-zone identity/count summary. |
| D12 | Local order cue, first/last LED markers, Top label and shape-relative rotate handle. |
| D13 | Dedicated bottom strip with normalized bounds and interaction hints. |
| D14 | Native normalized XYWH/edge presets directly control sample extent/spacing; Help states this equivalent instead of inventing physical centimetres. |
| D15 | Calibration grouped in toolbar; explicit return-to-ambience control remains. |
| D16 | Empty inventory explanation, device-hub symbol and reconnect action; offline maps retained. |
| E01 | Three summary/action cards above inventory. |
| E02 | Cyan Orbitron counts. |
| E03 | Dedicated icon Flash all action. |
| E04 | Typed device cards with name, counts, status, enable, topology and Flash. |
| E05 | Distinct matrix/linear device glyphs and matrix colour. |
| E06 | Pill switches, dim disabled cards, disabled Flash for offline hardware. |
| E07 | Compact per-zone Map zone links. |
| E08 | Zone/topology counts separately labelled from connectivity. |
| E09 | Explicit empty/reconnect state, retaining offline-map semantics. |
| F01 | Centered 640px maximum Settings column. |
| F02 | Column starts below compact page header. |
| F03 | 32px icon badges and compact uppercase card labels. |
| F04 | Truthful local-owner directory/transport hierarchy; no fake SDK host/port. |
| F05 | Status left, compact Test/Reconnect right, separated by hairline. |
| F06 | Recovered test/save symbols. |
| F07 | Application replaces inapplicable Web Server, using the same card anatomy. |
| F08 | Startup/tray/motion switches and compact lifecycle/log actions. |
| F09 | Cyan display-font Office Ambilight wordmark. |
| F10 | Subdued package version aligned beside wordmark. |
| F11 | Divider, concise description and explicit attribution. |
| F12 | No map footer on Settings. |
| F13 | Centered compact card column with intentional surrounding space. |
| G01 | Live capture and original procedural animation are explicitly distinct tools. |
| G02 | Retained original procedural HTML/JS/fonts and controls, previously browser-verified. |
| G03 | Native Preview launches the original full-window playground with its own Back control; external default-browser presentation is explicit, avoiding another embedded capture renderer. |
| G04 | Native preview pill switch and icon action use shared control styling. |
| G05 | Centered original emblem geometry, rings, brand/subtitle and connection progress. |
| G06 | Distinct amber unavailable heading, wrapped explanation, Reconnect and Settings actions. |
| G07 | Original Eel error is historical runtime content and is deliberately not reproduced. |
| G08 | Help/onboarding is distinct from native diagnostics. |

Native adaptations above preserve the required single owner, occlusion-safe LG
policy, matrix keyboards, device identities and real sample geometry. The
reference's placeholder data, excluded-keyboard note and HTTP server are not
requirements to regress the working integration.

## Rotation and private-state continuity

The floating action and R key rotate by 90°, preserving monitor pixel aspect.
Its connector follows the selected region's own Top, including square shapes.
Per-LED quarter-turn metadata is validated and saved without changing indices.
Production widget tests cover click placement, orientation, undo/redo, four turns
and metadata serialization. The real panel Save exercise temporarily rotates and
renames a zone, reads back persisted orientation, then restores the exact map.
No private pairing tokens, maps or captured wallpaper images enter the package.

## Delivery status

ACTIVE: final exporter lifecycle check, final versioned package and installed
runtime/delivery verification remain. This record is not yet release completion.
