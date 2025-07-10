import csv
from typing import List, Dict

def write_to_csv(results: List[Dict], filename: str):
    if not results:
        print("No results to write.")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
