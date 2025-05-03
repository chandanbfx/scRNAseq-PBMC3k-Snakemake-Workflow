import scanpy as sc
import pandas as pd
import sys

# Snakemake inputs
adata_file = snakemake.input.anndata
marker_table_file = snakemake.input.marker_table
annotated_adata_file = snakemake.output.annotated_adata
cluster_labels_file = snakemake.output.cluster_labels

# Load data
adata = sc.read_h5ad(adata_file)
marker_df = pd.read_csv(marker_table_file)

# Example: Assigning cluster names manually using marker genes
cluster_mapping = {
    0: "T cells",
    1: "B cells",
    2: "NK cells",
    3: "Monocytes",
    4: "Dendritic cells",
    # Add more cluster labels as needed
}

# Annotate clusters
adata.obs['cell_type'] = adata.obs['leiden'].astype(int).map(cluster_mapping)

# Save annotations
adata.write(annotated_adata_file)
adata.obs[['leiden', 'cell_type']].drop_duplicates().to_csv(cluster_labels_file, index=False)
