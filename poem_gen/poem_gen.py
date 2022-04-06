import openai
import os
import sys

def poem_gen(adj, noun):
  openai.api_key = os.environ.get("OPENAI_API_KEY")
  prompt_text = f"Write me a {adj} poem about {noun}\n"

  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.2,
    max_tokens=2000,
    presence_penalty=0.6,
  )

  return f"PROMPT: {prompt_text}\nOUTPUT: {response['choices'][0]['text']}\n\n"


def run_gen():
  file = open("prompts.txt", "r")

  if os.path.exists("output.txt"):
    os.remove("output.txt")
  output = open("output.txt", "x")

  for line in file:
    poem_args = [x.strip() for x in line.split(",")]
    text = poem_gen(poem_args[0], poem_args[1])
    output.write(text)

  file.close()
  output.close()


def main():
  run_gen()


if __name__ == '__main__':
  main()
