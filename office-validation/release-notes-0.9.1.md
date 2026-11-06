# Office Ambilight 0.9.1

RGB lighting and LightBulb screen adjustments now share one native application
and bulb tray icon. Screen settings include day/night temperature and brightness,
solar/manual schedules, transitions, smoothing, app exclusions, hotkeys and preview.
Existing LightBulb settings are imported while the original file and RGB map remain
preserved. Lighting and screen adjustments have independent persistent disable
menus, with sunrise and explicit durations.

This release corrects the inherited Windows SDK shutdown fault found during 0.9.0
delivery verification. Failed socket accepts cannot start client workers, and
connection/sender threads finish before their resources are destroyed.

Display gamma baselines restore on exit, RGB brightness follows the applied factor
once, and the existing quiet sign-in starts the integrated application. Original
standalone LightBulb and Office 0.8.0 remain available for rollback. Includes MIT
attribution and exact LightBulb/native/plugin source provenance.
