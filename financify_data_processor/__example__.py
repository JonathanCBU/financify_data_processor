"""Set up and print out the example DB"""

import argparse
import os
import random
import sqlite3
from typing import List, Tuple


def main() -> None:
    """Build an example DB and write in data"""
    args = get_args()
    db_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_db")
    if not os.path.exists(db_loc):
        print(f"Creating database directory {db_loc}")
        os.makedirs(db_loc)
    conn = sqlite3.connect(os.path.join(db_loc, "example.db"))
    cursor = conn.cursor()

    # clear existing table
    cursor.execute(f"DROP TABLE IF EXISTS {args.table}")

    # make a table if it isn't there
    cursor.execute(
        " ".join(
            [
                "CREATE TABLE",
                args.table,
                "(date not null, type not null, amount not null,",
                "unique (date, type, amount))",
            ]
        )
    )

    # get some random values
    statements: List[Tuple[str, str, float]] = []
    for month in range(1, args.num_months + 1):
        for asset_type in ["liquid", "investements", "debts"]:
            statements.append(
                (
                    f"2024-{month:02}-13",  # cool-ass way to pad numbers
                    asset_type,
                    round(random.uniform(10000, 50000), 2),
                )
            )

    # toss that data into your table
    cursor.executemany(
        f"INSERT INTO {args.table} (date, type, amount) VALUES(?, ?, ?)", statements
    )

    conn.commit()

    # print results
    for row in cursor.execute(f"SELECT * FROM {args.table} ORDER BY date"):
        print(row)


def get_args() -> argparse.Namespace:
    """Collect command line inputs"""
    parser = argparse.ArgumentParser(
        description="Command line arguments for the example database"
    )
    parser.add_argument(
        "--num_months",
        type=int,
        required=False,
        default=12,
        help="number of months to randomize data for",
    )

    parser.add_argument(
        "--table",
        type=str,
        required=False,
        default="statements",
        help="name of table to build example out of",
    )

    args = parser.parse_args()
    return args
