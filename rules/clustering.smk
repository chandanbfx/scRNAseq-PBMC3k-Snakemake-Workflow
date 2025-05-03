rule clustering:
    input: "results/reduced.h5ad"
    output: "results/clusters.h5ad"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/clustering.py"
