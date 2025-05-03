rule batch_correction:
    input: "results/normalized.h5ad"
    output: "results/batch_corrected.h5ad"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/batch_correction.py"
