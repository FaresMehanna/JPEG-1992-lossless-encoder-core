#ifndef SRC_CORE_AXI_LITE_H__
#define SRC_CORE_AXI_LITE_H__

//Declare class
class CoreAXILite;

#define SSSS_OFFSET  (0x400)
#define HW_OFFSET    (0x800)
#define DEBUG_OFFSET (0x1000)

#include <sys/mman.h>

#include <unistd.h>
#include <stdint.h>
#include <math.h>

#include <vector>
#include <string>

#include "tools.h"
#include "mmap_handler.h"

using namespace std;

class CoreAXILite
{

private:

    MMapHandler m_handler;
    volatile uint32_t* mem;
    uint8_t bit_depth;

    void __set(uint32_t offset, uint32_t value);
    uint32_t __get(uint32_t offset);

public:

    CoreAXILite(uint32_t base_addr, uint8_t bit_depth);
    ~CoreAXILite();

    uint16_t get_height();
    uint16_t get_width();

    uint32_t get_allowed_cycles();

    vector<string> get_ssss();
    vector<string> get_debug();

    void set_height(uint16_t nheight);
    void set_width(uint16_t nwidth);

    void set_allowed_cycles(uint32_t nallowed_cycles);
};

#endif