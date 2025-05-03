rule annotate_clusters:
    input:
        anndata="results/clusters.h5ad",
        marker_table="results/marker_genes/marker_table.csv"
    output:
        annotated_adata="results/annotation/adata_annotated.h5ad",
        cluster_labels="results/annotation/cluster_labels.csv"
    conda:
        "../envs/scanpy.yaml"
    threads: 4
    resources:
        mem_mb=8000
    script:
        "../scripts/annotate_clusters.py"
