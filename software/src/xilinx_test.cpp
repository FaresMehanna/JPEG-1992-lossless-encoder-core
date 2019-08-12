#include "tools.h"
#include "core_axi_lite.h"
#include "mmap_handler.h"
#include "xilinx_dma.h"
#include "config.h"

#include <time.h>
#include <math.h>

#include <algorithm>

using namespace std;

void re_order_set_raw12_64bits(volatile void* v_src_addr, struct mem_data raw12);
void re_order_set_raw12_32bits(volatile void* v_src_addr, struct mem_data raw12);
void re_order_lj92(struct mem_data lj92);
void zero_dest(volatile void* v_dest_addr);
uint32_t divisible_2(uint32_t num);
uint32_t divisible_4(uint32_t num);
void check_first_marker(volatile void* v_dest_addr);
void check_last_marker(volatile void* v_dest_addr, uint32_t size);
void validate(volatile void* v_dest_addr, struct mem_data lj92);
void print_vector(vector<string> vec, string title);

// timer
timespec t;
void get_time();
void initiate_timer();
double diff(timespec start, timespec end);

int main(int argc, char** argv)
{    
    // initializing timer
    initiate_timer();

    log("asserting argc&argv.");
    assert_term(3 == argc, "You must provide source image and compressed image as parameters.");
    
    MMapHandler m_handler;
    XilinxDMA xi_dma(DMA_BASE);

    log("MMap source & destination memories.");
    volatile void* v_src_addr = m_handler.mmap(SOURCE_BASE, 0x2000000);
    volatile void* v_dest_addr = m_handler.mmap(DEST_BASE, 0x2000000);
    get_time();

    log("Load LJ92 img.");
    struct mem_data lj92 = load_file(argv[2]);
    log("LJ92 size: " + to_string(lj92.length));
    get_time();

    log("Load Raw12 img.");
    struct mem_data raw12 = load_file(argv[1]);
    assert_term(raw12.length >= 4096*3072*1.5, "Corrupted RAW12 file.");
    log("Raw12 size: " + to_string(raw12.length));
    get_time();

    log("Re-order and set Raw12 into MMaped region.");
    if (INPUT_LENGTH == 64)
        re_order_set_raw12_64bits(v_src_addr, raw12);
    else
        re_order_set_raw12_32bits(v_src_addr, raw12);
    get_time();

    log("Remove Raw12 img form memory.");
    clear_mem_data(raw12);
    get_time();

    log("Re-order compressed LJ92 img.");
    re_order_lj92(lj92);
    get_time();

    log("Zero out the MMaped destination region.");
    zero_dest(v_dest_addr);
    get_time();

    if(AXI_LITE_ENABLE)
    {
        log("AXI Lite is enabled.");
        log("Set height and width.");
        CoreAXILite c_axi(AXI_LITE_BASE, CORE_BIT_DEPTH);
        c_axi.set_width(4096);
        c_axi.set_height(3072);
        log("width: " + to_string(c_axi.get_width()));
        log("height: " + to_string(c_axi.get_height()));
        get_time();

        log("Set allowed cycles.");
        c_axi.set_allowed_cycles(0xFFFFFF);
        log("allowed_cycles: " + to_string(c_axi.get_allowed_cycles()));
        get_time();

        print_vector(c_axi.get_ssss(), "SSSS Data.");
        get_time();

    } 
    else
    {
        log("AXI Lite is not enabled.");
        log("skip setting height, width and allowed cycles.");
        get_time();
    }

    log("Reset DMA.");
    xi_dma.reset_dma();
    print_vector(xi_dma.dma_s2mm_status(), "dma_s2mm_status");
    print_vector(xi_dma.dma_mm2s_status(), "dma_mm2s_status");

    log("Halt DMA.");
    xi_dma.halt_dma();
    print_vector(xi_dma.dma_s2mm_status(), "dma_s2mm_status");
    print_vector(xi_dma.dma_mm2s_status(), "dma_mm2s_status");

    log("Writing src & dest addresses.");
    xi_dma.set_dma_src_dist(SOURCE_BASE, DEST_BASE);

    log("Starting DMA.");
    xi_dma.start_dma();

    log("Writing transfer lengths.");
    xi_dma.set_dma_transfer_len(divisible_4(lj92.length+1024), (4096*3072*2));
    get_time();

    log("Waiting for MM2S synchronization.");
    xi_dma.dma_mm2s_sync();

    log("Waiting for S2MM synchronization.");
    xi_dma.dma_s2mm_sync();

    log("LJ92 done.");
    print_vector(xi_dma.dma_s2mm_status(), "dma_s2mm_status");
    print_vector(xi_dma.dma_mm2s_status(), "dma_mm2s_status");
    get_time();

    log("Dump first 256Bytes of LJ92 file.");
    mem_dump(lj92.pointer, 256);

    log("Dump first 256Bytes of core.");
    mem_dump(v_dest_addr, 256);

    log("Dump last 256Bytes of LJ92 file.");
    mem_dump((char*)lj92.pointer+lj92.length-256, 256);

    log("Dump last 256Bytes of core.");
    mem_dump((char*)v_dest_addr+lj92.length-256+16, 256);

    get_time();

    log("Check for first marker.");
    check_first_marker(v_dest_addr);

    log("Check for last marker.");
    check_last_marker(v_dest_addr, lj92.length);

    get_time();

    log("Validate data.");
    validate(v_dest_addr, lj92);
    get_time();

    if(AXI_LITE_ENABLE & DEBUG_REG_ENABLE){
        CoreAXILite c_axi(AXI_LITE_BASE, CORE_BIT_DEPTH);
        print_vector(c_axi.get_debug(), "Debugging data.");
    }
}

void re_order_set_raw12_64bits(volatile void* v_src_addr, struct mem_data raw12)
{
    int counter8 = 0, counter64 = 0;
    
    volatile uint8_t* base = (uint8_t*) raw12.pointer;
    volatile uint64_t* base64 = (uint64_t*) v_src_addr;

    for(int i=0; i<(4096*3072); i+=4)
    {
        uint64_t p1 = base[counter8]<<4 | (base[counter8+1] & 0xF0)>>4;
        uint64_t p2 = (base[counter8+1] & 0x0F)<<8 | base[counter8+2];
        counter8 += 3;

        uint64_t p3 = base[counter8]<<4 | (base[counter8+1] & 0xF0)>>4;
        uint64_t p4 = (base[counter8+1] & 0x0F)<<8 | base[counter8+2];
        counter8 += 3;

        uint64_t pixs4 = (p1 << 52) | (p2 << 40) | (p3 << 28) | (p4 << 16);

        base64[counter64++] = pixs4;
    }
}

void re_order_set_raw12_32bits(volatile void* v_src_addr, struct mem_data raw12)
{
    int counter8 = 0, counter32 = 0;
    
    volatile uint8_t* base = (uint8_t*) raw12.pointer;
    volatile uint32_t* base32 = (uint32_t*) v_src_addr;

    for(int i=0; i<(4096*3072); i+=2)
    {
        uint32_t p1 = base[counter8]<<4 | (base[counter8+1] & 0xF0)>>4;
        uint32_t p2 = (base[counter8+1] & 0x0F)<<8 | base[counter8+2];
        counter8 += 3;

        uint32_t pixs2 = (p1 << 20) | (p2 << 8);

        base32[counter32++] = pixs2;
    }
}

void re_order_lj92(struct mem_data lj92)
{
    volatile uint16_t* compressed_img_16 = (uint16_t*) lj92.pointer;
    uint32_t len2 = divisible_2(lj92.length);
    for(int i=0; i<len2; i+= 2) {
        compressed_img_16[i/2] = __builtin_bswap16(compressed_img_16[i/2]);
    }
}

void zero_dest(volatile void* v_dest_addr)
{
    volatile uint32_t* v_dest_addr32 = (uint32_t*) v_dest_addr;
    for(int i=0; i<0x800000; i++) { 
        v_dest_addr32[i] = 0;   
    }
}

uint32_t divisible_4(uint32_t num)
{
    while(num % 4 != 0) {
        num++;
    }
    return num;
}

uint32_t divisible_2(uint32_t num)
{
    while(num % 2 != 0) {
        num++;
    }
    return num;
}

void check_first_marker(volatile void* v_dest_addr)
{
    bool found = true;
    for(int i=0; i<4; i++) {
        if(((uint32_t*)v_dest_addr)[i] != 0xFFFFFFFF) {
            log("No marker found.");
            found = false;
            break;
        }
    }
    if(found){
        log("marker found.");
    }
}

void check_last_marker(volatile void* v_dest_addr, uint32_t size)
{
    uint32_t offset = size + 16;
    for(int i=0; i<128; i++) {
        if(*((uint32_t*)(((uint8_t*)v_dest_addr) + offset)) == 0xFFFFFFFF ||
           *((uint32_t*)(((uint8_t*)v_dest_addr) + offset)) == __builtin_bswap32(0xFFFEFFFE)) {
            break;
        }
        offset++;
    }
    volatile uint32_t* start_addr = (uint32_t*)(((uint8_t*)v_dest_addr) + offset);
    bool found = true;
    for(int i=0; i<4; i++) {
        if(start_addr[i] != 0xFFFFFFFF &&
           start_addr[i] != __builtin_bswap32(0xFFFEFFFE)) {
            log("No marker found.");
            found = false;
            break;
        }
    }
    if(found){
        if(start_addr[0] == 0xFFFFFFFF)
            log("normal marker found - offset is " + to_string((offset-size-16)) + ".");
        if(start_addr[0] == __builtin_bswap32(0xFFFEFFFE))
            log("force marker found - offset is " + to_string((offset-size-16)) + ".");
    }
}

void validate(volatile void* v_dest_addr, struct mem_data lj92_struct)
{
    bool failed = false;

    volatile uint32_t* core = (uint32_t*)(((uint8_t*)v_dest_addr) + 16);
    volatile uint32_t* lj92 = (uint32_t*)((uint8_t*)lj92_struct.pointer);
    for(int i=0; i<(lj92_struct.length/4); i++) {
        if(core[i] != lj92[i]) {
            log("Validation failed at word: " + to_string(i));

            log("Dump core");
            mem_dump(core+max(i-8, 0), 64);
            log("Dump lj92");
            mem_dump(lj92+max(i-8, 0), 64);

            failed = true;
            break;
        }
    }

    if(!failed) {
        volatile uint8_t* core_8 = ((uint8_t*)v_dest_addr) + 16;
        volatile uint8_t* lj92_8 = (uint8_t*)lj92_struct.pointer;
        for(int i=lj92_struct.length-10; i<lj92_struct.length; i++) {
            if(core_8[i] != lj92_8[i]) {
                log("Validation failed at byte: " + to_string(i));

                log("Dump core");
                mem_dump(core_8+max(i-32, 0), 64);
                log("Dump lj92");
                mem_dump(lj92_8+max(i-32, 0), 64);

                failed = true;
                break;
            }
        }
    }

    if(!failed) {
        log("Validation succeeded.");
    }
}

void print_vector(vector<string> vec, string title)
{
    cout << title << endl;
    for(int i=0; i<vec.size(); i++) {
        cout << vec[i] << endl;
    }
}

void initiate_timer()
{
    clock_gettime(CLOCK_MONOTONIC, &t);
}

void get_time()
{
    timespec t_now;
    clock_gettime(CLOCK_MONOTONIC, &t_now);
    printf("Operation toke %.3lfms.\n\n", diff(t, t_now));
    clock_gettime(CLOCK_MONOTONIC, &t);
}

double diff(timespec start, timespec end)
{
    double temp = 0;
    if ((end.tv_nsec-start.tv_nsec)<0) {
        temp += (end.tv_sec-start.tv_sec-1)*1000;
        temp += (1000000000+end.tv_nsec-start.tv_nsec)/1000000.0;
    } else {
        temp += (end.tv_sec-start.tv_sec)*1000;
        temp += (end.tv_nsec-start.tv_nsec)/1000000.0;
    }
    return temp;
}
