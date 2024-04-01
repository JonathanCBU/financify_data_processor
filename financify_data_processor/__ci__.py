"""CI entry points to be called in actions"""

import argparse
import re
from typing import Any, Dict

import toml

from financify_data_processor.library.exceptions import CiError


def main() -> None:
    """CI entry point"""
    args = get_args()

    with open(args.pyproject, "r", encoding="utf-8") as toml_file:
        pyproject = toml.load(toml_file)

    if args.tag:
        check_tag_update(args.tag, pyproject)


def check_tag_update(tag: str, toml_dict: Dict[str, Any]) -> None:
    """Confirm that version is updated in the toml file

    :param tag: expected tag
    :param toml_dict: pyproject.toml as a dict
    """
    tag_pattern = r"v(\d{,3}\.){2}.\d{,3}"
    version_tag = re.search(tag_pattern, tag)
    if not version_tag:
        raise CiError(f"Tag {tag} does not match pattern {tag_pattern}")

    new_tag = version_tag.group(0)
    if new_tag.lstrip("v") != toml_dict["tool"]["poetry"]["version"]:
        raise CiError(
            f"Tag {new_tag} does not match version {toml_dict['tool']['poetry']['version']}"
        )

    # print version_tag to stdout for use in github actions
    print(new_tag)


def get_args() -> argparse.Namespace:
    """Collect command line args for CI"""

    parser = argparse.ArgumentParser(description="Command line args for CI")
    parser.add_argument("--tag", help="Release tag branch name")
    parser.add_argument("--pyproject", required=True, help="Path to pyproject.toml")
    args = parser.parse_args()

    return args
