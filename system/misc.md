`/etc/issue`

```
       _~
    _~ )_)_~
    )_))_))_)
    _!__!__!_
    \____t__/
  ~~~~~~~~~~~~~

```
```

backup with
`backup.sh`

```
#!/bin/bash

rdiff-backup --exclude /media --exclude /srv --exclude /lost+found --exclude /tmp --exclude /mnt --exclude /proc --exclude /dev --exclude /sys / /media/home/sys/rdiff
```

run as user ship yeilds permission errors. and probably should be some kind of systemd thing anyway...
