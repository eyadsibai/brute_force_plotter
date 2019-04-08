import pandas as pd


def plot_feature(
    train_df_path_in_parquet,
    feature_name,
    target_column=None,
    test_df_path_in_parquet=None,
):
    train_df = pd.read_parquet(train)
