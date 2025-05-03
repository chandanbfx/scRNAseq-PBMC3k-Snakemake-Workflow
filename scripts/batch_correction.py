import scanpy as sc
import scanorama
import scipy.sparse

adata = sc.read(snakemake.input[0])

# Add dummy batch label for testing (only needed for single-sample test data)
adata.obs["batch"] = "batch1"

# Convert .X to csr_matrix if it's in csc_matrix format
if not isinstance(adata.X, scipy.sparse.csr_matrix):
    adata.X = adata.X.tocsr()

# Split data by batch
adata_list = [adata[adata.obs["batch"] == b].copy() for b in adata.obs["batch"].unique()]

# Correct
corrected = scanorama.correct_scanpy(adata_list, return_dimred=True)

# Concatenate corrected objects
adata_corrected = corrected[0].concatenate(corrected[1:])

# Save
adata_corrected.write(snakemake.output[0])
