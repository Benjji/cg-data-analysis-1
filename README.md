# cg-data-analysis-1

First we obtain reference file GCA_000001405.28_GRCh38.p13_genomic.fna.gz

Then we index it:
  bwa index refgene_x.fa

We generate BAM files.

First let us do it for tumor read files.

  bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz  tu.r1.fq.gz tu.r2.fq.gz > tumor.sam
  samtools view -O BAM -o tumor.bam tumor.sam
  samtools sort -T temp -O bam -o tumor.sorted.bam tumor.bam
  samtools index tumor.sorted.bam
  samtools view -b tumor.bam chrX:20000000-40000000 > tumor_subset.bam

