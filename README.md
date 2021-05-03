# cg-data-analysis-1

First we obtain reference file `GCA_000001405.28_GRCh38.p13_genomic.fna.gz`

Then we index it:
  `  	bwa index refgene_x.fa`

Next, we generate BAM files.

First let us do it for tumor read files.

    bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz  tu.r1.fq.gz tu.r2.fq.gz > tumor.sam
    samtools view -O BAM -o tumor.bam tumor.sam
    samtools sort -T temp -O bam -o tumor.sorted.bam tumor.bam
    samtools index tumor.sorted.bam
    samtools view -b tumor.bam chrX:20000000-40000000 > tumor_subset.bam

In the same way, we do it for wildcard files.

    bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz  wt.r1.fq.gz wt.r2.fq.gz > wildcard.sam
    samtools view -O BAM -o wildcard.bam wildcard.sam
    samtools sort -T temp -O bam -o wildcard.sorted.bam wildcard.bam
    samtools index wildcard.sorted.bam
    samtools view -b wildcard.bam chrX:20000000-40000000 > wildcard_subset.bam
    
BAM files contain compressed information about alignment of input reads
to human reference genome. 

In the next step, we extract coverage statistics from BAM files into 
respective files:

    
    
