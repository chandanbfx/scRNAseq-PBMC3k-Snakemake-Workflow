rule normalize_data:
    input: "results/qc_filtered.h5ad"
    output: "results/normalized.h5ad"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/normalization.py"
