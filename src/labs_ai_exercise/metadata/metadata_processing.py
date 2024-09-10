from __future__ import annotations

from datetime import datetime


def extract_year(publication_date: str) -> int:
    """Extracts the year from the publication date."""
    try:
        return datetime.strptime(publication_date, "%Y-%m-%d").year
    except ValueError:
        print("Date format should be YYYY-MM-DD")
        return None


def validate_metadata(title: str, authors: list[str], journal: str, date: str) -> bool:
    """Checks to see if all metadata fields are present."""
    return all([title, authors, journal, date])


def parse_author_name(full_name: str) -> dict[str, str]:
    """Parses the authors name into a structure."""
    names = full_name.split(" ")
    if len(names) < 2:
        raise ValueError("Full name must include at least a first name and a last name")
    return {"first_name": names[0], "last_name": names[-1]}
