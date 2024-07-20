import pandas as pd


def get_accuracy(test_df: pd.DataFrame, ans_df: pd.DataFrame) -> float:
    correct = 0

    if len(test_df) != len(ans_df):
        raise ValueError("2 dataframes not same length.")

    total_row = len(test_df)
    for row in range(total_row):
        actual = test_df.loc[row, "category"]
        predict = ans_df.loc[row, "category"]
        if actual == predict:
            correct += 1
    return correct / total_row