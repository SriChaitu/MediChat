import os

folder_path = 'en'
chunks = []
extra_chunk=''

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            paragraphs = text.split('\n\n')
            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                if len(extra_chunk)>200:
                    chunks.append(extra_chunk)
                    extra_chunk=''
                if len(paragraph)>200:
                    chunks.append(extra_chunk+paragraph)
                    extra_chunk=''
                else:
                    extra_chunk=extra_chunk+paragraph


for i, chunk in enumerate(chunks[:5]):
    print(f"Chunk {i+1}:\n{chunk}\n")

print(len(chunks))

import chromadb
def create_chroma_db(documents, path, name):
    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.create_collection(name=name)

    for i, d in enumerate(documents):
        if i%100 == 0:
          print(i)
          print(d)
        db.add(documents=d, ids=str(i))

    return db, name

db,name =create_chroma_db(documents=chunks, path="RAG4", name="collection_4")