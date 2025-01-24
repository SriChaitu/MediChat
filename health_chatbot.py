import google.generativeai as palm
import chromadb
from groq import Groq

palm.configure(api_key='AIzaSyAIHxQwpth7S_xTpf7yUhmvp3ZmCkxUsto')

chroma_client = chromadb.PersistentClient(path="RAG_S")
db = chroma_client.get_collection(name="collection_S")
client= Groq(api_key='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')
# anatomy_text_example = db.query(query_texts=["What is Vasectomy"], n_results=5)['documents'][0]
# print(anatomy_text_example[0])

# model = palm.GenerativeModel('gemini-1.5-flash')
model2= palm.GenerativeModel('gemini-1.5-pro')
model = 'llama-3.1-70b-versatile'
def generate_answer(db,query):

    # chat = model.start_chat(
    # history=[]
    # )   

    obtained_chunks = db.query(query_texts=[query], n_results=2)['documents'][0]
    merged_chunk ="".join(obtained_chunks)
    merged_chunk = merged_chunk.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""You are a medical assistant bot. End yuor sentence with 'Stay healthy!!' You need to answer the following question using text from the reference passage which is given below the question, just use the information from the passage and summarize in your own words, dont use sentences like 'This passage tells that'
                QUESTION: '{query}' 
                PASSAGE: '{merged_chunk}'
                Here is the example to the question and the way you should answer:
                Question: Hi, I'm feeling pain in my muscles after I worked out, can u please tell me if it is ok?
                Answer: It is perfectly fine to fell the pain in muscles since, workout session usually leads to micro tears in muscles. Hope this helps, ask me anything if you need. Stay Healthy!!
                If you find the passage irrelevant to the question asked, then answer to the best of your knowledge. You are a health professional and you should not tell to consult another doctor at any cost.
    """).format(query=query, merged_chunk=merged_chunk)
    # print(merged_chunk)
    # answer = chat.send_message(prompt)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=0.0,
    )

    answer = chat_completion.choices[0].message.content
    prompt2 ="""Given a paragraph, your aim is to remove the sentences like 'Consult a doctor', 'Go to healthcare professional' and return the remaining paragraph PARAGRAPH:{} """.format(answer)
    answer2 = model2.generate_content(prompt2)
    return answer2.text


while(True):
    question = input('User: ')
    if question == 'q':
        break
    print('HealthBot: ',generate_answer(db,question))
