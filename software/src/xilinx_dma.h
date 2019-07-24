#ifndef SRC_XILINX_DMA_H__
#define SRC_XILINX_DMA_H__

//Declare class
class XilinxDMA;

#define MM2S_CONTROL_REGISTER    (0x00)
#define MM2S_STATUS_REGISTER     (0x04)
#define MM2S_START_ADDRESS       (0x18)
#define MM2S_LENGTH              (0x28)

#define S2MM_CONTROL_REGISTER    (0x30)
#define S2MM_STATUS_REGISTER     (0x34)
#define S2MM_DESTINATION_ADDRESS (0x48)
#define S2MM_LENGTH              (0x58)

#include <unistd.h>
#include <stdint.h>

#include <vector>
#include <string>

#include "tools.h"
#include "mmap_handler.h"

using namespace std;

class XilinxDMA
{

private:

    MMapHandler m_handler;
    volatile uint32_t* mem;

    void __dma_sync(uint32_t status_register);
    vector<string> __dma_status(uint32_t status_register);

    void __dma_set(uint32_t offset, uint32_t value);
    uint32_t __dma_get(uint32_t offset);

public:

    XilinxDMA(uint32_t base_addr);
    ~XilinxDMA();

    vector<string> dma_s2mm_status();
    vector<string> dma_mm2s_status();

    void dma_mm2s_sync();
    void dma_s2mm_sync();

    void reset_dma();

    void halt_dma();

    void set_dma_src_dist(uint32_t src, uint32_t dist);

    void start_dma();

    void set_dma_transfer_len(uint32_t s2mm_len, uint32_t mm2s_len);
};

#endif