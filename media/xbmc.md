## old

x has been set up (with `xorg-xinit` and everything as per the beginner's guide).

optional dependancies installed:

 * `upower`

make xbmc go

```bash
$ echo "exec xbmc-standalone" > ~/.xinitrc
```

and then it's just `$ startx`.


## current

`xbmc` is installed with pacman (not `xbmc-git` from AUR, though that was tried).

### aux jack addon

[`script.audio.jack`](script.audio.jack) is sym-linked to `~/.xbmc/addons/` (something like `$ ln -s /path/to/script.audio.jack ~/.xbmc/addons/`)

patch the line-in ports to the main outs through the firebox. we've got a 3.5mm stereo -> 2 mono 1/4" cord always plugged into line-in for playing off phones/mp3 players etc.

the current addon is pretty hack -- a dirty script with jack ports hardcoded and stuff.
