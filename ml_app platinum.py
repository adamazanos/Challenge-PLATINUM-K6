import re
import gradio as gr

def data_processing(text):
    return re.sub(r'[^a-zA-Z0-9]',' ', text)

gradio_ui = gr.Interface(
    fn=data_processing,
    title="Data Processing and Modeling Platinum",
    description="Aplikasi Web Data Processing dan Modeling Platinum",
    inputs=[gr.inputs.Textbox(lines=10, label="Paste some text here"), "file"],
    outputs=[gr.outputs.Textbox(label="Result")],
    allow_flagging='manual')

gradio_ui.launch()