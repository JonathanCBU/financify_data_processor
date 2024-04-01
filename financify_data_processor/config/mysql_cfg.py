date_fmt_short = "%b %d %Y"
date_fmt_long = "%B %d %Y"
date_fmt_nums = "%m/%d/%y"
info_patterns = {
    "LIQUID": {
        "val": r"\$(\d{1,9}\.\d{2})TOTAL ENDING BALANCE",
        "date": r"ACCOUNT NAME [A-Za-z]{3} \d{1,2} ([A-Za-z]{3} \d{1,2})",
    },
    "INVESTMENT": {
        "val": r"Your Portfolio Value: \$(\d{1,9}\.\d{2})",
        "date": r"[A-Za-z]{3,9} \d{1,2} \d{4} - ([A-Za-z]{3,9} \d{1,2} \d{4})",
    },
    "LOANS_1": {
        "val": r"Unpaid Principal \$(\d{1,9}\.\d{2})",
        "date": r"\d{2}/\d{2}/\d{2} to (\d{2}/\d{2}/\d{2})",
    },
    "LOANS_2": {
        "val": r"Current Balance \$(\d{1,9}\.\d{2})",
        "date": r"Loan Information as of (\d{2}/\d{2}/\d{2})",
    },
}
