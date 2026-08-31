import pytest
from preprocess.preprocess_rna_seq import preprocess_rna_seq

def test_preprocess_rna_seq():
    """
    This is a placeholder test for the RNA-seq data preprocessing function.
    """
    data = {"gene1": 1, "gene2": 2}
    assert preprocess_rna_seq(data) == data
