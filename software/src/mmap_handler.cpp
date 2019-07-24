#include "mmap_handler.h"

MMapHandler::MMapHandler()
{
    mem_fp = open("/dev/mem", O_RDWR | O_SYNC);
    assert_term(-1 != mem_fp, "MMapHandler-open");
}

MMapHandler::~MMapHandler()
{
	close(mem_fp);
}

void* MMapHandler::mmap(uint32_t base, uint32_t length)
{
    void* v_addr = ::mmap(NULL, length, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fp, base);
    assert_term(MAP_FAILED != v_addr, "MMapHandler-mmap");
    return v_addr;
}