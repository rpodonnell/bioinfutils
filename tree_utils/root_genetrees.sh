# use this to root all gene trees in a file. add the argument -r to have ranked outgroups so it will root in the order that outgroups appear in the gene trees if a specified outgroup taxon is absent
pxrr -t input.tree -g outgroup1,outgroup2,outgroup3 -o output.tree
