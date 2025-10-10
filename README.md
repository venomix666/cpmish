CP/Mish
=======

What?
-----

CP/Mish is an open source CP/M distribution for the 8080 and Z80
architectures.

It contains a collection of software, some from Digital Research and some not,
all with proper open source licenses, integrated into a build system which lets
you build everything into proper disk images at a moment's notice.

What you get is a working CP/M 2.2 clone consisting of:

  - ZSDOS as the BDOS
  - ZCPR1 as the CCP
  - open source BIOSes for the supported platforms
  - various Digital Research programs from the original CP/M (I'm slowly
    importing them and integrating them into the build system)
  - various tools copying the functionality of the standard CP/M tools (some
    of them [written by me](http://cowlark.com/2019-06-01-cpm-asm)
  - [R.T. Russell's superb BBC Basic](http://www.bbcbasic.co.uk/bbcbasic.html),
    Z80 edition (with integrated assembler)
  - Richard Surwilo's Z8E full-screen symbolic debugger
  - B. J. Rodriguez's CamelForth
  - a build system which provides a turnkey cross-compilation system for
    producing bootable disk images for any of the supported platforms
  - a classic CP/M syntax assembler and linker for cross-compiling ancient
    source
  - a simple but useful vi-adjacent editor called qe (written by myself)
  - an emulator for testing CP/M binaries
  - source for _everything_; no binaries are in this distribution
  - other things which I may well have forgotten to document
  - bugs

Currently it supports these platforms:

  - [the Amstrad NC200 laptop](arch/nc200/README.md)
  - [the Kaypro II](arch/kayproii/README.md)
  - [the Brother WP-1 typewriter (and probably others)](arch/brother/wp1/README.md)
  - [the Brother LW-30 typewriter (and probably others)](arch/brother/lw30/README.md)
  - [the Brother WP-2450DS typewriter (and probably others)](arch/brother/wp2450/README.md)
  - [the Brother PN-8510MDS SuperPowerNote laptop (and probably others)](arch/brother/pn8510/README.md)
  - [the Brother PN-8800FXB SuperPowerNote laptop (and probably others)](arch/brother/pn8800/README.md)
  - [the nano-z80 SoC for the Tang Nano 20k FPGA board](arch/nano-z80/README.md)

(Some of these are pretty stale due to difficulty of testing and may not work.
Later entries are newer! If you have any problems, please report bugs.)

If anyone wants to contribute any more BIOSes, I'd love pull requests!


Why?
----

CP/M is Digital Research's seminal desktop operating system from 1977 that
for a decade dominated the personal computer market. It's of enormous
historical value and there's a vast wealth of programs written for it. It's
even useful today: both to study (as aa superb example of sheer minimalism)
but also to use; the Z80 is a common target for homebrew computers, and CP/M
is the obvious operating system to run on one.

Don't believe me? Watch this:

[![Video of me doing stuff on an NC200](http://img.youtube.com/vi/FGWshrMZcCc/0.jpg)](https://www.youtube.com/watch?v=FGWshrMZcCc)

The source and binaries have long been available via the (the amazing)
[Unofficial CP/M Web Site](http://www.gaby.de/cpm/), but the license had a bug
in it which meant they couldn't be distributed anywhere else; this was
[recently fixed](third_party/dr/COPYING.md) so it's now properly open source.


How?
----

**From binaries:** precompiled disk images are available [as part of the current
development release](https://github.com/davidgiven/cpmish/releases/tag/dev).
This are built automatically and aren't tested in any way.

**From source:** you pretty much need a Unix --- I developed it on Linux. You'll
need to install the dependencies. These are the names of the Debian packages:

  - cpmtools
  - libz80ex-dev
  - libreadline-dev

You _also_ need to install [the Amsterdam Compiler
Kit](https://github.com/davidgiven/ack), which is used as the C compiler
(yes, some of the tools are written in C). You'll have to install it from
source yourself as it's not in Debian.

Once in place, just do:

    make

...and it should build. You'll end up with some `.img` files in the project
directory which are the bootable disk images.

If you want more detailed build instructions, try [the script used for
automatic
builds](https://github.com/davidgiven/cpmish/blob/master/.github/workflows/ccpp.yml),
which has got the exact commands needed buried inside it. This also has the
instructions for OSX.

For information on what to do with these, look in the READMEs in the
individual [`arch/*`](https://github.com/davidgiven/cpmish/tree/master/arch)
directories.


Where?
------

- [Check out the GitHub repository](http://github.com/davidgiven/cpmish) and
build from source. (Alternatively, you can download a source snapshot from
[the latest release](https://github.com/davidgiven/cpmish/releases/latest),
but I suggect the GitHub repositories better because I don't really intend to
make formal releases often.) Build instructions as in the README.

- [Ask a question by creating a GitHub
issue](https://github.com/davidgiven/cpmish/issues/new), or just email me
directly at [dg@cowlark.com](mailto:dg@cowlark.com). (But I'd prefer you
opened an issue, so other people can see them.)


Who?
----

There's a lot of stuff here, and while I assembled it, I didn't write all of
it. See the licensing section below for the full list.

For the distribution work and the bits I did write --- I am David Given. Feel
free to send me email at [dg@cowlark.com](mailto:dg@cowlark.com). You may
also [like to visit my website](http://cowlark.com); there may or may not be
something interesting there.


License?
--------

This is a big aggregation of software, all with its own licensing. It contains
GPLv2-licensed code, so as a whole it must be distributed under the terms of
the GPL version 2 (because complying with the GPL also complies with the
license of everything else). See the `COPYING.gpl2` file for more details.

Specifically:

  - Everything _not_ in `arch` or `third_party` is © 2018-2019 David Given and
	is distributable under the terms of the 2-clause BSD license. See the
	`COPYING.cpmish` file for more details.

  - `arch/nc200` and `arch/kayproii` were written by me and are covered by the
	main CP/Mish license.

  - `third_party/bbcbasic` contains a copy of R.T.Russell's Z80 BBC Basic,
	which is distributable under the terms of the zlib license. See the
	`third_party/bbcbasic/COPYING` file for more details.

  - `third_party/libstb` contains a copy of Sean Barrett's stb library, which
	is partially in the public domain and partially distributable under the
	Expat license. See the `third_party/libstb/COPYING` file for more details.

  - `third_party/zcpr1` contains a (modified) copy of the ZCPR1 CCP
	replacement, written by the CCP-GROUP, which is in the public domain. See
	the `third_party/zcpr1/COPYING` file for more details.

  - `third_party/zmac` contains a (modified) copy of the ZMAC macro assembler,
	written by George Phillips, Thierry Join, Mark Rison, Russell Marks, Colin
	Kelley, John Providenza and Bruce Norskog (some time in 1978!) --- and
	probably others. To the best of my knowledge this is in the public domain.
	See the `third_party/zmac/COPYING` file for more details.

  - `third_party/ld80` contains a (modified) copy of the LD80 macro assembler,
	written by (as far as I know) George Philips and Gabor Kiss. It is in the
	public domain.

  - `third_party/zsdos` contains a (modified) copy of the ZSDOS CP/M BDOS
	clone, written by lots of people but mainly Cameron W. Cotrill and Harold
	F. Bower. This is available under the terms of the General Public License
	version 2. See the `third_party/zsdos/COPYING` file for more details.

  - `third_party/z8e` contains a (modified) copy of the Z8E symbolic
    debugger, mostly written by Richard Surwilo and Jon Saxton. It is in the
	public domain.

  - `third_party/libz80ex` contains a copy of the libz80ex Z80 emulation
	library, mostly written by Pigmaker57. It is distributable under the terms
	of the General Public license version 2. See the
	`third_party/libz80ex/COPYING` file for the full text.

  - `third_party/camelforth` contains a copy of CamelForth for the Z80, written
	by B. J. Rodriguez. It is distributable under the terms of the General
	Public License version 3. See `third_party/camelforth/COPYING` for the full
	text.

  - `third_party/dr` contains a variety of software, all by Digital Research.
	It is distributable under a rather complicated license which kind of
	accreted over the years but is mostly a do-what-thou-wilt license
	equivalent to 2-clause BSD. See `third_party/dr/COPYING.md` for more
	information.

