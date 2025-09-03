from transformers import pipeline
import gradio as gr

# Inicializa o pipeline T5 para summarization (text2text-generation)
summarizer = pipeline(
    "text2text-generation",
    model="google-t5/t5-small",
    framework="pt"  # força PyTorch
)

def summarize(text):
    # Prefixo 'summarize:' instrui T5 a resumir
    result = summarizer(f"summarize: {text}", max_length=50, min_length=10)
    return result[0]['generated_text']

# Interface Gradio
iface = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=5, placeholder="Cole seu texto aqui..."),
    outputs=gr.Textbox(label="Resumo"),
    title="Resumo de Texto com T5",
    description="Digite ou cole um texto e receba um resumo curto usando T5 (PyTorch)."
)

if __name__ == "__main__":
    iface.launch()
