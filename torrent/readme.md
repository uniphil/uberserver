rtorrent

service file set up as per https://wiki.archlinux.org/index.php/RTorrent#systemd_service_file_with_tmux

`.rtorrent.rc`:

```
# NOTE: ~/.rtorrent.rc should symlink to this file.


## BASIC CONFIG STUFF

check_hash = yes
directory = /home/ship/torrent/data  ; default destination for torrents (nothing should ever land here?)
session = /home/ship/torrent/session  ; the magic.
schedule = low_diskspace,5,60,close_low_diskspace=100M  ; don't completely fill the disk (the right disk?)
port_range = 49164-49164  ; arch wiki says just one port should be used
encryption = require,require_RC4,allow_incoming,enable_retry  ; force encryption, at the cost of possibly fewer peers
dht = disable  ; don't to dht. since it's all private tracker stuff.
schedule = filter_active,30,30,"view_filter = active,\"or={d.get_up_rate=,d.get_down_rate=}\""  ; what's goin on (press 9)

## WATCH FOLDERS

schedule = watch_data,1,5,"load=/home/ship/torrent/watch/data/*.torrent"  ; will go to the default ~/torrent/data dir

# cool watchy watchy stuff
schedule = watch_jamie_music,2,5,"load=/home/ship/torrent/watch/jamie/whatcd_music/*.torrent,d.set_directory=/home/ship/media/Music/Jamie_whatcd/"
schedule = watch_jamie_other,3,5,"load=/home/ship/torrent/watch/jamie/whatcd_other/*.torrent,d.set_directory=/home/ship/media/Stuff/Jamie/Whatcd_other/"
schedule = watch_phil_music,4,5,"load=/home/ship/torrent/watch/phil/what/*.torrent,d.set_directory=/home/ship/media/Music/Phil/what/"
schedule = watch_phil_other,5,5,"load=/home/ship/torrent/watch/phil/what_other/*.torrent,d.set_directory=/home/ship/media/Stuff/Phil/otherwhat/"
schedule = watch_phil_ptp,5,1,"load=/home/ship/torrent/watch/phil/ptp/*.torrent,d.set_directory=/home/ship/media/Movies/Phil/PTP/"
schedule = watch_amani_what,5,2,"load=/home/ship/torrent/watch/amani/what/*.torrent,d.set_directory=/home/ship/media/Music/Amani/"


## SCHEUDLING

# throttling
schedule = throttle_up_off,02:00:00,24:00:00,upload_rate=0
schedule = throttle_up,08:00:00,24:00:00,upload_rate=125k  ; leave a bit of breathing room during the day

# start everything that's been loaded once downloads are free
schedule = start_loaded,02:00:00,24:00:00,"d.multicall=,d.start="

```

todo:

* set up xmlrpc and a web front-end
* scan xbmc libraries on torrent completion
* set up flexget for awesomeness
