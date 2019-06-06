# Test files

## portrait-gainx2-offset2047-20ms-01.raw12:
- IMG: Width  -> 4096
- IMG: Height -> 10
- LJ92: Huffman used to compress -> {0b1110, 0b000,0b001,0b010,0b011,0b100,0b101,0b110,0b11110,0b111110,0b1111110,0b11111110,0b111111110,0b1111111110,0b11111111110,0b111111111110,0b1111111111110}
- LJ92: 4 components.
- LJ92: predictor 1 is used.
- LJ92: normal height and width.
- LJ92: compression ratio: 0.556120.
- LJ92: pixel size: 6.673438 bits.
- LJ92: SSSS analyses ->
```
  31.17%   |                            |                                                                          
  28.05%   |                            |                                                                          
  24.94%   |                            |     |                                                                    
  21.82%   |                      |     |     |                                                                    
  18.70%   |                      |     |     |                                                                    
  15.59%   |                      |     |     |                                                                    
  12.47%   |                |     |     |     |                                                                    
   9.35%   |                |     |     |     |                                                                    
   6.23%   |          |     |     |     |     |                                                                    
   3.12%   |    |     |     |     |     |     |     |                                                              
   ssss    |    0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16
 frequency | .0288 .0568 .1124 .2077 .3117 .2340 .0407 .0062 .0005 .0010 .0000 .0001 .0000 .0000 .0000 .0000 .0000 
   code    |    e     0     1     2     3     4     5     6    1e    3e    7e    fe    1fe   3fe   7fe   ffe  1ffe 
code Length|    4     3     3     3     3     3     3     3     5     6     7     8     9    10    11    12    13  
Encode Bits|    4     4     5     6     7     8     9    10    13    15    17    19    21    23    25    27    13 
```
- LJ92: four pixels sums ->
```
Four pixels count of (16Bits) : 1 time.
Four pixels count of (17Bits) : 4 times.
Four pixels count of (18Bits) : 11 times.
Four pixels count of (19Bits) : 39 times.
Four pixels count of (20Bits) : 106 times.
Four pixels count of (21Bits) : 239 times.
Four pixels count of (22Bits) : 413 times.
Four pixels count of (23Bits) : 680 times.
Four pixels count of (24Bits) : 968 times.
Four pixels count of (25Bits) : 1254 times.
Four pixels count of (26Bits) : 1432 times.
Four pixels count of (27Bits) : 1382 times.
Four pixels count of (28Bits) : 1259 times.
Four pixels count of (29Bits) : 971 times.
Four pixels count of (30Bits) : 579 times.
Four pixels count of (31Bits) : 374 times.
Four pixels count of (32Bits) : 209 times.
Four pixels count of (33Bits) : 101 times.
Four pixels count of (34Bits) : 59 times.
Four pixels count of (35Bits) : 36 times.
Four pixels count of (36Bits) : 22 times.
Four pixels count of (37Bits) : 29 times.
Four pixels count of (38Bits) : 20 times.
Four pixels count of (39Bits) : 13 times.
Four pixels count of (40Bits) : 13 times.
Four pixels count of (42Bits) : 4 times.
Four pixels count of (43Bits) : 6 times.
Four pixels count of (46Bits) : 4 times.
Four pixels count of (49Bits) : 1 time.
Four pixels count of (60Bits) : 10 times.
Four pixels count of (76Bits) : 1 time.
```

## random.raw12:
- IMG: Width  -> 4096
- IMG: Height -> 10
- LJ92: Huffman used to compress -> {0b1110, 0b000,0b001,0b010,0b011,0b100,0b101,0b110,0b11110,0b111110,0b1111110,0b11111110,0b111111110,0b1111111110,0b11111111110,0b111111111110,0b1111111111110}
- LJ92: 4 components.
- LJ92: predictor 1 is used.
- LJ92: normal height and width.
- LJ92: compression ratio: 1.554508.
- LJ92: pixel size: 18.654102 bits.
- LJ92: SSSS analyses ->
```
  31.46%   |                                                                      |                                
  28.32%   |                                                                      |                                
  25.17%   |                                                                      |     |                          
  22.02%   |                                                                      |     |                          
  18.88%   |                                                                |     |     |                          
  15.73%   |                                                                |     |     |                          
  12.58%   |                                                          |     |     |     |                          
   9.44%   |                                                          |     |     |     |                          
   6.29%   |                                                    |     |     |     |     |                          
   3.15%   |                                              |     |     |     |     |     |                          
   ssss    |    0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16
 frequency | .0002 .0005 .0011 .0021 .0038 .0079 .0153 .0306 .0593 .1119 .1999 .3146 .2528 .0000 .0000 .0000 .0000 
   code    |    e     0     1     2     3     4     5     6    1e    3e    7e    fe    1fe   3fe   7fe   ffe  1ffe 
code Length|    4     3     3     3     3     3     3     3     5     6     7     8     9    10    11    12    13  
Encode Bits|    4     4     5     6     7     8     9    10    13    15    17    19    21    23    25    27    29
```
- LJ92: four pixels sums ->
```
Four pixels count of (35Bits) : 1 times.
Four pixels count of (39Bits) : 1 times.
Four pixels count of (42Bits) : 2 times.
Four pixels count of (44Bits) : 2 times.
Four pixels count of (45Bits) : 2 times.
Four pixels count of (46Bits) : 5 times.
Four pixels count of (47Bits) : 8 times.
Four pixels count of (48Bits) : 10 times.
Four pixels count of (49Bits) : 9 times.
Four pixels count of (50Bits) : 11 times.
Four pixels count of (51Bits) : 11 times.
Four pixels count of (52Bits) : 23 times.
Four pixels count of (53Bits) : 24 times.
Four pixels count of (54Bits) : 37 times.
Four pixels count of (55Bits) : 45 times.
Four pixels count of (56Bits) : 51 times.
Four pixels count of (57Bits) : 92 times.
Four pixels count of (58Bits) : 101 times.
Four pixels count of (59Bits) : 127 times.
Four pixels count of (60Bits) : 158 times.
Four pixels count of (61Bits) : 184 times.
Four pixels count of (62Bits) : 233 times.
Four pixels count of (63Bits) : 224 times.
Four pixels count of (64Bits) : 351 times.
Four pixels count of (65Bits) : 268 times.
Four pixels count of (66Bits) : 556 times.
Four pixels count of (67Bits) : 225 times.
Four pixels count of (68Bits) : 809 times.
Four pixels count of (69Bits) : 166 times.
Four pixels count of (70Bits) : 1031 times.
Four pixels count of (71Bits) : 84 times.
Four pixels count of (72Bits) : 1207 times.
Four pixels count of (73Bits) : 17 times.
Four pixels count of (74Bits) : 1310 times.
Four pixels count of (76Bits) : 1167 times.
Four pixels count of (78Bits) : 868 times.
Four pixels count of (80Bits) : 564 times.
Four pixels count of (82Bits) : 226 times.
Four pixels count of (84Bits) : 30 times.
```