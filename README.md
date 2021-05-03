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

    bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz  wt.r1.fq.gz wt.r2.fq.gz > wildtype.sam
    samtools view -O BAM -o wildtype.bam wildtype.sam
    samtools sort -T temp -O bam -o wildtype.sorted.bam wildtype.bam
    samtools index wildtype.sorted.bam
    samtools view -b wildtype.bam chrX:20000000-40000000 > wildtype_subset.bam
    
BAM files contain compressed information about alignment of input reads
to human reference genome. 

In the next step, we extract coverage statistics from BAM files into 
respective files:

    samtools depth tumor.sorted.bam > tumor.sorted.coverage
    samtools depth wildtype.sorted.bam > wildtype.sorted.coverage

When we take a look at the newest assembly of a human reference genome
(`https://www.ncbi.nlm.nih.gov/grc/human/data?asm=GRCh38`),
we see chromosome X has GenBank accession code `CM000685.2`, which we may find
in coverage files generated in the previous step.

We parse relevant information out from coverage files using following commands:

    perl -lane  'print "$F[1]\t$F[2]" if $F[1] > 20000000 and $F[1] < 40000000 and $F[0]=~m/CM000685/' < wildtype.sorted.coverage > wildtype.sorted.coverage.filtered
    perl -lane  'print "$F[1]\t$F[2]" if $F[1] > 20000000 and $F[1] < 40000000 and $F[0]=~m/CM000685/' < tumor.sorted.coverage > tumor.sorted.coverage.filtered



    
    
