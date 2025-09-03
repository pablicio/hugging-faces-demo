from transformers import pipeline

# Modelos como BART já suportam summarization direto
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    framework="pt"
)

text = "Hugging Face mudou autenticação por senha para tokens ou SSH em 2023."
print(summarizer(text, max_length=50, min_length=10))
