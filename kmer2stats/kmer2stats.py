#!/usr/bin/env python
import pandas as pd
import numpy as np
from skbio.diversity import alpha_diversity
import argparse
import time

def parse_arguments():
    """
    This function is there to capture the arguments in the command line and to parse them to use them correctly.

    Please refer to the usage how to use this tool.

    """

    parser = argparse.ArgumentParser(
        prog="kmer2stats",
        description="This tool was designed to create data files for statistic based on kmers",
        usage="kmer2stats.py count_file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    parser.add_argument(
        "counting_file",
        type=str, 
        help="Input the counting file here."
    )

    parser.add_argument("--version", action="version", version="1.0.1")

    parser.print_usage = parser.print_help

    args = parser.parse_args()

    return args

def compute_stats_from_counts(kmer_file):
    """
    Compute alpha diversity metrics and descriptive statistics from a k-mer count file.

    Parameters:
    -----------
    kmer_file : str
        Path to a k-mer count file (e.g., output from Jellyfish) that can be loaded
        using `load_jellyfish_output`. The file must include a 'count' column with
        integer counts for each unique k-mer.

    Returns:
    --------
    diversity_df : pandas.DataFrame
        A dataframe containing various alpha diversity metrics and descriptive
        statistics. The index is the name of each metric, and the 'Value' column
        contains the computed value for each.

    Metrics computed include:
        - Standard ecological diversity indices (e.g., Shannon, Simpson, Chao1)
        - Richness estimators (e.g., observed features, ACE)
        - Evenness and dominance metrics
        - Summary statistics on the k-mer count distribution:
            - total_count
            - unique_kmers
            - mean/median/std/min/max counts
            - count range
            - number and percentage of singletons/doubletons
    """

    # Load the k-mer counts file into a dataframe
    df = load_jellyfish_output(kmer_file)

    # Extract k-mer counts (assuming 'count' is the relevant column)
    counts = df['count'].tolist()

    # List of alpha diversity metrics to compute
    alpha_metrics = [
        "shannon", "simpson_d", "pielou_e", "berger_parker_d", "doubles", "chao1",
        "ace", "margalef", "menhinick", "observed_features", "singles", "brillouin_d",
        "enspie", "fisher_alpha", "hill", "inv_simpson", "kempton_taylor_q", "renyi",
        "tsallis", "heip_e", "mcintosh_e", "simpson_e", "dominance", "gini_index",
        "mcintosh_d", "strong", "goods_coverage", "robbins",
    ]

    # Dictionary to hold all computed metrics
    diversity_metrics = {}

    # Compute each alpha diversity metric
    for metric_name in alpha_metrics:
        result = alpha_diversity(metric_name, counts)
        diversity_metrics[metric_name] = result[0]

    # Compute basic statistics on the raw count distribution
    total_count = sum(counts)
    unique_kmers = sum(1 for c in counts if c > 0)
    mean_count = np.mean(counts)
    median_count = np.median(counts)
    max_count = max(counts)
    min_count = min(counts)
    std_count = np.std(counts)
    count_range = max_count - min_count
    num_singletons = counts.count(1)
    num_doubletons = counts.count(2)
    percent_singletons = (num_singletons / unique_kmers) * 100 if unique_kmers > 0 else 0

    # Add summary stats to the result dictionary
    diversity_metrics.update({
        'total_count': total_count,
        'unique_kmers': unique_kmers,
        'mean_count': mean_count,
        'median_count': median_count,
        'max_count': max_count,
        'min_count': min_count,
        'std_count': std_count,
        'count_range': count_range,
        'num_singletons': num_singletons,
        'num_doubletons': num_doubletons,
        'percent_singletons': percent_singletons,
    })

    # Convert to a pandas DataFrame
    diversity_df = pd.DataFrame(list(diversity_metrics.items()), columns=["Metric", "Value"])
    diversity_df.set_index("Metric", inplace=True)

    return diversity_df

def load_jellyfish_output(file_path):
    """Loads k-mer counts from a Jellyfish dump file (.tsv)."""
    df = pd.read_csv(file_path, sep=" ", header=None, names=["kmer", "count"], skiprows=1)
    return df

if __name__ == "__main__":
    start_time = time.time()
    args = parse_arguments()
    result_df = compute_stats_from_counts(args.counting_file)
    result_df.to_csv('compute_diversity.csv', sep='\t', index=True)
    end_time = time.time()
    print(f'Run time: {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))}')
