import sys
from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import struct


if __name__ == "__main__":

	org_bin = []

	with open(sys.argv[1], "rb") as f:
		byte = f.read(1)
		for i in range (int(sys.argv[2])):
			un = int.from_bytes(byte, byteorder='big')
			org_bin.append(un)
			byte = f.read(1)

	with open(sys.argv[1], "wb") as f:
		f.write(bytes(org_bin))