import matplotlib.pyplot as plt

# Model names and accuracy data for each chunking type
models = ['llama-3.1-70b', 'gemini', 'gemma', 'Mixtral 7B']
accuracies = {
    'Few-shot Prompting': [0.720, 0.592, 0.580, 0.641],
    'Zero-shot Prompting': [0.720, 0.592, 0.575, 0.635],
    'Fixed Size Chunking': [0.706, 0.580, 0.572, 0.636],
    'Recursive Chunking': [0.724, 0.604, 0.579, 0.641],
    'Semantic Chunking': [0.741, 0.616, 0.591, 0.661]
}

# Generate a separate plot for each chunking type
for chunking_type, data in accuracies.items():
    plt.figure(figsize=(8, 6))
    plt.bar(models, data, color=['#4C72B0', '#55A868', '#C44E52', '#8172B2'])
    plt.title(f"Accuracy for {chunking_type}")
    plt.ylim(0.5, 0.8)
    plt.ylabel("Accuracy")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add data labels on each bar
    for i, v in enumerate(data):
        plt.text(i, v + 0.005, f"{v:.3f}", ha='center', fontsize=10)
    
    plt.show()
