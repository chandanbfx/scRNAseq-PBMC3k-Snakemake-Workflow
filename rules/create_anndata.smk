rule create_anndata:
    input:
        matrix="data/matrix.mtx",
        genes="data/genes.tsv",
        barcodes="data/barcodes.tsv"
    output:
        "results/anndata.h5ad"
    conda:
        "../envs/scanpy.yaml"
    script:
        "../scripts/create_anndata.py"
