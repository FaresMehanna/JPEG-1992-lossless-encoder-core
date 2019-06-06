import sys
from math import log, ceil
import struct, random 


if __name__ == "__main__":

	new_bin = []

	for i in range(int(4096*10*1.5)):
		new_bin.append(random.randint(0, 255))

	with open(sys.argv[1], "wb") as f:
		f.write(bytes(new_bin))