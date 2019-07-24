#include "xilinx_dma.h"

using namespace std;

XilinxDMA::XilinxDMA(uint32_t base_addr)
: m_handler()
{
    mem = (uint32_t*) m_handler.mmap(base_addr, 65535);
}

XilinxDMA::~XilinxDMA()
{
}

vector<string> XilinxDMA::dma_s2mm_status()
{
    return __dma_status(S2MM_STATUS_REGISTER);
}

vector<string> XilinxDMA::dma_mm2s_status()
{
    return __dma_status(MM2S_STATUS_REGISTER);
}

void XilinxDMA::dma_mm2s_sync()
{
    __dma_sync(MM2S_STATUS_REGISTER);
}

void XilinxDMA::dma_s2mm_sync()
{
    __dma_sync(S2MM_STATUS_REGISTER);
}

void XilinxDMA::reset_dma()
{
    __dma_set(S2MM_CONTROL_REGISTER, 4);
    __dma_set(MM2S_CONTROL_REGISTER, 4);
}

void XilinxDMA::halt_dma()
{
    __dma_set(S2MM_CONTROL_REGISTER, 0);
    __dma_set(MM2S_CONTROL_REGISTER, 0);
}

void XilinxDMA::set_dma_src_dist(uint32_t src, uint32_t dist)
{
    __dma_set(S2MM_DESTINATION_ADDRESS, dist);
    __dma_set(MM2S_START_ADDRESS, src);
}

void XilinxDMA::start_dma()
{
    __dma_set(S2MM_CONTROL_REGISTER, 0xf001);
    __dma_set(MM2S_CONTROL_REGISTER, 0xf001);
}

void XilinxDMA::set_dma_transfer_len(uint32_t s2mm_len, uint32_t mm2s_len)
{
    __dma_set(S2MM_LENGTH, s2mm_len);
    __dma_set(MM2S_LENGTH, mm2s_len);
}

void XilinxDMA::__dma_sync(uint32_t status_register)
{
    uint32_t s2mm_status = __dma_get(status_register);
    while(!(s2mm_status & 1<<12) || !(s2mm_status & 1<<1)){
        usleep(100);
        s2mm_status = __dma_get(status_register);
    }
}

vector<string> XilinxDMA::__dma_status(uint32_t status_register)
{
    vector<string> data;
    uint32_t status = __dma_get(status_register);

    if (status & 0x00000001)
        data.push_back("halted");
    else
        data.push_back("running");
    if (status & 0x00000002)
        data.push_back("idle");
    if (status & 0x00000008)
        data.push_back("SGIncld");
    if (status & 0x00000010)
        data.push_back("DMAIntErr");
    if (status & 0x00000020)
        data.push_back("DMASlvErr");
    if (status & 0x00000040)
        data.push_back("DMADecErr");
    if (status & 0x00000100)
        data.push_back("SGIntErr");
    if (status & 0x00000200)
        data.push_back("SGSlvErr");
    if (status & 0x00000400)
        data.push_back("SGDecErr");
    if (status & 0x00001000)
        data.push_back("IOC_Irq");
    if (status & 0x00002000)
        data.push_back("Dly_Irq");
    if (status & 0x00004000) 
        data.push_back("Err_Irq");
    return data;
}

void XilinxDMA::__dma_set(uint32_t offset, uint32_t value)
{
    mem[offset>>2] = value;
}

uint32_t XilinxDMA::__dma_get(uint32_t offset)
{
    return mem[offset>>2];
}