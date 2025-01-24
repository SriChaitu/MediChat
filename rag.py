import google.generativeai as palm
import chromadb
import pandas as pd
import json
from time import sleep
from groq import Groq

palm.configure(api_key=YOUR_KEY)

client= Groq(api_key=YOUR_KEY)

chroma_client = chromadb.PersistentClient(path="RAG_S")
db = chroma_client.get_collection(name="collection_S")

# anatomy_text_example = db.query(query_texts=["Cervical cancer"], n_results=3)['documents'][0]
# print(anatomy_text_example[0])

model = palm.GenerativeModel('gemini-1.5-flash')
# model = 'llama-3.1-70b-versatile'
# model = 'llama-3.1-8b-instant'
# model = 'mixtral-8x7b-32768'

def generate_answer(db,df):
    responses=[]
    for i, row in df.iterrows():
        query= row['question']
        obtained_chunks = db.query(query_texts=[query], n_results=1)['documents'][0]
        merged_chunk ="".join(obtained_chunks)
        merged_chunk = merged_chunk.replace("'", "").replace('"', "").replace("\n", " ")
        prompt = ("""You are a medical assistant bot. You need to answer the following MCQ question with multiple options 
                QUESTION: '{query}' using text from the reference passage included below.
                PASSAGE: '{merged_chunk}'
                If you find the passage irrelevant to the question asked, then answer to the best of your knowledge.
                Choose the correct answer and respond in the following format:
                Answer: Then provide the correct option (e.g., A, B, C, D or E).
                Do not add any extra sentences or explanations.
        """).format(query=query,merged_chunk='')

        try:
            # chat_completion = client.chat.completions.create(
            #     messages=[
            #         {
            #             "role": "user",
            #             "content": prompt,
            #         }
            #     ],
            #     model=model,
            #     temperature=0.0,
            # )

            # answer = chat_completion.choices[0].message.content
            answer = model.generate_content(prompt).text
            print(i)
            # responses.append(answer.text)
            responses.append(answer)
            # print(merged_chunk)
            print(answer)
        except Exception as e:
            print("The error is: ",e)
            responses.append('nan')
        if i%14 ==0:
            sleep(61)
    return responses

size = 850

df = pd.read_json('test.jsonl', lines=True)

filtered_df = df[['question','options','answer_idx']]

filtered_df['options'] = filtered_df['options'].apply(lambda x: json.dumps(x))

# Create a new 'question' column by concatenating 'question' with 'options'

filtered_df['question'] = filtered_df['question'] + ' options: ' + filtered_df['options']

filtered_df = filtered_df.drop(columns=['options'])

filtered_df = filtered_df.iloc[800:size,:]

print(filtered_df.head(10))

filtered_df['predicted_answer'] = generate_answer(db,filtered_df)

final_df= filtered_df

final_df.to_csv("Predicted_Table4_RAG.csv")
