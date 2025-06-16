# app.py
import gradio as gr
from groq import Groq
from gtts import gTTS
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def initialize_messages():
    return [{"role": "system",
             "content": "You are a talented mythological storyteller. Tell short, engaging Indian mythology stories in a simple, emotional style. End every story with a moral."}]

messages_prmt = initialize_messages()

def generate_story(user_input):
    global messages_prmt

    try:
        messages_prmt.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            messages=messages_prmt,
            model="llama3-8b-8192",
        )
        story = response.choices[0].message.content
        messages_prmt.append({"role": "assistant", "content": story})

        # TTS generation
        audio_path = "story.mp3"
        try:
            tts = gTTS(story)
            tts.save(audio_path)
        except Exception as e:
            print("TTS Error:", e)
            audio_path = None

        return story, audio_path

    except Exception as e:
        return f"⚠️ Error: {str(e)}", None

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🕉️ Mythology Storyteller Bot
    _Ask for short Indian mythology stories and hear them come alive!_
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            user_input = gr.Textbox(
                label="Your Prompt",
                placeholder="e.g. Tell me a story about Krishna",
                lines=2
            )
            generate_btn = gr.Button("🪄 Generate Story")

        with gr.Column(scale=3):
            story_output = gr.Textbox(label="📜 Story", lines=8, interactive=False)
            audio_output = gr.Audio(label="🔊 Listen", autoplay=True)

    generate_btn.click(fn=generate_story, inputs=user_input, outputs=[story_output, audio_output])

app.launch()
