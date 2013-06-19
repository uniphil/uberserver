Network Time Protocol Dameon:
```bash
pacman -S ntp
```


inside /etc/ntp.conf :
```
#...
server 0.ca.pool.ntp.org iburst
server 1.ca.pool.ntp.org iburst
server 2.ca.pool.ntp.org iburst
server 3.ca.pool.ntp.org iburst
#...
```


```bash
systemctl enable ntpd
systemctl start ntpd
```