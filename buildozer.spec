[app]

# (str) Title of your application
title = TrendApp

# (str) Package name
package.name = trendapp

# (str) Package domain (needed for android/ios packaging)
package.domain = shikharsolutions.co.in

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let Kivy find these!)
source.include_exts = py,png,jpg,kv,txt,xlsx

# (list) Application requirements
requirements = python3.10.8,kivy,openpyxl,pandas,yfinance,plotly,numpy

# (str) Custom source folders for requirements
# Separate with commas to add multiple directories
requirements.source.kivy = /path/to/your/kivy/source

# (list) Presplash of the application
presplash.filename = presplash.png

# (list) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0: False, 1: True)
warn_on_root = 1
