from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))


from bootcamp_data.config import make_paths

from bootcamp_data.io import (
    read_orders_csv,
    read_users_csv,
    write_parquet,
)

from bootcamp_data.quality import (
    assert_in_range,
    assert_non_empty,
    require_columns,
)

from bootcamp_data.transforms import (
    add_missing_flags,
    apply_mapping,
    enforce_schema,
    missingness_report,
    normalize_text,
)

paths = make_paths(ROOT)

orders_raw = read_orders_csv(paths.raw / "orders.csv")
users_raw = read_users_csv(paths.raw / "users.csv")

require_columns(orders_raw, ["order_id", "user_id", "amount", "quantity", "created_at", "status"])
assert_non_empty(orders_raw, name="orders")
require_columns(users_raw, ["user_id", "country", "signup_date"])
assert_non_empty(users_raw, name="users")

orders_schema = enforce_schema(orders_raw)

rep = missingness_report(orders_schema)

paths.reports.parent.mkdir(parents=True, exist_ok=True)
rep.to_csv(paths.reports / "missingness_orders.csv", index=False)

status_norm = normalize_text(orders_schema["status"])
mapping = {
        "paid": "paid",
        "refund": "refund",
        "refunded": "refund",
}
status_clean = apply_mapping(status_norm, mapping)

orders_clean = (
    orders_schema
    .assign(status_clean=status_clean)
    .pipe(add_missing_flags, cols=["amount", "quantity"])
)

assert_in_range(orders_clean["amount"], lo=0, name="amount")

write_parquet(orders_clean, paths.processed / "orders_clean.parquet" )
write_parquet(users_raw, paths.processed / "users.parquet" )
