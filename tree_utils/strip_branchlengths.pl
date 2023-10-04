# this script strips branch lengths from newick trees in preparation for divergence time estimation
#
perl -ne '$_=~s/:[\d\.]+//g; print $_;' tree.nwk >output_tree.nwk
