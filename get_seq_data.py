# This script takes in a fasta file, and outputs a csv file with the genbank accession number, genus, species, and sequence length as columns. This script assumes that each fasta header is in the format >genbank_Genus_species
# usage 
# python get_seq_data.py input.fasta output.csv

import argparse
import csv
from Bio import SeqIO

def fasta_to_csv(input_file, output_file):
    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['genbank_no', 'genus', 'species', 'seq_length'])

        # Iterate through the input FASTA file and write data to the CSV
        for record in SeqIO.parse(input_file, 'fasta'):
            header_parts = record.description.split('_')
            
            # Extract genbank_no, genus, and species from the header
            genbank_no = header_parts[0]
            genus = header_parts[1]
            species = header_parts[2]
            
            # Calculate sequence length
            seq_length = len(record.seq)
            
            # Write data to the CSV file
            csv_writer.writerow([genbank_no, genus, species, seq_length])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert FASTA file to CSV with header split and sequence length.")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("output_file", help="Output CSV file")

    args = parser.parse_args()

    fasta_to_csv(args.input_file, args.output_file)

