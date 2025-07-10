import pandas as pd

files = [
    ("SP100_return_ffill.csv", "SP100 Return (Forward Fill)"),
    ("SP100_vol_ffill.csv", "SP100 Volatility (Forward Fill)")
]

def review_file(filename, label):
    print(f"\n--- {label} ---")
    df = pd.read_csv(filename)
    zero_count = (df == 0).sum().sum()
    nan_count = df.isna().sum().sum()
    print(f"Total zeros: {zero_count}")
    print(f"Total NaNs: {nan_count}")
    print("Summary statistics:")
    print(df.describe())

if __name__ == "__main__":
    for fname, label in files:
        review_file(fname, label) 