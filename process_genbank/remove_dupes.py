# this script takes output from the get_seq_data.py script, identifies taxa with multiple accessions, and retains only the longest sequence

import argparse
import pandas as pd

def filter_csv(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Group by 'full_name' and keep rows with the maximum 'seq_length' in each group
    filtered_df = df.loc[df.groupby('full_name')['seq_length'].idxmax()]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter a CSV file by retaining the accession with the largest seq_length for each unique full_name.")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("output_file", help="Output CSV file")

    args = parser.parse_args()

    filter_csv(args.input_file, args.output_file)

