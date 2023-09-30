# this script contains commands for using itsx

conda activate itsx

# plant
in=input_file &&
ITSx -i $in -o itsx -t T --cpu 10 --save_regions all --preserve T 

# fungi 
in=input_file &&
ITSx -i $in -o itsx -t F --cpu 10 --save_regions all --preserve T 
