# scRNA-seq Snakemake Workflow

This repository contains a comprehensive and modular Snakemake workflow for single-cell RNA-seq (scRNA-seq) analysis using the 10x Genomics PBMC 3k dataset.

## Dataset

Download the filtered gene-barcode matrix from 10x Genomics:

```bash
curl -L -o pbmc3k_filtered_gene_bc_matrices.tar.gz https://cf.10xgenomics.com/samples/cell/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz
mkdir -p data/pbmc3k
tar -xzf pbmc3k_filtered_gene_bc_matrices.tar.gz -C data/ --strip-components=1
```

This will create the following input files in `raw_data/`:
- `barcodes.tsv`
- `genes.tsv`
- `matrix.mtx`

## Folder Structure

```
.
├── config/
│   └── config.yaml
├── envs/
│   └── scanpy.yaml
├── data/
│       ├── barcodes.tsv
│       ├── genes.tsv
│       └── matrix.mtx
├── results/
├── rules/
│   ├── create_anndata.smk
│   ├── qc.smk
│   ├── normalize.smk
│   ├── batch_correction.smk
│   ├── reduce_dim.smk
│   ├── clustering.smk
│   ├── markers.smk
│   └── annotation.smk
├── scripts/
│   ├── create_anndata.py
│   ├── qc_filtering.py
│   ├── normalization.py
│   ├── batch_correction.py
│   ├── dimensionality_reduction.py
│   ├── clustering.py
│   ├── marker_gene_identification.py
│   └── annotation.py
├── .gitignore
├── LICENSE
└── Snakefile
```

## Usage

Create conda environments and run the workflow:

```bash
snakemake --use-conda --conda-frontend conda --cores 4
```

## License

This project is licensed under the MIT License.


**Acknowledgements**

This workflow uses the following tools and libraries:

    Scanpy: https://scanpy.readthedocs.io/en/stable/
    
    BBKNN: https://github.com/Teichlab/bbknn
    
    Scanorama: https://github.com/brianhie/scanorama
    
    Harmonypy: https://github.com/slowkow/harmonypy
    
    Leidenalg: https://github.com/vtraag/leidenalg
    
    iGraph (Python): https://igraph.org/python/
    
    Snakemake: https://snakemake.readthedocs.io/en/stable/
    
    AnnData: https://anndata.readthedocs.io/en/latest/
