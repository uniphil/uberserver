Uninstalled from server:
gdm
gnome-shell
gnome-control-center
gnome-user-share

installed:
bluez (5.5)
bluez-utils (5.5)


```bash
sudo hciconfig hci0 up
sudo systemctl start bluetooth
bluetoothctl
# connect **MAC ADDRESS**
```


add line to bluetooth.service:
```
ExecStartPre=/usr/bin/hciconfig hci0 up
```