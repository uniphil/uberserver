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

