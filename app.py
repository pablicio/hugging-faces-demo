from transformers import pipeline

# Usa PyTorch ao invés de TensorFlow
summarizer = pipeline(
    "summarization",
    model="google-t5/t5-small",
    framework="pt"  # força PyTorch
)

text = "O Hugging Face trocou autenticação por senha para tokens ou SSH em 2023."
print(summarizer(text, max_length=40, min_length=10, do_sample=False))
