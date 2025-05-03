import scanpy as sc
adata = sc.read(snakemake.input[0])
sc.pp.scale(adata)
sc.tl.pca(adata, svd_solver="arpack", n_comps=int(snakemake.config["params"]["n_pcs"]))
sc.pp.neighbors(adata, n_pcs=int(snakemake.config["params"]["n_pcs"]))
sc.tl.umap(adata)
adata.write(snakemake.output[0])
