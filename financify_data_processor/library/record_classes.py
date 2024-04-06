"""Data class definitions for each table"""

from dataclasses import dataclass


@dataclass
class Statements:
    """Statement record data type"""

    date: str
    value: float
    asset_type: str
