'''
Author: Armand Meijers
Date: 02/04/2026
Description: store functions for Chunking documents (pdf) NOTE: adding other file types later
'''

#imports
import os, pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunking_files_pdf(DOCUMENT_PATH):
    """
    Reads all PDFs in DOCUMENTS_PATH, splits pages into chunks,
    and returns a list of chunk objects with metadata.

    Returns:
        List[Dict]: Each dict has "text" and "metadata"  with valyes filename, page, chunk_index
    """


    #chunk tokens
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    #chunk arrays
    chunk_metadata = []
    
    #text splitter for chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP,
    )   

    for file in os.listdir(DOCUMENT_PATH):

        #checks if file is a pdf
        if not file.endswith(".pdf"):
            continue

        page_index = 0
        chunk_index = 0

        file_path = os.path.join(DOCUMENT_PATH, file)

        #error handling
        try:
            doc = pymupdf.open(file_path)
        except Exception as e:
            print(f"Skipping {file} Error: {e}")
            continue

        try:
            #loop through all pages in doc
            for page in doc:
                #checks if doc page has text (can have no text only images ect)
                page_text = page.get_text()
                page_index += 1

                if page_text.strip() == "":
                    continue

                #chunking of page
                chunks = text_splitter.split_text(page_text)

                #loops through each chunk
                for chunk in chunks:
                    chunk_index += 1
                    
                    #append metadata to array
                    chunk_metadata.append({
                        "text": chunk,
                        "metadata": {
                            "filename": file,
                            "page": page_index,
                            "chunk_index": chunk_index,
                        }
                    })

        #errpr handling
        except Exception as e:
            print(f"Error: {file}: {e}")

        finally:
            #close doc
            doc.close()

        
    return chunk_metadata
