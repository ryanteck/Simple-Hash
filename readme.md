#Simple Hash
A python scrypt I am using for basic benchmarking (To mainly see difference in speed between PCs I have).

Results:

| CPU / PC | Numbers Tested | Arch | Operating Sys | Time Taken 1 | Time Taken 2 | Time Taken 3 |
| --- | --- | --- | --- | --- | --- |
| AMD FX-8350 @ 4Ghz | 1 2 3 4 5 | x86 Python | Win 7 Home Prem (x86_64) | 26.741 | 26.319 | 26.457 |
| Raspberry Pi Model B (512) @ Medium | 1 2 3 4 5 | Arch | Raspbian (ARMHF) | 26.741 | 26.319 | 26.457 |
| Blank | 1 2 3 4 5 | x86 / x86_64 / ARM / Arch | OS (Arch) | 0.000 | 0.000 | 0.000 |
