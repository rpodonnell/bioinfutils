# This script takes a fasta file as input, removes any accessions with strings input as a comma separated list, and outputs a filtered fasta file

# usage example
# python filter_fasta.py input.fasta output.fasta string1,string2,string3



import argparse
from Bio import SeqIO

def filter_fasta(input_file, output_file, search_strings):
    # Convert the comma-separated search strings to a list
    search_strings = search_strings.split(',')

    # Open the output file for writing
    with open(output_file, 'w') as output_handle:
        # Iterate through the input FASTA file and write matching sequences to the output
        for record in SeqIO.parse(input_file, 'fasta'):
            header = record.description
            # Check if any of the search strings are in the header
            if not any(search in header for search in search_strings):
                SeqIO.write(record, output_handle, 'fasta')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter sequences in a FASTA file based on header strings.")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("output_file", help="Output FASTA file")
    parser.add_argument("search_strings", help="Comma-separated list of search strings")

    args = parser.parse_args()

    filter_fasta(args.input_file, args.output_file, args.search_strings)

