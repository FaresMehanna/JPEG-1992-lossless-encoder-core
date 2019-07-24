#include "tools.h"

using namespace std;

void log(string msg)
{
    cout << msg << endl;
}

void assert_term(bool cond, string msg)
{
    if(!cond) {
        log("Error & Terminating - " + msg);
        exit(EXIT_FAILURE);
    }
}


void mem_dump(volatile void* arr, uint32_t length)
{
    volatile char *p = (char*)arr;
    int offset;
    for (offset = 0; offset < length; offset++) {
        printf("%02x", p[offset]);
        if (offset % 4 == 3) { printf(" "); }
    }
    printf("\n");
}

struct mem_data load_file(string file_path)
{
    struct stat info;
    assert_term(stat(file_path.c_str(), &info) == 0, "load_file-stat");
    int size = info.st_size;
    assert_term(size > 0, "load_file-size_test");
    FILE* fp = fopen(file_path.c_str(), "rb");
    assert_term(NULL != fp, "load_file-fopen");
    void* file_data = malloc(size + 128);
    assert_term(NULL != file_data, "load_file-malloc");
    assert_term(fread(file_data, size, 1, fp) == 1, "load_file-fread");
    fclose(fp);
    memset((char*)file_data + size, 0, 128);
    struct mem_data data(file_data, size);
    return data;
}

void clear_mem_data(mem_data data)
{
    if(data.pointer != NULL) {
        free(data.pointer);
        data.pointer = NULL;
        data.length = 0;
    }
}