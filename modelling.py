from transformers import Gemma3ForConditionalGeneration,Gemma3Processor,TextIteratorStreamer
import threading
import pdf2image
import torch

class Model:
    def __init__(self,model_path:str,device:str):
        self.processor = Gemma3Processor.from_pretrained(model_path,local_files_only=True)
        self.model = Gemma3ForConditionalGeneration.from_pretrained(model_path,local_files_only=True).to(device).eval()
        self.streamer = TextIteratorStreamer(tokenizer=self.processor,skip_prompt=True,skip_special_tokens=True)
        
    def __call__(self,pdf_input,user_prompt):
        images = pdf2image.convert_from_bytes(pdf_input,dpi=150)
        images = images[:5]
        preview_image = images[0]
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are an assistant who gives feedback about users resumes."}]
            },
            {
                "role": "user",
                "content": [{"type": "image", "image": img} for img in images] + [{"type": "text", "text": user_prompt}]
            }
        ]
        inputs = self.processor.apply_chat_template(messages,add_generation_prompt=True,tokenize=True,return_dict=True,return_tensors="pt").to(self.model.device,dtype=torch.bfloat16)
        streamer = TextIteratorStreamer(self.processor.tokenizer, skip_prompt=True, skip_special_tokens=True)
        generation_kwargs = dict(
            **inputs,
            streamer=streamer,
            max_new_tokens=1024,
            do_sample=False,
        )
        thread = threading.Thread(target=self.model.generate, kwargs=generation_kwargs)
        thread.start()
        partial_output = ""
        for new_text in streamer:
            partial_output += new_text
            yield preview_image, partial_output
