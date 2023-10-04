# this script will rename a set of genes used for tree inference sequentially in the format gene_****.fasta to match the output of splitting a genetree file into multiple trees

a=1
for i in *.fasta; do
  new=$(printf "gene_%04d.fasta" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
