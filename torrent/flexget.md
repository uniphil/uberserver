manage tv series watchlist on trakt, movie watchlist on imdb

## tv series

flexget task is like this:

```yaml
  trakt series from btn:
    rss: https://broadcasthe.net/feeds.php?feed=torrents_episode&user=#####&auth=########&authkey=########
    import_series:
      from:
        trakt_list:
          api_key: ######
          username: uniphil
          series: watchlist
      settings:
        quality: 720p+ webrip+
    set:
      path: /home/ship/torrents/tv_shows/phil/btn/{{ series_name }}/Season {{ series_season }}
    download: yes
```

(and of course rtorrent is watching the btn folder)


## movies

... are harder.

this flexget tasks queues tasks from imdb watchlist:

```yaml
  queue imdb watchlist:
    priority: 1
    imdb_list:
      user_id: ur34010952
      list: watchlist
    accept_all: yes
    queue_movies: yes
```

and then we have to search ptp for things in the queue. I don't think the vanilla forms plugin will work to log in, because it only seems to accept `username` and `password`. [ptp also needs your passkey](http://passthepopcorn.me/forums.php?page=3&action=viewthread&threadid=15602)

> Instead of login.php, now you have to POST the username and password to ajax.php?action=login. New requirement is the sending of the passkey.

