1) pacman installed `alsa-utils` and `ffado`
2) installed jack from source. probably not necessary, but... `./waf configure --dbus --firewire --alsa --enable-pkg-config-dbus-service-dir`
3) pacman installed `qjackctl`
4) fix `/usr/local/bin/jack_control` to use python2 (`#!/usr/bin/env python2`)

