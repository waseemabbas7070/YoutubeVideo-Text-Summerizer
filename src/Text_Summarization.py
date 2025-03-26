groq_api = "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"
import os
from langchain.chat_models import init_chat_model

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = groq_api

class modelling:
    def __init__(self):
        self.model = init_chat_model("llama3-8b-8192", model_provider="groq")

    def split_text(self, text, max_tokens=5000):
        return [text[i:i + max_tokens] for i in range(0, len(text), max_tokens)]

    def model2(self, text):
        chunks = self.split_text(text)  
        summaries = []

        for chunk in chunks:
            message = self.model.invoke(f"Summarize this text: {chunk} in 50 to 200 words")
            summaries.append(message.content)

        final_summary = " ".join(summaries)  
        return final_summary
