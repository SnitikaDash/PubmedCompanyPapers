from typing import List

COMPANY_KEYWORDS = [
    'pharma', 'biotech', 'inc', 'ltd', 'corp', 'gmbh',
    'company', 'therapeutics', 'laboratories', 'biosciences'
]

def is_company_affiliation(affiliation: str) -> bool:
    return any(word.lower() in affiliation.lower() for word in COMPANY_KEYWORDS)
