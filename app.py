from modelling import Model
import gradio as gr

model = Model(model_path="model",device="cuda")

with gr.Blocks(title="Resume Insights") as demo:
    gr.Markdown("## 🧠 Resume Analyzing Tool (With Gemma 3)\nFirst 5 pages of resume you uploaded will be analyzed.")

    with gr.Row():
        pdf_input = gr.File(type="binary", label="📄 Upload PDF.")
        user_prompt = gr.Textbox(label="🤔 What would you like to ask?", value="Could you give me a feedback about this resume?")

    with gr.Row():
        image_output = gr.Image(label="📸 First Page Screenshot",container=True,scale=True)
        text_output = gr.Markdown(label="🧾 Model's response.")

    analyze_btn = gr.Button("🔍 Analiz Et")

    analyze_btn.click(fn=model.__call__, 
                      inputs=[pdf_input, user_prompt], 
                      outputs=[image_output, text_output])
    
if __name__ == "__main__":
    demo.launch()