import pandas as pd
from kmer2stats.core import compute_stats_from_counts


def test_kmer_file_input(tmp_path):
    # 1. Create a temporary file
    file_path = tmp_path / "kmers.txt"

    # 2. Write test data
    file_path.write_text("""
AAAAAC 6870
AAAAAG 6312
AAAAAT 7966
AAAACA 5133
AAAACC 5600
AAAACG 5870
AAAACT 3911
""")

    # 3. Run function
    result = compute_stats_from_counts(str(file_path))

    # 4. Assertions
    assert isinstance(result, pd.DataFrame)
    # check values properly
    assert "shannon" in result.index
    assert result.loc["num_singletons"].values[0] == 0