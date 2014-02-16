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

### Install requirements

```sh
# depends
yaourt -S 'hicolor-icon-theme' 'fribidi' 'lzo2' 'smbclient' 'libtiff' 'libva' 'libpng' 'libcdio' 'yajl' 'libmysqlclient' 'libjpeg-turbo' 'libsamplerate' 'glew' 'libssh' 'libmicrohttpd' 'libxrandr' 'sdl_mixer' 'sdl_image' 'python2' 'libass' 'libmpeg2' 'libmad' 'libmodplug' 'jasper' 'rtmpdump' 'unzip' 'mesa-demos' 'xorg-xdpyinfo' 'libbluray' 'libnfs' 'afpfs-ng' 'avahi' 'bluez-libs' 'tinyxml' 'libcap' 'swig' 'taglib' 'java-runtime-headless' 'glu' 'mesa' 'shairplay-git' 'libxslt' 'libpulse'
# make depends
yaourt -S 'boost' 'cmake' 'git' 'gperf' 'nasm' 'libxinerama' 'zip' 'libva-vdpau-driver' 'libcec' 'udisks' 'upower')
```

### Get the source
`git@github.com:xbmc/xbmc.git`

I forked it and then branched off the Frodo branch for my jack experiments.

```
./bootstrap
```

Then, the following is important, else it cannot find samba:

```
sed -e 's/\(#include \)<libsmbclient\.h>/\1<samba-4.0\/libsmbclient\.h>/g' \
        -i xbmc/filesystem/SmbFile.cpp \
        -i xbmc/filesystem/SMBDirectory.cpp
```

I also got `ccache` to speed things up since I'll probably be recompiling a lot (recommended in `README.linux`).

Before `./configure`, we want to use python 2:

```
export PYTHON_VERSION=2
./configure
```

also needed `sudo pacman -S libgl yasm ffmpeg`

After reviewing the config, I went ahead and also grabbed `sudo pacman -S lame libusb`

Also, `sudo pacman -S mesa-demos xorg-xdpyinfo`.

### build!
Before building, make sure you edit the top-level `Makefile` and add `-ljack` after `-lasound`.

`make -j2` (because my computer is dual-core)

... find something else to do forever while it compiles...

installed but won't start (


yeeeeeeeeeeeaaaaaaaaaaaaaaaaaaa!!! (it runs)


## runnin

initerestingly, when it starts up with jack already running, it throws an error a bunch of times: `jack_client_new: deprecated`.

scrolling through audio output device in settings > system > audio output, it freezes after pulseaudio for about 30 sec, the console logs that `jack_client_new` deprecation warning, and then it reverts the its default blank state.

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

