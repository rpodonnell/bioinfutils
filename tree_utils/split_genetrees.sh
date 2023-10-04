# use these commands to split a genetree file containing n genetrees into single files containing a single tree

split --numeric=1 -l 1 -d -a 4 locus.treefile gene_

for i in gene_* ; do mv $i $i.tree ; done
