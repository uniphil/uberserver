
todo:

 * set up flexget for tv shows
 * fix the xbmc scan trigger to scan the video or music library based on which watch folder the torrent was added to.

rutorrent is set up as a web front-end.

rtorrent service file set up as per https://wiki.archlinux.org/index.php/RTorrent#systemd_service_file_with_tmux

`.rtorrent.rc`:

```
# NOTE: ~/.rtorrent.rc should symlink to this file.


## PEERS AND SPEED
min_peers = 100  ; try to keep asking until this is reached
max_peers = 300  ; stop asking when this is reached
min_peers_seed = 50
max_peers_seed = 100

download_rate = 0
upload_rate = 175

## BASIC CONFIG STUFF

encoding_list = UTF-8
check_hash = yes
directory = /home/ship/torrent/data  ; default destination for torrents (nothing should ever land here?)
session = /home/ship/torrent/session  ; the magic.
schedule = low_diskspace,5,60,close_low_diskspace=100M  ; don't completely fill the disk (the right disk?)
port_range = 49164-49164  ; arch wiki says just one port should be used
#encryption = require,require_RC4,allow_incoming,enable_retry  ; force encryption, at the cost of possibly fewer peers
encryption = allow_incoming,try_outgoing,enable_retry  ; prefer encryption
dht = disable  ; don't to dht. since it's all private tracker stuff.
schedule = filter_active,30,30,"view_filter = active,\"or={d.get_up_rate=,d.get_down_rate=}\""  ; what's goin on (press 9)
schedule = session_save,300,300,session_save=  ; periodically save session data
schedule = untied_directory,1,30,close_untied=  ; stop deleted torrents
schedule = tied_directory,02:00:00,24:00:00,load_tied=  ; restart re-added torrents

# a view that's sorted by ratio? maybe?
#view_add = ratio
#view_sort_new = ratio,greater=d.getratio=
#view_sort_current = ratio,greater=d.get_ratio=

## WATCH FOLDERS

schedule = watch_data,1,5,"load=/home/ship/torrent/watch/data/*.torrent"  ; will go to the default ~/torrent/data dir

# cool watchy watchy stuff
schedule = watch_jamie_music,2,5,"load=/home/ship/torrent/watch/jamie/whatcd_music/*.torrent,d.set_directory=/home/ship/media/Music/Jamie_whatcd/,d.set_custom2=\"music\""
schedule = watch_jamie_other,3,5,"load=/home/ship/torrent/watch/jamie/whatcd_other/*.torrent,d.set_directory=/home/ship/media/Stuff/Jamie/Whatcd_other/"
schedule = watch_phil_music,4,5,"load=/home/ship/torrent/watch/phil/what/*.torrent,d.set_directory=/home/ship/media/Music/Phil/what/,d.set_custom2=\"music\""
schedule = watch_phil_other,5,5,"load=/home/ship/torrent/watch/phil/what_other/*.torrent,d.set_directory=/home/ship/media/Stuff/Phil/otherwhat/"
schedule = watch_phil_ptp,5,1,"load=/home/ship/torrent/watch/phil/ptp/*.torrent,d.set_directory=/home/ship/media/Movies/Phil/ptp/,d.set_custom2=\"movie\""
schedule = watch_amani_what,5,2,"load=/home/ship/torrent/watch/amani/what/*.torrent,d.set_directory=/home/ship/media/Music/Amani/,d.set_custom2=\"music\""

# scan the appropriate xbmc library on torrent completion
system.method.set_key = event.download.finished,scan_xbmc,"execute=/home/ship/code/xbmc-scan/scan.py,$d.get_custom2="


## SCHEUDLING

# throttling
schedule = throttle_up_off,02:00:00,24:00:00,upload_rate=0
schedule = throttle_up,08:00:00,24:00:00,upload_rate=175k  ; leave a bit of breathing room during the day

# start everything that's been loaded once downloads are free
# DISABLE WHILE SETTING UP STUFF
schedule = start_loaded,02:00:00,24:00:00,"d.multicall=,d.start="

# xmlrpc for other UI controls
scgi_port = localhost:5000

```

