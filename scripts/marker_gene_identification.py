import scanpy as sc
adata = sc.read(snakemake.input[0])
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, save=".png")
markers = sc.get.rank_genes_groups_df(adata, group=None)
markers.to_csv(snakemake.output[0], index=False)
