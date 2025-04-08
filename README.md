# kmer2stats
A tool for creating data files for statistic based on kmers

# Input
As Input you can use either the output from the tool jellyfish or you can use your own file in followed format:

```
000000543{"alignment":8,"canonical":true,"cmdline":["count","--mer-len","6","--size","32M","--canonical","--text","/data/dnb10/galaxy_db/files/1/7/a/dataset_17a81659-206c-4bd7-b335-57b7d09668f9.dat"],"exe_path":"/usr/local/tools/_conda/envs/__kmer-jellyfish@2.3.0/bin/jellyfish","format":"text/sorted","hostname":"vgcnbwc-worker-c120m405-0004.novalocal","key_len":12,"matrix1":{"c":12,"identity":true,"r":12},"max_reprobe":0,"pwd":"/data/jwd05e/main/079/791/79791039/working","reprobes":[1],"size":4096,"time":"Thu Feb 27 13:11:25 2025","val_len":14}��AAAAAA 8453
AAAAAC 6870
AAAAAG 6312
AAAAAT 7966
AAAACA 5133
AAAACC 5600
AAAACG 5870
AAAACT 3911
AAAAGA 4173
AAAAGC 5078
AAAAGG 3047
AAAAGT 3067
AAAATA 5726
AAAATC 6167
AAAATG 5731
AAAATT 4987
AAACAA 3719
AAACAC 2817
AAACAG 5565
AAACAT 3342
AAACCA 5011
AAACCC 2469
```

# Output

This tool output a `.csv` file which then can be used with other tools/scripts to create plots or other statistics.

