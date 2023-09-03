import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant for giving adivise to decide what study based on latest trends."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)