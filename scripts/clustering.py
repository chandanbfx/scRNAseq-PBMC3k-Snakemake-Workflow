import scanpy as sc
adata = sc.read(snakemake.input[0])
sc.tl.leiden(adata, resolution=float(snakemake.config["params"]["resolution"]))
adata.write(snakemake.output[0])
