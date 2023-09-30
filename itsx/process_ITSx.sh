# this script automates subsequent processing of itsx output

# move stats output
mkdir stats;
mv *.txt stats;
mv *.graph stats;
mv *_no_detections.fasta stats;

# loci to retain
mkdir align;
for f in  5_8S ITS1 ITS2; do
	mv *$f* align;
done;

# loci to exclude

mkdir exclude;
for f in LSU SSU full; do
	mv *$f* exclude
done
