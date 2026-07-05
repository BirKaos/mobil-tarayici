[app]
title = FoxBrowser
package.name = foxbrowser
package.domain = org.kaos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,android
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1


