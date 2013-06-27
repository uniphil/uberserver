all the audio stuff to get the firebox going

also, connect pulseaudio when jack starts

jack will be set up to run as a service on boot (as root), not under a particular user.

some funny `systemd` tricks are needed to enable realtime support in the `cgroup` that `systemd` puts JACK in.

`dbus` makes all of this really fun...

Ideally, this service will actually just be started on-demand whenever XBMC is launched, and stopped afterward. `JACK` really demands that the system be running full-power, but the server doesn't need that when XBMC is not being used.

```bash
# pacman -S jack2
# mkdir /etc/jack
```

Here is the service file for `JACK` (`/etc/jack/jack.service`)

```
[Unit]
Description=Jack Audio Connection Kit

[Service]
User=root
ControlGroup=cpu:/
ExecStart=/etc/jack/start-jack.sh
ExecStop=/etc/jack/stop-jack.sh

[Install]
WantedBy=multi-user.target
```

note: currently using [option 2](http://www.freedesktop.org/wiki/Software/systemd/MyServiceCantGetRealtime) to get realtime.

`/etc/jack/start-jack.sh` (don't forget to `# chmod +x`)

```
#!/bin/bash
jackd -d firewire
```

`~/.xinitrc` (for user `ship`)
```
pacmd suspend true
exec xbmc-standalone
pactl load-module module-jack-sink channels=2
pacmd set-default-sink jack_out
```

retrying without pulseaudio...

install alsa as per beginner's guide

install alsa-plugins

install jack2

install python2-dbus

find what the ports are called with jack_lsp

alsa is set up with /etc/asound.conf for jack which works(!!!)... but xbmc ignores it and only finds hardware devices.

installed xbmc-git

... audio still doesn't work. back to...


### pulseaudio.

made sure jack module gets loaded (https://wiki.archlinux.org/index.php/PulseAudio/Examples#PulseAudio_through_JACK_the_new_new_way)

installed pavucontrol, turned off the default internal sound card

yay sound from xbmc!

boo 6-channel surround bullshit from xbmc, setting it to 2.0 channel does nothing.

options

1. fix xbmc, have it obey the number of channels selected. nat.
2. fix pulse jack loader. tell it to only use 2 channels connected to jack. nat.
3. fix jack firewire start-up to only initiate with 2 channels. hmm....
4. downmix from jack. ugh. (most realistic? really?)


taking path #2 (or at least assuming someone else may have)

install pulseaudio-git from aur

`/etc/pulse/default.pa`
```
load-module module-jackdbus-detect channels=2
```

hooray! (hopefully this will work in the main pulseaudio soon...)


## X-Runs

default setup yeilds frequent x-runs running JACK for my firebox.

1. install cpupower and set the governer to `performance` https://wiki.archlinux.org/index.php/Cpufreq

```
# pacman -S cpupower
# cpupower frequency-set -g performance
```

the second one is not persistent.


... and then do everything on the pro audio page except the rt-kernel. wouldn't hurt, but takes FOREVER to compile...

still get some x-runs when starting/stopping, but otherwise it's pretty smooth.


... installing linux-rt (from aur) takes care of the rest of the x-runs. don't forget `# grub-mkconfig -o /boot/grub/grub.cfg`


rtkit group???????????
