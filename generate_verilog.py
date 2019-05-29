from os import system, stat, remove
import glob
import ntpath

if __name__ == "__main__":
	# generate verilog files
	src_files = [f for f in glob.glob("./migen_src/*.py")]
	for src_file in src_files:
		system("python " + src_file + " generate > ./verilog_src/" + ntpath.basename(src_file)[:-3] + ".v")

	#remove empty files
	v_files = [f for f in glob.glob("./verilog_src/*.v")]
	for v_file in v_files:
		if stat(v_file).st_size == 0:
			remove(v_file)
