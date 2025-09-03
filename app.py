from transformers import pipeline
import gradio as gr

# Load the summarization model
model = pipeline("summarization")


# Define the prediction function
def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


# Set up the Gradio app
with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    output = gr.Textbox(label="Summary", lines=3)
    submit_button = gr.Button("Summarize")

    # submit_button.click(fn=predict, inputs=textbox, outputs=output)
    submit_button.click(
        fn=predict, inputs=textbox, outputs=output
    )  # pylint: disable=no-member


# Launch the app
demo.launch()