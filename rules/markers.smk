rule marker_gene_identification:
    input: "results/clusters.h5ad"
    output: "results/marker_genes/marker_table.csv"
    conda: "../envs/scanpy.yaml"
    script: "../scripts/marker_gene_identification.py"
