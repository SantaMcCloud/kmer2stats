# kmer2stats

[![PyPI version](https://img.shields.io/pypi/v/kmer2stats.svg)](https://pypi.org/project/kmer2stats/)[![Bioconda](https://img.shields.io/conda/vn/bioconda/kmer2stats.svg)](https://anaconda.org/bioconda/kmer2stats)

**kmer2stats** computes k-mer based statistics for microbial community analysis, including a wide range of alpha diversity metrics (e.g. *Shannon*, *Chao1*, *inverse Simpson*) and descriptive count statistics (e.g. *total_count*, *unique_kmers*, *percent_singletons*). The output can be used for downstream plotting or comparative analyses.

## Installation

All dependencies (`pandas>=2.2.2`, `numpy>=1.26.4`, `scikit-bio>=0.6.3`, `argparse>=1.4.0`) are automatically installed by both methods below.

### With pip

```bash
pip install kmer2stats
```

Or directly from source:

```bash
git clone https://github.com/SantaMcCloud/kmer2stats.git
cd kmer2stats
pip install -r requirements.txt
```

### With conda

```bash
conda install bioconda::kmer2stats
```

## Usage

```bash
kmer2stats count_file
```

kmer2stats is also available as a **Galaxy tool** on the [usegalaxy.eu](https://usegalaxy.eu) server — search for `kmer2stats` in the tool panel.

## Input

The input is a space-separated k-mer count file with two columns (k-mer sequence and count), without a header. This is the format produced by [`jellyfish dump`](https://github.com/gmarcais/Jellyfish):

```
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

A test file is provided in [`test_files/test_file.txt`](test_files/test_file.txt).

## Output

The output is a tab-separated (TSV) file (`compute_diversity.csv`) with two columns: the metric name and its computed value. Diverse metrics are reported:

### Richness estimators

| Metric | Description |
|---|---|
| `observed_features` | Number of distinct k-mers observed |
| `singles` | Number of k-mers observed exactly once (singletons) |
| `doubles` | Number of k-mers observed exactly twice (doubletons) |
| `chao1` | Chao1 non-parametric richness estimator |
| `ace` | Abundance-based coverage estimator (ACE) |
| `margalef` | Margalef's richness index |
| `menhinick` | Menhinick's richness index |

### Diversity indices

| Metric | Description |
|---|---|
| `shannon` | Shannon entropy (H') — measures overall diversity |
| `brillouin_d` | Brillouin index — diversity for fully censused communities |
| `fisher_alpha` | Fisher's alpha diversity index |
| `hill` | Hill number (order 1) — effective number of species |
| `renyi` | Rényi entropy |
| `tsallis` | Tsallis entropy |

### Evenness metrics

| Metric | Description |
|---|---|
| `pielou_e` | Pielou's evenness (J') — Shannon evenness |
| `heip_e` | Heip's evenness index |
| `mcintosh_e` | McIntosh evenness index |
| `simpson_e` | Simpson's evenness index |
| `enspie` | ENS_PIE (effective number of species via PIE) |

### Dominance and concentration metrics

| Metric | Description |
|---|---|
| `simpson_d` | Simpson's dominance index (D) |
| `inv_simpson` | Inverse Simpson index (1/D) |
| `berger_parker_d` | Berger-Parker dominance index |
| `dominance` | Dominance index |
| `gini_index` | Gini coefficient of inequality |
| `mcintosh_d` | McIntosh dominance index |
| `strong` | Strong's dominance index |
| `kempton_taylor_q` | Kempton-Taylor Q statistic |

### Coverage and completeness

| Metric | Description |
|---|---|
| `goods_coverage` | Good's coverage estimator |
| `robbins` | Robbins' estimator of the probability of unseen species |

### Descriptive statistics

| Metric | Description |
|---|---|
| `total_count` | Sum of all k-mer counts |
| `unique_kmers` | Number of distinct k-mers |
| `mean_count` | Mean count per k-mer |
| `median_count` | Median count per k-mer |
| `max_count` | Maximum k-mer count |
| `min_count` | Minimum k-mer count |
| `std_count` | Standard deviation of counts |
| `count_range` | Range of counts (max − min) |
| `num_singletons` | Number of k-mers with count = 1 |
| `num_doubletons` | Number of k-mers with count = 2 |
| `percent_singletons` | Percentage of unique k-mers that are singletons |

## Citation

If you use kmer2stats, please cite:

> Faack, S. (2026). *kmer2stats* (v1.0.2). Zenodo. https://doi.org/10.5281/zenodo.19828576

## License

[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)