import pandas as pd

# List of files to process
files = [
    ("SP100_vol.csv", "SP100_vol_ffill.csv"),
    ("SP100_return.csv", "SP100_return_ffill.csv")
]

def replace_zeros_with_ffill(input_file, output_file):
    print(f"Processing {input_file}...")
    # Read CSV
    df = pd.read_csv(input_file)
    # Replace 0 with NaN
    df_replaced = df.replace(0, pd.NA)
    # Forward fill
    df_filled = df_replaced.ffill()
    # Optionally, if you want to keep original 0s at the start, you can backfill those
    df_filled = df_filled.bfill()
    # Save to new file
    df_filled.to_csv(output_file, index=False)
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    for infile, outfile in files:
        replace_zeros_with_ffill(infile, outfile) 