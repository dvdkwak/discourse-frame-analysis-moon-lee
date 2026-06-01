import pandas as pd
import sys

def remove_duplicates(input_file, output_file):
    # Read CSV
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df_cleaned = df.drop_duplicates()

    # Save cleaned CSV
    df_cleaned.to_csv(output_file, index=False)

    print(f"Duplicates removed. Clean file saved to: {output_file}")
    print(f"Original rows: {len(df)}")
    print(f"Cleaned rows: {len(df_cleaned)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicates.py input.csv output.csv")
    else:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        remove_duplicates(input_csv, output_csv)