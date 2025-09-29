from third_party.zmac.build import zmac

zmac(
    name="baudrate",
    relocatable=False,
    src="./baudrate.z80",
    deps=[
        "arch/nano-z80+addresses",
    ],
)

