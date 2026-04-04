'''
Author: Armand Meijers
Date: 03/04/2026
Description: main file that puts all fucntions toegther to run full pipeline
'''


from src import chunking, embedding


import json, os

def main():
    #ensures paths exist
    DOCUMENT_PATH = "data/raw/papers/"
    os.makedirs(os.path.dirname(DOCUMENT_PATH), exist_ok=True)

    METADATA_PATH = "data/processed/metadata/"
    os.makedirs(os.path.dirname(METADATA_PATH), exist_ok=True)

    METADATA_JSON_PATH = "data/processed/metadata/chunk_metadata.json"

    #run pdf chunking of all pdf files in doc path and save metadata to json 
    #chunk_metadata = chunking.chunking_files_pdf(DOCUMENT_PATH)
    #if chunk_metadata == 0:
    #    return 0
    
    #with open(METADATA_JSON_PATH, "w", encoding="utf-8") as f:
    #    json.dump(chunk_metadata, f, indent=2, ensure_ascii=False)
        
    #embeddingLoc = embedding.embedding_text(METADATA_JSON_PATH)

    import faiss

    index = faiss.read_index("data/processed/vector_DB/index.faiss")

    print("Vectors:", index.ntotal)
    print("Dimensions:", index.d)

    for i in range(5):
        print(index.reconstruct(i))


if __name__ == "__main__":
    main()