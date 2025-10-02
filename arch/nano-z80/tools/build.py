from third_party.zmac.build import zmac
from build.ack import ackprogram

zmac(
    name="baudrate",
    relocatable=False,
    src="./baudrate.z80",
    deps=[
        "arch/nano-z80+addresses",
    ],
)

ackprogram(
    name="nanoterm",
    srcs=["./nanoterm.c", "./uart.s"],
)
