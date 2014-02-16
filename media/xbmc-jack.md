## install jack n stuff

1. pacman installed `alsa-utils` and `ffado`
2. installed jack from source. probably not necessary, but... `./waf configure --dbus --firewire --alsa --enable-pkg-config-dbus-service-dir`
3. pacman installed `qjackctl`
4. fix `/usr/local/bin/jack_control` to use python2 (`#!/usr/bin/env python2`)


## get jack_cpp

`git@github.com:x37v/jackcpp.git`

had to add `#include <unistd.h>` in `jackaudio.hpp` to make it build. The fix is in my fork (https://github.com/uniphil/jackcpp)

... and now the tests pass. yay!


## get xbmc

`git@github.com:xbmc/xbmc.git`

I forked it and then branched off the Frodo branch for my jack experiments.

Running `./bootstrap` warned that swig was not found, so I installed it (`pacman -S swig`) and then it ran without issue.

I also got `ccache` to speed things up since I'll probably be recompiling a lot (recommended in `README.linux`).

`./configure` failed on something that looked boost-related, so `pacman -S boost`....

`./configure` choked on arch's default python3 setup... `./configure PYTHON_VERSION=2.7` did it.

also needed `sudo pacman -S libgl glew tinyxml libmicrohttpd cmake gperf yasm ffmpeg`

After reviewing the config, I went ahead and also grabbed `sudo pacman -S lame libnfs libusb`

### build!
Before building, make sure you edit the top-level `Makefile` and add `-ljack` after `-lasound`.

`make -j2` (because my computer is dual-core)


... find something else to do forever while it compiles...

hahaha if failed at samba. back a step: `./configure --disable-samba PYTHON_VERSION=2.7`

aaaaaaand again. `make -j2`

installed but won't start (`/bin/sh: glxinfo: command not found`). `pacman -S mesa-demos`...

`sudo pacman -S xorg-xdpyinfo`


yeeeeeeeeeeeaaaaaaaaaaaaaaaaaaa!!! (it runs)


## runnin

initerestingly, when it starts up with jack already running, it throws an error a bunch of times: `jack_client_new: deprecated`.

scrolling through audio output device in settings > system > audio output, it freezes after pulseaudio for about 30 sec, the console logs that jack_client_new deprecation warning, and then it reverts the its default blank state.






### hack.

My efforts to make xbmc support jack:

https://github.com/uniphil/xbmc (see the `jack` branch)

(I borrowed a lot of ideas from http://yjpark.blogspot.ca/2009/11/xbmc-over-jack-revisited.html)

It works! Hooray! _Almost_ all the bugs we had before with puleaudio are gone:

 * UI sound enable/disable/only-when-stopped settings actually have an effect (they were always on before)
 * UI sounds now honour whatever the volume is set at (were always full volume before)
 * Crossfade settings are now honoured (were always on 5-ish seconds before with no way to disable)
 * No more system freezes and fewer audio glitches. So far...

XBMC still hangs after finishing playing an album sometimes (doesn't trigger `onPlaybackEnded`, UI stays as if it were playing a song [though the counter stops]). Although it seems to occur less frequently?

The most glaring issue right now is a very short audio dropout happening a couple seconds before the end of most songs when there is something queued up to be played next.

