'''
Author: Armand Meijers
Date: 02/04/2026
Description: Downloads a set of Comp Sci Research Papers from arxiv (https://arxiv.org) and stores in folder data/raw/papers
'''

#imports
import arxiv, json, os, time


MAX_PAPERS = 50
CATEGORIES = ["cs.LG","cs.AI","cs.CL","cs.CV"] #types of papers searched for.

metadata = []
CURRENT_PAPER = 1 #file index identifier

# folder to store papers
paper_path = "data/raw/papers/"
os.makedirs(os.path.dirname(paper_path), exist_ok=True)

#Dowloads n number of docs for each categorie states in the list
for category in CATEGORIES:
    query = f"cat:{category}"

    #searches arxiv database for n number of docs related to categirie
    search = arxiv.Search(
        query=query, 
        max_results=MAX_PAPERS,
        #https://arxiv.org
    )

    #for each result download document
    for paper in search.results():
        filename = f"paper{CURRENT_PAPER}-{category}.pdf"
        filepath = os.path.join(paper_path, filename)

        #checks if there are duplicate files
        if not os.path.exists(filepath):
            #error checking and logging.
            try:
                paper.download_pdf(dirpath=paper_path, filename=filename)

                metadata.append({
                    "filename": filename,
                    "title": paper.title,
                    "authors": [a.name for a in paper.authors],
                    "abstract": paper.summary,
                    "arxiv_id": paper.entry_id
                })

                print(f"[LOG] Downloaded {filename}")

            except Exception as e:
                print(f"[ERROR] Failed to download {filename}: {e}")
        
        CURRENT_PAPER += 1 
        time.sleep(1) #preventing excessive requests


#writes metaData into a json file
metadata_path = "data/processed/metadata/"
os.makedirs(os.path.dirname(metadata_path), exist_ok=True)

with open("data/processed/metadata/doc_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)
    print("[LOG] Saved metadata")