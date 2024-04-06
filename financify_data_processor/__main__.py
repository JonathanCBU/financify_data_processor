"""Main PDF parsing pipeline"""

import os
import re
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from pypdf import PdfReader

from financify_data_processor.config import mysql_cfg
from financify_data_processor.library.exceptions import ParsingException
from financify_data_processor.library.record_classes import Statements


def main() -> None:
    """Parse statement PDFs"""

    load_dotenv()
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_db"))
    records: List[Statements] = []
    for doc in os.listdir(os.environ["STATEMENTS"]):
        if doc.endswith(".pdf"):
            reader = PdfReader(os.path.join(os.environ["STATEMENTS"], doc))
            front_page = reader.pages[0].extract_text().replace(",", "")
            if os.environ["BANK_ID"] in front_page.upper():
                statement_type = "LIQUID"
                date_fmt = mysql_cfg.date_fmt_short
            elif os.environ["BROKER_ID"] in front_page.upper():
                statement_type = "INVESTMENT"
                date_fmt = mysql_cfg.date_fmt_long
            elif os.environ["LENDER_ID_1"] in front_page.upper():
                statement_type = "LOANS_1"
                date_fmt = mysql_cfg.date_fmt_nums
            elif os.environ["LENDER_ID_2"] in front_page.upper():
                statement_type = "LOANS_2"
                date_fmt = mysql_cfg.date_fmt_nums
            val = re.search(mysql_cfg.info_patterns[statement_type]["val"], front_page)
            date = re.search(
                mysql_cfg.info_patterns[statement_type]["date"], front_page
            )
            if val is None or date is None:
                raise ParsingException(f"Regex failure parsing {statement_type}")
            if date_fmt == mysql_cfg.date_fmt_short:
                date_info = f"{date.group(1)} {datetime.now().year}"
            else:
                date_info = date.group(1)
            records.append(
                Statements(
                    date=datetime.strptime(date_info, date_fmt).strftime("%Y-%m-%d"),
                    value=float(val.group(1)),
                    asset_type=statement_type,
                )
            )
    net_worth: float = 0
    for rec in records:
        print(rec)
        print(f"{rec.asset_type}: ${rec.value}")
        if rec.asset_type in ["LOANS_1", "LOANS_2"]:
            net_worth -= rec.value
        else:
            net_worth += rec.value
    print(f"NET WORTH: ${net_worth}")
