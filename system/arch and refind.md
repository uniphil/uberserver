Most of the [Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide) applies. Here are notes that are mostly specific to the Macbook 2,1. The [Macbook wiki page](https://wiki.archlinux.org/index.php/MacBook) is worth a read.

1) The [arch ISO image](https://www.archlinux.org/download/) needs to be [modified](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#Remove_UEFI_boot_support_from_ISO) to remove UEFI.

... erm, I couldn't actually boot my no-UEFI image. Probably screwed something up. @jameh made the original one we used, so I used it instead.

2) Partitioning

uberserver's layout:

* 500GB HD sda

  sda1: 200M   EF00 fat32 for EFI
  sda2: 50G    8300 ext4  root
  sda3: 411.6G 8300 ext4  home
  sda4: 4G     8300 swap

The macbook 2,1 will need at least:

 1. a fat32 partition for efi
 2. another partion (ext4 is pretty solid) for `/`.


3) Mount everything [with `noatime`](https://wiki.archlinux.org/index.php/Pro_Audio#System_Configuration) in fstab. Just swap out the `relatime`s with `noatime`. This step is just for avoiding xruns in JACK.

4) ramdisk modules: add `ahci` and `sd_mod` to MODULES (`/etc/mkinitcpio.conf`) before running `mkinitcpio -p linux`.


## 5) Refind

_(the tricky part)_

chroot into your system

```bash
# mount /dev/sda2 /mnt
# arch-chroot /mnt /bin/bash
```

install wget `# pacman -S wget`

wget rod's refind from sourceforge (the first one, "A binary zip file", not the gnu-efi variant package.)

get unzip `# pacman -S unzip`

unzip and go to, and install refind

```bash
# unzip refind-bin-XXXXX.zip
# cd refind-bin-XXXXX
# sh install.sh
```

You should get `Installation has completed successfully.`

---------------------------------------------------------------


6) grub

The 2,1 has 32-bit efi, but we're installing a 64-bit os (the intel dual core is 64-bit). Kernel stub EFI bootloading only works on systems where the bit-widths match, so we need ugly old grub as an intermediary.

```bash
# pacman -S grub-efi-i386
# grub-install --target=i386-efi
# grub-mkconfig -o /boot/grub/grub.cfg
```

yay
