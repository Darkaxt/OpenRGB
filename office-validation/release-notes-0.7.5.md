Ambilight can now follow the main display's applied dimming, including LightBulb,
through read-only Windows gamma-ramp queries. The measured factor multiplies the
existing manual brightness baseline after colour sampling and before output
smoothing. A static wallpaper can therefore respond to dimming without another
capture or GPU sampling pass.

Control → Advanced options → Output balance exposes the follow toggle and current
readback status. Following defaults on for existing maps without rewriting their
saved settings. Identify/calibration reference colours and black rest output are
preserved. Temperature attenuation does not change LED hue. Failed reads retain
the last valid factor only for the same display; nonlinear calibration ramps are
reported as unsupported. Physical monitor backlight and HDR tone mapping are not
measured by this method. LightBulb and display gamma are never modified.
