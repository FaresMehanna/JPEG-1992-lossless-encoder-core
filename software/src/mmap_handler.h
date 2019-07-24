#ifndef SRC_MMAP_HANDLER_H__
#define SRC_MMAP_HANDLER_H__

//Declare class
class MMapHandler;

#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>

#include <unistd.h>
#include <stdint.h>

#include "tools.h"

class MMapHandler{
private:
    int mem_fp;
public:
	MMapHandler();
	~MMapHandler();
	void* mmap(uint32_t base, uint32_t length);
};

#endif