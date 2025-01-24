from Bio import Entrez
import json

def pubmed(output_json_file, start_date, end_date, max_num_articles):
    Entrez.email = 'srichaitanyakattamuri2601@gmail.com'
    query = f"Mental Health, ({start_date}[Date - Publication] : {end_date}[Date - Publication])"
    ID_results = Entrez.read(Entrez.esearch(db='pubmed', sort='relevance', retmax=max_num_articles, retmode='xml', term=query))
    id_list = ID_results['IdList']
    print(id_list)
    ids = ','.join(id_list)
    papers = Entrez.read(Entrez.efetch(db='pubmed', retmode='xml', id=ids))
    result = {}

    for i, paper in enumerate(papers['PubmedArticle']):
        article = paper['MedlineCitation']['Article']
        abstract = article.get('Abstract')
        if abstract:
            result[i] = {"article_title": article['ArticleTitle'],"article_abstract": abstract['AbstractText'][0]}
            
    with open(output_json_file, 'w') as f:
        f.write(json.dumps(list(result.values())))
        

if __name__ == "__main__":
    # max_articles=input('Enter the maximum number of Articles: ')
    # start_date=input('Enter the Start Date: ')
    # end_date=input('Enter the End Date: ')
    pubmed('D:\Codes\BTP\pubmed.json', '2021/01/01', '2024/06/06', 50000)