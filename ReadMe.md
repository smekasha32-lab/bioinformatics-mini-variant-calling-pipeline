# Mini Variant Calling Pipeline

A Python-based bioinformatics project that detects single nucleotide polymorphisms (SNPs) by comparing a sequencing read to a reference DNA sequence. The program reads FASTA files, identifies sequence differences, and writes the detected variants to a simplified VCF-like output file.

## Features

- Read DNA sequences from FASTA files
- Compare a sequencing read to a reference sequence
- Detect single nucleotide variants (SNPs)
- Output detected variants to a VCF-like file
- reusable Python functions

## Project Structure

```
bioinformatics-mini-variant-calling-pipeline/
│
├── mini_varient_calling_pipeline.py
├── reference.fasta
├── read.fasta
├── variants.vcf
└── README.md
```

## Input Files

### reference.fasta

```
>Reference
ATCGATCG
```

### read.fasta

```
>Read
ATGGATCG
```

## Example Output

### Console Output

```
[{'Position': 3, 'Reference': 'C', 'Alternate': 'G'}]
```

### variants.vcf

```
Position    Reference    Alternate
3           C            G
```

## Concepts Demonstrated

### Python

- Functions
- Parameters
- Return values
- Lists
- Dictionaries
- Loops
- Conditional statements
- File input/output
- Modular programming

### Bioinformatics

- FASTA file parsing
- Reference genome comparison
- SNP detection
- Variant calling
- VCF-style output
- Genomic coordinates (1-based indexing)

## Author

**Solomon Ketyebelu**