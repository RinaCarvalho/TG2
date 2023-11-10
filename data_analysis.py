import pandas as pd
import numpy as np

def pass_at_k(n, c, k):
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))


def calculate_pass_at_k(k):
    csv_file = "result_compilation.csv"
    df = pd.read_csv(csv_file)

    # number of samples for each problem, model and prompt
    n = 10

    pass_at_k_df = df.copy()

    # Iterate over the columns and rows to calculate pass@k for each cell
    for column in df.columns[1:]:
        for row in df.index:
            cell_value = df.at[row, column]
            if cell_value != "-":
                c = int(cell_value)
                pass_k = pass_at_k(n, c, k)
                pass_at_k_df.at[row, column] = pass_k

    # Save the new DataFrame with pass@k values to a new CSV file
    pass_at_k_csv_file = f"pass_at_{k}.csv"
    pass_at_k_df.to_csv(pass_at_k_csv_file, index=False)

    print(f"Pass@{k} values have been calculated and saved to {pass_at_k_csv_file}.")


def success_rate(c, n):
    return c/n

def extract_success_rate_by_model(model):
    c = 0
    n = 0

    csv_file = "result_compilation.csv"
    df = pd.read_csv(csv_file)

    for column in df.columns[1:]:
        if model in column:
            for row in df.index:
                cell_value = df.at[row, column]
                if cell_value != "-":
                    c += int(cell_value)
                    n += 10

    return c / n

def average_pass_at_k_by_model(k, model):
    csv_file = f"consolidated_pass_at_{k}.csv"
    df = pd.read_csv(csv_file)
    cols = []

    for column in df.columns[1:]:
        if model in column:
            cols.append(column)

    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
    stacked_cols = df[cols].stack()

    return stacked_cols.mean()


def average_pass_at_k_by_prompt_series(k, prompt_series=None):
    csv_file = f"consolidated_pass_at_{k}.csv"
    df = pd.read_csv(csv_file)

    cols = df[df.columns[1:]].apply(pd.to_numeric, errors='coerce')
    avg = cols.mean()

    if prompt_series:
        return avg[prompt_series]
    
    return avg
