import pandas as pd
import re

def extract_answer_from_response(response_text):

    # Use a regex to find the answer pattern "ANS: <answer>" where <answer> is a letter (A, B, C, or D)
    response_text=str(response_text)

    match = re.search(':\s([A-Z])', response_text)

    if(match):
        try:
            return match.group(1)
        except:
            return 'nan'
        
    match = response_text.strip()

    if(len(match)==1):

        return match
    try:
        match = response_text.split()[1]
    except:
       match='nan'
    
    if(len(match)==1):
        return match



    match = re.search(r'\*\*(\w)', response_text)

    if(match):

        return match.group(1)

    match = re.search(r'\*\*(\w)\)', response_text)

    return match.group(1) if match else "None"

filtered_df=pd.read_csv('Predicted_Table4_RAG.csv')
filtered_df.fillna('nan')
# filtered_df=filtered_df.iloc[:185]
filtered_df['predicted_extracted_answer'] = filtered_df['predicted_answer'].apply(lambda x: extract_answer_from_response(x))
def calculate_accuracy(df):

  correct_count = 0

  total_count = len(df)

  for _, row in df.iterrows():

    if(row['predicted_extracted_answer'].strip()==row['answer_idx'].strip()):

      correct_count += 1

  accuracy = correct_count / total_count

  return accuracy

print(calculate_accuracy(filtered_df))

filtered_df.to_csv('Predicted_Table4_RAG1.csv') 