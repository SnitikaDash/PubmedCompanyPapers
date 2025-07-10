from typing import List, Dict, Any
from Bio import Entrez

Entrez.email = "snitikad@gmail.com" 

def fetch_pubmed(query: str, max_results: int = 20) -> List[Dict[str, Any]]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    papers = []
    for pid in ids:
        fetch = Entrez.efetch(db="pubmed", id=pid, retmode="xml")
        data = Entrez.read(fetch)
        papers.append(data)
    return papers
