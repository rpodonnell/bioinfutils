# this script takes an input fasta with headers in the format >GU066228.1_Rhizanthella_gardneri and replaces the header with the format >RHIZgard

# usage 

#python rename_accessions.py input.fasta output.fasta

import argparse
from Bio import SeqIO

def rename_fasta_accessions(input_file, output_file):
    # Open the output FASTA file for writing
    with open(output_file, 'w') as output_handle:
        # Iterate through the input FASTA file and rename accessions
        for record in SeqIO.parse(input_file, 'fasta'):
            header_parts = record.description.split('_')
            
            # Ensure there are at least three parts in the header
            if len(header_parts) >= 3:
                # Capitalize the first four letters of the second part
                genus = header_parts[1][:4].upper()
                
                # Get the first four letters of the third part
                species = header_parts[2][:4]
                
                # Concatenate genus and species to form the new accession
                new_accession = genus + species
                
                # Set the new accession as the description, replacing the original
                record.description = new_accession
                
                # Write the modified record to the output file
                output_handle.write(f">{record.description}\n{record.seq}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename accessions in a FASTA file.")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("output_file", help="Output renamed FASTA file")

    args = parser.parse_args()

    rename_fasta_accessions(args.input_file, args.output_file)

