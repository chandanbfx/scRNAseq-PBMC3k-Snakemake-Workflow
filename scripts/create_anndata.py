import scanpy as sc
import pandas as pd
from scipy import io
import sys

matrix = io.mmread(snakemake.input["matrix"]).T.tocsc()
genes = pd.read_csv(snakemake.input["genes"], header=None, sep='\t')
barcodes = pd.read_csv(snakemake.input["barcodes"], header=None)

adata = sc.AnnData(X=matrix)
adata.var_names = genes[0]
adata.obs_names = barcodes[0]

adata.write(snakemake.output[0])
