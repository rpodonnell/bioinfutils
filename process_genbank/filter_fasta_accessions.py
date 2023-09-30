# this script takes a fasta file and a namelist as input and outputs a filtered fasta which only has the accessions in the namelist
# usage
# python filter_fasta_accessions.py input.fasta accession_list.txt output.fasta
import argparse
from Bio import SeqIO

def filter_fasta_by_accessions(fasta_file, accession_file, output_file):
    # Read accession numbers from the text file into a set
    with open(accession_file, 'r') as accession_handle:
        accession_set = set(line.strip() for line in accession_handle)

    # Open the output FASTA file for writing
    with open(output_file, 'w') as output_handle:
        # Iterate through the input FASTA file and write matching sequences to the output
        for record in SeqIO.parse(fasta_file, 'fasta'):
            # Extract the accession number from the sequence header
            header = record.description
            
            # Check if any accession string from the namelist is present in the header
            if any(accession in header for accession in accession_set):
                SeqIO.write(record, output_handle, 'fasta')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter a FASTA file by accession numbers from a text file.")
    parser.add_argument("fasta_file", help="Input FASTA file")
    parser.add_argument("accession_file", help="Text file with accession numbers")
    parser.add_argument("output_file", help="Output filtered FASTA file")

    args = parser.parse_args()

    filter_fasta_by_accessions(args.fasta_file, args.accession_file, args.output_file)

