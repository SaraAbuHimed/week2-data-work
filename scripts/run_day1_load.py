from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv
from bootcamp_data.io import read_users_csv
from bootcamp_data.transforms import enforce_schema
from bootcamp_data.io import write_parquet

paths = make_paths(ROOT)

orders = read_orders_csv(paths.raw / "orders.csv")
users = read_users_csv(paths.raw / "users.csv")

orders_schema = enforce_schema(orders)

orders_write = write_parquet(orders_schema, paths.processed / "orders.parquet")
users_write = write_parquet(users, paths.processed / "users.parquet")