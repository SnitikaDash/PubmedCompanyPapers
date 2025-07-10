import argparse
from get_papers.pubmed_api import fetch_pubmed
from get_papers.filters import is_company_affiliation
from get_papers.csv_writer import write_to_csv

def extract_affiliations(pubmed_data):
    results = []
    for article in pubmed_data:
        try:
            article_info = article['PubmedArticle'][0]['MedlineCitation']
            pmid = article_info['PMID']
            title = article_info['Article']['ArticleTitle']
            pub_date = article_info['Article']['Journal']['JournalIssue']['PubDate']
            pub_date_str = " ".join([v for v in pub_date.values()])

            authors = article_info['Article'].get('AuthorList', [])
            non_academic_authors = []
            company_affiliations = []
            email = ""

            for author in authors:
                affiliation_info = author.get('AffiliationInfo', [])
                for aff in affiliation_info:
                    affiliation = aff.get('Affiliation', '')
                    if is_company_affiliation(affiliation):
                        name = author.get('ForeName', '') + " " + author.get('LastName', '')
                        non_academic_authors.append(name.strip())
                        company_affiliations.append(affiliation)
                        if "@" in affiliation and not email:
                            email = affiliation.split()[-1]

            if non_academic_authors:
                results.append({
                    "PubmedID": str(pmid),
                    "Title": title,
                    "Publication Date": pub_date_str,
                    "Non-academic Author(s)": "; ".join(non_academic_authors),
                    "Company Affiliation(s)": "; ".join(company_affiliations),
                    "Corresponding Author Email": email
                })
        except Exception as e:
            continue
    return results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with company-affiliated authors")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file")

    args = parser.parse_args()

    if args.debug:
        print(f"Query: {args.query}")
        if args.file:
            print(f"Results will be saved to: {args.file}")

    pubmed_data = fetch_pubmed(args.query)
    results = extract_affiliations(pubmed_data)

    if args.file:
        write_to_csv(results, args.file)
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()
