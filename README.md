# JPEG 1992 lossless encoder core
Implementation of JPEG 1992 lossless encoder core in python using nmigen.
```
               Main Pipeline for LJ92 encoder

+-----------+------------+------------+---------+--------+
|           |            |            |         |        |
| Predictor | Difference | Normalizer | Encoder | Merger |
|           |            |            |         |        |
+--------------------------------------------------------+
<------------------------| Must |------------------------>
+----------->------------>------------>--------->--------+
```
```
                                                 Main Core Pipeline

+---------------+------+-----------+------+------------------+------------+------------------+
|               |      |           |      |                  |            |                  |
| LJ92 Pipeline | FIFO | Converter | FIFO | V-bits to C-bits | 0xFF Fixer | Start/End marker |
|               |      |           |      |                  |            |                  |
+----------------------+-----------+------+------------------+------------+------------------+
<-------| Must |------> <--| Optional |--> <----| Must |----> <|Optional|> <--| Optional |--->
+--------------->------>----------->------>------------------>------------>------------------+
```
```
                        Non-pipeline Components

+---------------+  +---------+  +--------------------+  +--------------+
|               |  |         |  |                    |  |              |
| Register File |  | Signals |  | AXI-Lite interface |  | Debug Module |
|               |  |         |  |                    |  |              |
+---------------+  +---------+  +--------------------+  +--------------+

<-+ Optional +-->  <+ Must +->  <----+ Optional +---->  <-+ Optional +->
```