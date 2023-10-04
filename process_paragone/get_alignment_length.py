# this script loops through all loci in the 28_RT_final_alignments_trimmed folder produced by paragone and outputs a CSV with alignment lengths and taxon coverage
import os
import csv
import argparse
from Bio import AlignIO

def get_alignment_length(align):
    return align.get_alignment_length()

def process_fasta_files(input_dir, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['name', 'sequences', 'alignment_length'])

        fasta_files = [f for f in os.listdir(input_dir) if f.endswith('.fasta')]

        for fasta_file in fasta_files:
            fasta_path = os.path.join(input_dir, fasta_file)
            alignment = AlignIO.read(fasta_path, 'fasta')
            num_sequences = len(alignment)
            alignment_length = get_alignment_length(alignment)
            csv_writer.writerow([fasta_file, num_sequences, alignment_length])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process FASTA files and generate a CSV file.')
    parser.add_argument('input_directory', help='Input directory containing FASTA files')
    parser.add_argument('output_csv_file', help='Output CSV file name')

    args = parser.parse_args()
    input_directory = args.input_directory
    output_csv_file = args.output_csv_file

    process_fasta_files(input_directory, output_csv_file)
    print("CSV file generated successfully!")

