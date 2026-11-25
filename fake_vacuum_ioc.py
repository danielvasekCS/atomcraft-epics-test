import asyncio
import random

from caproto.server import (
    PVGroup,
    pvproperty,
    ioc_arg_parser,
    run
)


class VacuumIOC(PVGroup):

    pressure = pvproperty(
        value=1e-6,
        name="PRESSURE"
    )

    status = pvproperty(
        value="OK",
        name="STATUS"
    )

    valve_open = pvproperty(
        value=0,
        name="VALVE_OPEN"
    )

    @pressure.startup
    async def pressure(self, instance, async_lib):
        while True:
            fake_pressure = random.uniform(1e-6, 5e-6)

            await instance.write(fake_pressure)

            await async_lib.library.sleep(1)


if __name__ == "__main__":

    ioc_options, run_options = ioc_arg_parser(
        default_prefix="ATOMCRAFT:VACUUM:",
        desc="Fake AtomCraft vacuum IOC"
    )

    ioc = VacuumIOC(**ioc_options)

    run(
        ioc.pvdb,
        **run_options
    )

