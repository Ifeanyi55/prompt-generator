from transformers import pipeline
import gradio as gr

def PromptGenerator(prompt):
  pipe = pipeline("text-generation", model="Gustavosta/MagicPrompt-Stable-Diffusion")

  prompt = pipe(prompt)

  prompt = prompt[0]

  prompt = prompt["generated_text"]

  return prompt

app = gr.Interface(PromptGenerator,
                   inputs = "text",
                   outputs = "text",
                   theme = gr.themes.Soft(primary_hue="blue",secondary_hue="stone"),
                   title = "AI Prompt Generator",
                   examples = ["Landscape of","Pixar style little girl","A racecar driving","Fireflies at night"],
                   css = ".gradio-container {background: url('file=/content/sample_data/boy 2.jpeg')}"
)

app.launch()
