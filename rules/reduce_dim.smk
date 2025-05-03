rule dimensionality_reduction:
    input: "results/batch_corrected.h5ad"
    output: "results/reduced.h5ad"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/dimensionality_reduction.py"
