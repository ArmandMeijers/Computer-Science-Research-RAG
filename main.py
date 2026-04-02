'''
Author: Armand Meijers
Date: 03/04/2026
Description: main file that puts all fucntions toegther to run full pipeline
'''


from src import Chunking
import json

def main():
    #file paths
    DOCUMENT_PATH = "data/raw/papers"
    METDATA_PATH = "data/processed/metadata/chunk_metadata.json"

    #run pdf chunking of all pdf files in doc path and save metadata to json 
    chunk_metadata = Chunking.chunking_files_pdf(DOCUMENT_PATH)
    with open(METDATA_PATH, "w", encoding="utf-8") as f:
        json.dump(chunk_metadata, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()