#
# gwscript-generated settings for Makefile.gw
#
HWMODULENAME=AxiGCD
BRIDGEBN=target_bridge
TOPNAME=wrapper
SRCDIR = $(abspath ../generated/$(HWMODULENAME))

# Add more cocotb test target names here (matching your tb_<name>.py files)
TARGETS = base

.DEFAULT_GOAL := base

SCALA_SRCS := $(shell find ../src -name '*.scala') ../build.sbt
GENCMD = (cd .. ; sbt "runMain axigcd.AxiGCD")
