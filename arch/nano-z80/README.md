Platform: the nano-z80
======================

The [nano-z80](https://github.com/venomix666/nano-z80) is a Z80 based SoC for the [Tang Nano 20k FPGA Board](https://wiki.sipeed.com/hardware/en/tang/tang-nano-20k/nano-20k.html). It is specifically designed to run CP/M but on modern hardware - with HDMI output, USB keyboard, SD-card and the processor running at ~25 MHz.

What you get with this port:

- 16x2 Mb drives on the SD-card
- Most of an ADM-3a / Kaypro II terminal emulator supporting 80x30 text
- A TPA of about 60kB
- Two serial ports, one on the built in USB UART and on a TTL UART header
- A crude but functional terminal program with X-modem file transfer support
- A fully implemented IO-byte which allows using monitor/keyboard or any of serial ports for the console.

How to use it
-------------
Write `nano-z80.img` to a micro-SD card using `dd` and press `B` in the nano-z80 monitor to boot from the SD-card.

By default, only drive `A:` is formatted. To use the additional drives, run `mkfs B:` up to `mkfs P:` to format the other drives once you have booted to CP/M.

UART B (the one on the TTL UART header) supports changing baudrates, this can be done either using the `baudrate.com` tool or from inside `nanoterm`.


Who?
----

This port and the nano-z80 project was made by [Henrik Löfgren](https://github.com/venomix666/).






