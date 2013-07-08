#Simple Hash
A python scrypt I am using for basic benchmarking (To mainly see difference in speed between PCs and operating systems).

##Your results are needed! 
To get your results.
Git clone this project or just download the hash.py file

run "python hash.py 1 2 3 4 5"
Note the time taken (Printed at the end of the run)
Repeat another 2 times.
Create an issue with the tag "benchmark" with the following:
CPU / PC (Mainly the CPU Model and Clock rate are needed here)
Numbers Tested (1 2 3 4 and 5 if the arguments given are as above)
Arch ( Python Architecture, Normally what your computer runs [Depending on what you install])
Operating System (You should know this, also include your OS's Arch in brackets)
Time Taken 1, Time Taken 2 & Time Taken 3 (The results from your tests. 3 Decimal Points are prefered).

###Thanks if you do it! The results will be used for a possible future Raspberry Pi project.


Results:

| CPU / PC | Numbers Tested | Arch | Operating Sys | Time Taken 1 | Time Taken 2 | Time Taken 3 |
| --- | --- | --- | --- | --- | --- | --- |
| AMD FX-8350 @ 4Ghz | 1 2 3 4 5 | x86_64 | Win 7 Home Prem (x86_64) | 26.741 | 26.319 | 26.457 |
| Raspberry Pi Model B (512) @ Medium OC | 1 2 3 4 5 | ARM / ARMHF | Raspbian (ARMHF) | 26.741 | 26.319 | 26.457 |
| Intel(R) Core(TM) i3-2350M CPU @ 2.30GHz | 1 2 3 4 5 | x86_64 | Ubuntu 13.04 x86_64 | 19.402 | 19.962 | 20.45 |
<!--- Template | Blank | 1 2 3 4 5 | x86 / x86_64 / ARM / Arch | OS (Arch) | 0.000 | 0.000 | 0.000 |--->
