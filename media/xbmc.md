
x has been set up (with `xorg-xinit` and everything as per the beginner's guide).

optional dependancies installed:

 * `upower`

make xbmc go

```bash
$ echo "exec xbmc-standalone" > ~/.xinitrc
```

and then it's just `$ startx`.
