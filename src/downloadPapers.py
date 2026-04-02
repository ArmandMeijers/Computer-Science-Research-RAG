'''
Author: Armand Meijers
Date: 02/04/2026
Description: Downloads a set of Comp Sci Research Papers from arxiv and stores in folder data/raw/papers
'''

#imports
import arxiv, json, os, time


# folder to store papers
folder = "data/raw/papers"
os.makedirs(folder, exist_ok=True)

CURRENT_PAPER = 1 #file index identifier
MAX_PAPERS = 25

CATEGORIES = ["cs.LG","cs.AI","cs.CL","cs.CV"] #types of papers searched for.
metadata = []

#Dowloads n number of docs for each categorie states in the list
for category in CATEGORIES:
    query = f"cat:{category}"

    #searches arxiv database for n number of docs related to categirie
    search = arxiv.Search(
        query=query, 
        max_results=MAX_PAPERS,
    )

    #for each result download document
    for paper in search.results():
        filename = f"paper{CURRENT_PAPER}-{category}.pdf"
        filepath = os.path.join(folder, filename)

        #checks if there are duplicate files
        if not os.path.exists(filepath):
            #error checking and logging.
            try:
                paper.download_pdf(dirpath=folder, filename=filename)

                metadata.append({
                    "filename": filename,
                    "title": paper.title,
                    "authors": [a.name for a in paper.authors],
                    "abstract": paper.summary,
                    "arxiv_id": paper.entry_id
                })

                print(f"Downloaded {filename}")

            except Exception as e:
                print(f"Failed to download {filename}: {e}")
        
        CURRENT_PAPER += 1 
        time.sleep(1) #preventing excessive requests

with open("data/raw/papers/metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)