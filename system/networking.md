Network Time Protocol Dameon:
<code>
pacman -S ntp
</code>


inside /etc/ntp.conf :
<code>
#...
server 0.ca.pool.ntp.org iburst
server 1.ca.pool.ntp.org iburst
server 2.ca.pool.ntp.org iburst
server 3.ca.pool.ntp.org iburst
#...
</code>


<code>
systemctl enable ntpd
systemctl start ntpd
</code>