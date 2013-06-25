exporting 192.168.1.0/24:/srv/nfs4/watch
exporting 192.168.1.0/24:/srv/nfs4/media
exporting 192.168.1.0/24:/srv/nfs4

in /etc/exports:
```
/srv/nfs4
192.168.1.0/24(ro,fsid=root,no_subtree_check,nohide,all_squash,anonuid=1000,anongid=100)
/srv/nfs4/media
192.168.1.0/24(rw,no_subtree_check,nohide,all_squash,anonuid=1000,anongid=100)
/srv/nfs4/watch
192.168.1.0/24(rw,no_subtree_check,nohide,all_squash,anonuid=1000,anongid=100)
```

in /etc/fstab:
```
#bind mounts for nfs4
/media/home	/srv/nfs4/media	ext4	bind	0	0
/home/ship/torrent/watch	/srv/nfs4/watch	ext4	bind	0	0
```

systemctl start nfsd
systemctl enable nfsd
