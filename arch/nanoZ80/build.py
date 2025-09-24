from build.ab import simplerule
from build.cpm import diskimage
from utils.build import unix2cpm
from third_party.zmac.build import zmac
from third_party.ld80.build import ld80


zmac(name="boot", src="./boot.z80", relocatable=False)

zmac(
    name="bios",
    src="./bios.z80",
    deps=[
        "arch/nanoZ80/include/nanoZ80.lib",
        "include/cpm.lib",
        "include/cpmish.lib",
    ],
)

# Builds the memory image.
ld80(
    name="bootfile_mem",
    objs={
        0xE400: ["third_party/zcpr1"],
        0xEC00: ["third_party/zsdos"],
        0xFA00: [".+bios"],
    },
)

# Repackages the memory image as a boot track. This doesn't include the extra
# section of boot image which exists above the directory.
simplerule(
    name="bootfile",
    ins=[".+boot", ".+bootfile_mem"],
    outs=["=bootfile.img"],
    commands=[
        "dd if={ins[0]} of={outs[0]} bs=128 count=1 2> /dev/null",
        "dd if={ins[1]} of={outs[0]} bs=128 seek=4 skip=454 count=56 2> /dev/null",
    ],
    label="nanoZ80",
)

unix2cpm(name="readme", src="README.md")

diskimage(
    name="diskimage",
    format="generic-1m",
    bootfile=".+bootfile",
    map={
        "-readme.txt": ".+readme",
        "dump.com": "cpmtools+dump",
        "stat.com": "cpmtools+stat",
        "asm.com": "cpmtools+asm",
        "copy.com": "cpmtools+copy",
        "submit.com": "cpmtools+submit",
        "bbcbasic.com": "third_party/bbcbasic+bbcbasic_ADM3A",
        "camel80.com": "third_party/camelforth",
        "qe.com": "cpmtools+qe_SPECTRUM_NEXT",
    },
)

