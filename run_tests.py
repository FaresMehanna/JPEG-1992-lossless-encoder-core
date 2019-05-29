from os import system
import glob

if __name__ == "__main__":
	test_files = [f for f in glob.glob("./migen_src/tests/*.py")]
	for test_file in test_files:
		system("python " + test_file)