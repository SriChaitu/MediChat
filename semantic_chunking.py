
chunks = []

import json

with open('semantic_chunks.json', 'r') as file:
    data = json.load(file)

# Extract content and append to a list
chunks = [item for item in data.values()]

chunks_len=[len(item.split()) for item in chunks]

print(min(chunks_len))
print(max(chunks_len))

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

db,name =create_chroma_db(documents=chunks, path="RAG_S", name="collection_S")