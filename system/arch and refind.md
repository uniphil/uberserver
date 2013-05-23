Most of the [Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide) applies. Here are notes that are mostly specific to the Macbook 2,1. The [Macbook wiki page](https://wiki.archlinux.org/index.php/MacBook) is worth a read.

1) The [arch ISO image](https://www.archlinux.org/download/) needs to be [modified](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface#Remove_UEFI_boot_support_from_ISO) to remove UEFI.

... erm, I couldn't actually boot my no-UEFI image. Probably screwed something up. @jameh made the original one we used, so I used it instead.

2) Partitioning

* 500GB HD sda

  sda1: 200M   EF00 fat32 for EFI
  sda2: 50G    8300 ext4  root
  sda3: 411.6G 8300 ext4  home
  sda4: 4G     8300 swap


3) Mount everything [with `noatime`](https://wiki.archlinux.org/index.php/Pro_Audio#System_Configuration) in fstab. Just swap out the `relatime`s with `noatime`.
