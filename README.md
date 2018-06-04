# GEMMA Wrapper

A wrapper to run cis-eQTL mapping with GEMMA

## Instructiions

With this wrapper, you can create PLINK files with gene expression as phenotypes and run cis-eQTL mapping with GEMMA.

### Prerequisites

Software:

- Linux or Mac OS
- Python 2.7: 
	- Numpy package
- GEMMA
-  PLINK

Input files:
- plink bfiles
- Expression file
- Matrix eQTL cis-eQTL mapping output



#### GEMMA_input.py
To create PLINK files with gene expression as phenotype
- Input files:
	- PLINK bfiles
	- Expression file. Same format as Matrix eQTL expression file format. One row for each gene, and one column for each sample. The samples in the fam file should be a subset of samples in the expression file. There should be one column for gene name and the column name is “gene_id”. This file should be tab-separated.
- Output file:
	- New PLINK file. The gene expressions are added to the fam file from column 6 to the end. The number of columns is N+5 where N is the number of genes.
	- Gene list file. A list of genes in the same sequence as the gene expression in the fam file, and the number of rows is N.

```

```

#### get_cis_snp.py
To create cis-SNPs for each gene 
- Input files: 
	- Matrix eQTL cis-eQTL mapping results (no p-value filtering applied). 
- Output file:
	- Cis-SNPs for each gene under ./snp_list/ folder. One file for each gene.

```

```

#### run_gemma_parrelle.py

Run GEMMA for 1000 genes at a time

- Input files: 
	- GEMMA bfile (output from GEMMA_input.py). From column six are gene expression measurements (--bfile).
	- Relatedness matrix (--matrix)
	- GEMMA covariate file (--cov)
- Arguments:
	- '--lmm' Frequentist test used by GEMMA univariate LMM
	- --gemma The location of GEMMA executable
	- --index Parallel index. If index = 0, run GEMMA from the gene 0 to the gene 999.
	- --out  The prefix to give to the output files
- Output file:
	- GEMMA output for each gene as the phenotype

#### gerp_pve.py

Get the PVE estimates for all genes in the output folder

- Output
	--out The prefix to give to the output file


## Authors

* **Yizhen Zhong** - *

## License



## Acknowledgments


