# ================================
# BERT Language Model Full Project
# ================================

# Install required libraries (run once)
# !pip install transformers torch matplotlib seaborn scikit-learn

import torch
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import BertTokenizer, BertModel
from torch.nn.functional import cosine_similarity

# -------------------------------
# Load Tokenizer and Model
# -------------------------------
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

print("BERT model loaded successfully")

# -------------------------------
# Sample Text Input
# -------------------------------
text = "Artificial Intelligence is transforming the world of technology."

# Tokenization
tokens = tokenizer.tokenize(text)
inputs = tokenizer(text, return_tensors="pt")

print("\nTokens:")
print(tokens)

# -------------------------------
# Forward Pass Through Model
# -------------------------------
with torch.no_grad():
    outputs = model(**inputs)

last_hidden_states = outputs.last_hidden_state
print("\nHidden State Shape:", last_hidden_states.shape)

# -------------------------------
# Sentence Embedding
# -------------------------------
sentence_embedding = last_hidden_states.mean(dim=1)
print("Sentence Embedding Shape:", sentence_embedding.shape)

# -------------------------------
# Contextual Understanding Test
# -------------------------------
print("\nContextual Understanding Test:")
sentences = [
    "I went to the bank to deposit money.",
    "I sat near the river bank."
]

for sentence in sentences:
    encoded = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        output = model(**encoded)
    embedding = output.last_hidden_state.mean(dim=1)
    print(f"Sentence: {sentence}")
    print(f"Embedding Mean Value: {embedding.mean().item()}")
    print("-" * 50)

# -------------------------------
# Sentence Similarity Analysis
# -------------------------------
sentence1 = "Machine learning is fascinating."
sentence2 = "AI and ML are exciting fields."
sentence3 = "The weather is very hot today."

def get_embedding(sentence):
    encoded = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        output = model(**encoded)
    return output.last_hidden_state.mean(dim=1)

embed1 = get_embedding(sentence1)
embed2 = get_embedding(sentence2)
embed3 = get_embedding(sentence3)

sim_1_2 = cosine_similarity(embed1, embed2).item()
sim_1_3 = cosine_similarity(embed1, embed3).item()

print("\nSentence Similarity Scores:")
print(f"Similarity (Sentence 1 & 2): {sim_1_2}")
print(f"Similarity (Sentence 1 & 3): {sim_1_3}")

# -------------------------------
# Batch Processing Multiple Sentences
# -------------------------------
texts = [
    "Natural Language Processing is powerful.",
    "Deep learning models understand text.",
    "BERT is widely used in NLP applications."
]

batch_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    batch_outputs = model(**batch_inputs)

batch_embeddings = batch_outputs.last_hidden_state.mean(dim=1)
print("\nBatch Embedding Shape:", batch_embeddings.shape)

# -------------------------------
# Visualization of Token Embeddings
# -------------------------------
token_embeddings = last_hidden_states[0][:len(tokens)].detach().numpy()

plt.figure(figsize=(12, 6))
sns.heatmap(token_embeddings, cmap="viridis")
plt.title("BERT Token Embedding Heatmap")
plt.xlabel("Embedding Dimensions")
plt.ylabel("Tokens")
plt.show()

# -------------------------------
# Save and Load Embeddings
# -------------------------------
torch.save(sentence_embedding, "bert_sentence_embedding.pt")
loaded_embedding = torch.load("bert_sentence_embedding.pt")

print("\nSaved and Loaded Embedding Shape:", loaded_embedding.shape)

# -------------------------------
# Model Status
# -------------------------------
print("\nModel Evaluation Mode:", not model.training)

print("\nBERT Language Model Analysis Completed Successfully")