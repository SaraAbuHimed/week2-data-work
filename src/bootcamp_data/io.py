
from pathlib import Path
import pandas as pd

# Values that should be treated as missing
NA = ["", "NA", "N/A", "null", "None"]


def read_orders_csv(path: Path) -> pd.DataFrame:
    """
    Read the orders CSV with consistent dtypes and NA handling.
    """
    return pd.read_csv(
        path,
        dtype={"order_id": "string", "user_id": "string"},
        na_values=NA,
        keep_default_na=True,
    )


def read_users_csv(path: Path) -> pd.DataFrame:
    """
    Read the users CSV with consistent dtypes and NA handling.
    """
    return pd.read_csv(
        path,
        dtype={"user_id": "string"},
        na_values=NA,
        keep_default_na=True,
    )


def write_parquet(df: pd.DataFrame, path: Path) -> None:
    """
    Write a DataFrame to Parquet, creating parent folders if needed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def read_parquet(path: Path) -> pd.DataFrame:
    """
    Read a Parquet file into a DataFrame.
    """
    return pd.read_parquet(path)
