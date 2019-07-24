#ifndef SRC_TOOLS_H__
#define SRC_TOOLS_H__

#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/stat.h>

#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct mem_data{
	void* pointer = NULL;
	uint32_t length = 0;
	mem_data(void* pointer_, uint32_t length_) {
		pointer = pointer_;
		length = length_;
	}
};

void log(string msg);
void assert_term(bool cond, string msg);
void mem_dump(volatile void* arr, uint32_t length);
struct mem_data load_file(string file_path);
void clear_mem_data(mem_data data);

#endif