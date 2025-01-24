chunks = []

import json

with open('semantic_chunks.json', 'r') as file:
    data = json.load(file)

# Extract content and append to a list
chunks = [item for item in data.values()]
chunks_1 = [item for item in chunks if len(item.split())<15]
print(len(chunks_1))
numbers=[len(item.split()) for item in chunks]

less_than_50 = sum(1 for x in numbers if x < 10)


# Print results
print("Less than 50:", less_than_50)


print(chunks_1)