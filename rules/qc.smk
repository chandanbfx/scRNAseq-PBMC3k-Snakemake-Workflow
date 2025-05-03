rule qc_filtering:
    input: "results/anndata.h5ad"
    output: "results/qc_filtered.h5ad"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/qc_filtering.py"
