Platform: the nano-z80
======================

The [nano-z80](https://github.com/venomix666/nano-z80) is a Z80 based SoC for the [Tang Nano 20k FPGA Board](https://wiki.sipeed.com/hardware/en/tang/tang-nano-20k/nano-20k.html). It is specifically designed to run CP/M but on modern hardware - with HDMI output, USB keyboard, SD-card and the processor running at ~25 MHz.

What you get with this port:

- 14x4 MB drives on the SD-card
- Most of an ADM-3a / Kaypro II terminal emulator supporting 80x30 text
- A TPA of 57 kB
- Two serial ports, one on the built in USB UART and on a TTL UART header
- A crude but functional terminal program with X-modem file transfer support
- Utilities for changing baudrate and setting the display color
- A fully implemented IO-byte which allows using monitor/keyboard or any of serial ports for the console.

How to use it
-------------
Write `nano-z80.img` to a micro-SD card using `dd` and press `B` in the nano-z80 monitor to boot from the SD-card.

By default, only drive `A:` is formatted. To use the additional drives, run `mkfs B:` up to `mkfs N:` to format the other drives once you have booted to CP/M.

UART B (the one on the TTL UART header) supports changing baudrates, this can be done either using the `baudrate.com` tool or from inside `nanoterm`.

If you put the SD-card in a SD-card reader on a Linux machine, the diskdefs file in the
cpmish root allows you to read and write files to the A: drive, e.g.:

    cpmcp -f nanoz80 -i /dev/sdf 0:oncpm onlinux

Modifying the IO byte at boot
--------------
The IO is mapped in the following way:
- CRT: USB keyboard and HDMI output
- TTY/LPT: UART header on carrier board
- PTP/PTR/UC1: USB UART on Tang Nano 20k board

The default value is 0x81, so that the HDMI output and USB keyboard is used for the console. It can be modified according to the table below before booting by first loading to image from the SD-card using the `L` command in the monitor and then writing to address 0xF833 by running for instance `WF633,83` to redirect the console to the USB UART, and then booting by running `JF600`. 

As the monitor is diplayed both on the USB UART and the HDMI-output/USB-keyboard by default, this can be useful when running with no external display connected.
```
                     LIST    PUNCH    READER    CONSOLE  
0x81 - 10 00 00 01 - LPT:    TTY:     TTY:      CRT:  
0x95 - 10 01 01 01 - LPT:    PTP:     PTR:      CRT:  
0x80 - 10 00 00 00 - LPT:    TTY:     TTY:      TTY:  
0x83 - 10 00 00 11 - LTP:    TTY:     TTY:      UC1:  
0x97 - 10 01 01 11 - LTP:    PTP:     PTR:      UC1:  
```


Who?
----

CP/Mish  was written David Given, and is covered under the terms of the whole CP/Mish project. See the documentation in the project root for more information. This port and the nano-z80 project was made by [Henrik Löfgren](https://github.com/venomix666/).






