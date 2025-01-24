# MediChat - A RAG-based Health GPT  

MediChat is a specialized health chatbot that leverages advanced AI techniques to provide accurate and contextually relevant answers to medical questions. Built as part of a Bachelor’s Thesis Project, it incorporates Retrieval-Augmented Generation (RAG) with state-of-the-art language models like Gemini and LLaMA to enhance medical query handling.  

## Features  
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval mechanisms with generative AI for precise medical question answering.  
- **Advanced Prompting Techniques**: Utilizes zero-shot, few-shot, and RAG prompting strategies for diverse input scenarios.  
- **Data Processing**: Employs semantic and recursive chunking to handle large medical datasets efficiently.  
- **High Performance**: Optimized for clinical accuracy and practical usability.  

## Tech Stack  
- **Language Models**: Gemini, LLaMA  
- **Programming Languages**: Python  
- **Libraries and Frameworks**:  
  - `Hugging Face Transformers` for model integration  
  - `pandas` and `NumPy` for data manipulation  

## Dataset  
The project is built on the MedQA dataset, which includes extensive question-answer pairs from clinical and medical domains.  

## Implementation Details  
1. **Data Preprocessing**:  
   - Semantic and recursive chunking to split large text into manageable segments.  
   - Data cleaning and tokenization for model readiness.  

2. **Model Fine-tuning**:  
   - Zero-shot and few-shot prompting strategies implemented for baseline performance.  
   - RAG methodology applied to retrieve and generate relevant responses.  

3. **Evaluation**:  
   - Tested on clinical scenarios to ensure accuracy and reliability.  
   - Continuous evaluation using domain-specific metrics.  

