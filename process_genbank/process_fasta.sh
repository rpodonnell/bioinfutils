# This is a bash script of common commands to process genbank output

# Remove all spaces and replace with _
sed -i 's/ /_/g' file 

# Remove everything after the nth (here 3rd) iteration of a specified character (in this case, _)

sed 's/_[^_]*//3g' file # reminder that this will only print the changes remember to add either the -i argument or direct the output to a file with >

# Replace Ns with gaps
# I've written this in such a way that it should replace any Ns in the actual taxon name with a lower case n before it does the change so that they're not also converted to gaps
f=file &&
sed -i 's/_N/_n/g' $f && sed -i 's/N/-/g' $f && sed -i 's/_n/_N/g' $f  
