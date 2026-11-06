Office Ambilight now includes Awake in its existing tray menu.

- Automatic protects maximized or fullscreen applications on the Windows main
  display from automatic screensaver/display sleep. Restoring, minimizing or
  closing the last qualifying application releases the request.
- Manual interval, expiration date/time, indefinite, Off and Keep screen on
  controls replace the separate Awake tray workflow. The default intervals are
  30 minutes, one hour and two hours, with existing PowerToys custom preferences
  imported when present. Expired timers return to Off.
- Manual modes with Keep screen on unchecked prevent system sleep while allowing
  display sleep. Mode, preferences and deadlines survive application restart.
- Uses scoped Windows power-request handles and leaves the selected power plan,
  screensaver configuration, existing lighting/screen pause controls and other
  PowerToys utilities unchanged.

The package retains the existing single RGB/gamma owner, private settings and
startup path. The prior0.9.2 package remains available for rollback.
