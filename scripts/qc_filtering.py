import scanpy as sc
import sys
adata = sc.read(snakemake.input[0])

adata.var["mt"] = adata.var_names.str.startswith("MT-")
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)
adata = adata[adata.obs.n_genes_by_counts > int(snakemake.config["params"]["min_genes"]), :]
adata = adata[adata.obs.n_genes_by_counts < int(snakemake.config["params"]["max_genes"]), :]
adata = adata[adata.obs.pct_counts_mt < float(snakemake.config["params"]["max_mt"]), :]

adata.write(snakemake.output[0])
