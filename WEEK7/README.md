# Week 7 – Next Token Prediction Using DistilGPT2

## 📌 Project Overview
This project demonstrates how a Generative Pre-trained Transformer (GPT) predicts the next token in a given text prompt using the DistilGPT2 language model.

It uses Hugging Face Transformers and PyTorch to perform a forward pass and calculate the probability of the next possible tokens.

## 🎯 Objectives
- Load a pre-trained DistilGPT2 model.
- Understand tokenization and token IDs.
- Perform a forward pass using the language model.
- Calculate next-token probabilities using Softmax.
- Identify the Top-K most probable next tokens.
- Compare predictions for factual and creative prompts.

## 🛠️ Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- DistilGPT2
- Google Colab / Jupyter Notebook

## 📂 Project Structure

```text
Week7/
│
├── week7_colab.ipynb
└── README.md
```

## 📦 Installation

Install the required libraries:

```bash
pip install transformers torch
```

## 🚀 How to Run

1. Open the `week7_colab.ipynb` notebook in Google Colab or Jupyter Notebook.
2. Install the required libraries.
3. Import PyTorch and Hugging Face Transformers.
4. Load the DistilGPT2 tokenizer and model.
5. Execute the `inspect_next_tokens()` function.
6. Provide a text prompt.
7. Observe the Top-K predicted tokens, their token IDs, raw logits, and probabilities.

## 🧠 Implementation Details

### 1. Load the Model
Loads the pre-trained DistilGPT2 model and tokenizer.

### 2. Tokenization
Converts the input text into token IDs.

### 3. Forward Pass
Passes the input tokens through the model to obtain logits.

### 4. Softmax
Converts raw logits into probability values.

### 5. Top-K Prediction
Selects and displays the most probable next tokens.

## 📝 Sample Experiments

**Experiment 1:**

Prompt:
`The capital of France is`

Finds the Top-10 probable next tokens.

**Experiment 2:**

Prompt:
`Water boils at 100 degrees`

Finds the Top-5 probable next tokens.

**Experiment 3:**

Prompt:
`Once upon
