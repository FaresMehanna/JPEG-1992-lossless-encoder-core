#include "core_axi_lite.h"

using namespace std;

CoreAXILite::CoreAXILite(uint32_t base_addr, uint8_t bit_depth)
: m_handler()
{
    assert_term(2 <= bit_depth && 16 >= bit_depth, "CoreAXILite1");
    this->bit_depth = bit_depth;
    mem = (uint32_t*) m_handler.mmap(base_addr, 65535);
}

CoreAXILite::~CoreAXILite()
{
}

uint16_t CoreAXILite::get_height()
{
    uint32_t mask = pow(2, 16) - 1;
    return __get(HW_OFFSET) & mask;
}

uint16_t CoreAXILite::get_width()
{
    return __get(HW_OFFSET) >> 16;
}

uint32_t CoreAXILite::get_allowed_cycles()
{
    return __get(HW_OFFSET + 1);
}

vector<string> CoreAXILite::get_ssss()
{
    // get ssss codes from axi lite
    vector<uint64_t> ssss_codes;
    uint64_t code = 0;
    for(int i=0; i<2*bit_depth; i++){
        if(i%2==0){
            code = __get(SSSS_OFFSET+i);
        } else {
            code = (((uint64_t)__get(SSSS_OFFSET+i)) << 32) | code;
            ssss_codes.push_back(code);
        }
    }
    // get ssss info form them
    vector<string> ssss;
    for(int i=0; i<bit_depth; i++) {
        uint32_t code_length = (ssss_codes[i] >> (16+bit_depth));
        uint32_t mask = pow(2, code_length) - 1;
        uint32_t ssss_code = 0;
        if (i == 16) {
            ssss_code = (ssss_codes[i] & mask);
        } else {
            ssss_code = ((ssss_codes[i] >> i) & mask);
        }
        ssss.push_back(to_string(i) + " - " + "SSSS_CODE: " + to_string(ssss_code) + " - " + "LENGTH: " + to_string(code_length));
    }
    return ssss;
}

vector<string> CoreAXILite::get_debug()
{
    vector<string> ident {"valid_in=0","valid_in=1",
                          "valid_out=0","valid_out=1",
                          "nready=1","nready=0",
                          "busy_in=1","busy_in=0"};
    vector<string> explain {"valid_in: DMA have valid data for the core",
                            "valid_out: Core have valid data for the DMA",
                            "nready: Core don't have valid data for the DMA",
                            "busy_in: DMA can't accept new data from the core"};
    vector<uint32_t> debug_regs;
    for(int i=0; i<8; i++) {
        debug_regs.push_back(__get(DEBUG_OFFSET + i));
    }
    vector<string> debug_vals;
    for(int i=0; i<8; i++) {
        debug_vals.push_back(ident[i] + " : " + to_string(debug_regs[i]));
    }
    vector<string> debug_data;
    debug_data.insert(debug_data.end(), explain.begin(), explain.end());
    debug_data.insert(debug_data.end(), debug_vals.begin(), debug_vals.end());
    return debug_data;
}

void CoreAXILite::set_height(uint16_t nheight)
{
    uint16_t width = get_width();
    __set(HW_OFFSET, ((((uint32_t)width)<<16)|(nheight)));
}

void CoreAXILite::set_width(uint16_t nwidth)
{
    uint16_t height = get_height();
    __set(HW_OFFSET, ((((uint32_t)nwidth)<<16)|(height)));
}

void CoreAXILite::set_allowed_cycles(uint32_t nallowed_cycles)
{
    __set(HW_OFFSET + 1, nallowed_cycles);
}

void CoreAXILite::__set(uint32_t offset, uint32_t value)
{
    mem[offset] = value;
}

uint32_t CoreAXILite::__get(uint32_t offset)
{
    return mem[offset];
}