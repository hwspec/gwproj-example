from math import gcd

import cocotb

from gcd_bridge import GcdBridge

# keep in sync with AxiGCDSpec.scala's testVectors
TEST_VECTORS = [
    (48, 18),
    (18, 48),
    (1071, 462),
    (17, 5),
    (0, 42),
    (42, 0),
    (7, 7),
    (0, 0),
]


async def run_gcd(dut, value1, value2):
    await dut.writeWord(dut.p.value1_rw, value1)
    await dut.writeWord(dut.p.value2_rw, value2)  # kicks off the computation

    valid = 0
    tries = 0
    while valid == 0 and tries < 1000:
        valid = await dut.readWord(dut.p.valid_r)
        tries += 1
    assert valid == 1, f"AxiGCD did not finish in time for ({value1}, {value2})"

    expected = gcd(value1, value2)
    await dut.expectWord(dut.p.result_r, expected, msg=f"gcd({value1}, {value2})")

    cycles = await dut.readWord(dut.p.gcd_cycles_r)
    dut.log.info(f"gcd({value1}, {value2}) = {expected}, took {cycles} cycles")


@cocotb.test()
async def tb_base(cocotb_dut):
    dut = GcdBridge(cocotb_dut)
    await dut.setup()

    await dut.expectWord(dut.p.const1_r, dut.p.const1)
    await dut.expectWord(dut.p.const2_r, dut.p.const2)

    for value1, value2 in TEST_VECTORS:
        await run_gcd(dut, value1, value2)

    await dut.softReset()
    await dut.expectWord(dut.p.valid_r, 0)

    dut.log.info("Verified!")
