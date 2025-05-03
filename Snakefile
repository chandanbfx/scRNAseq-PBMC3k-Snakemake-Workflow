# Snakefile

configfile: "config/config.yaml"

include: "rules/create_anndata.smk"
include: "rules/qc.smk"
include: "rules/normalize.smk"
include: "rules/batch_correction.smk"
include: "rules/reduce_dim.smk"
include: "rules/clustering.smk"
include: "rules/annotation.smk"
include: "rules/markers.smk"

rule all:
    input:
        "results/marker_genes/marker_table.csv",
        "results/annotation/cluster_labels.csv"
