# kmer2stats

[![PyPI version](https://img.shields.io/pypi/v/kmer2stats.svg)](https://pypi.org/project/kmer2stats/)[![Bioconda](https://img.shields.io/conda/vn/bioconda/kmer2stats.svg)](https://anaconda.org/bioconda/kmer2stats)

A tool for creating data files for statistic based on kmers. Kmer2stat create all form of diversity metrics like *shannon*,*chao1* or *inv_simpson*. Also normal statistic are calculated by kmer2stats like *total_count*,*unique_kmers* or *percent_singletons*. The output can be used for creating plots with scrips or other tools.

## Installation 

### install with pip 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install kmer2stats.

```bash
pip install kmer2stats
```

Or use the source with pip to install kmer2stats.

```bash
git clone https://github.com/SantaMcCloud/kmer2stats.git
cd kmer2stats
pip install -r requirements.txt
```

### install with Bioconda 
Use [Bioconda](https://bioconda.github.io/recipes/kmer2stats/README.html) to install kmer2stats.

```bash
conda install kmer2stats
```

## Usage

```bash
kmer2stats.py count_file
```

Check [input](#input) for a example file if you want to make the count_file yourself or use the tool [Jellyfish](https://github.com/gmarcais/Jellyfish) to create a count_file.

## Input
As Input you can use either the output from the tool jellyfish or you can use your own file in followed format:

```bash
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

## Output

This tool output a `.csv` with the followed metrics:

```bash
shannon
simpson_d
pielou_e
berger_parker_d
doubles
chao1
ace
margalef
menhinick
observed_features
singles
brillouin_d
enspie
fisher_alpha
hill
inv_simpson
kempton_taylor_q
renyi
tsallis
heip_e
mcintosh_e
simpson_e
dominance
gini_index
mcintosh_d
strong
goods_coverage
robbins
total_count
unique_kmers
mean_count
median_count
max_count
min_count
std_count
count_range
num_singletons
num_doubletons
percent_singletons
```

## License

[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)