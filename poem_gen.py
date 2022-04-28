import openai
import os
import sys
import shutil

def poem_gen(adj, noun):
  openai.api_key = os.environ.get("OPENAI_API_KEY")
  prompt_text = f"Write a {adj} free verse poem about {noun}."

  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    top_p=1,
    temperature=1,
    max_tokens=200,
    presence_penalty=1.5,
    frequency_penalty=1.5,
  )

  return response['choices'][0]['text']


def run_gen():
  file = open("prompts.txt", "r")

  if os.path.exists("output"):
    shutil.rmtree("output")
  os.mkdir("output")

  cur_line = 0

  for line in file:
    poem_args = [x.strip() for x in line.split(",")]
    text = poem_gen(poem_args[0], poem_args[1])
    text.strip()

    output = open(f"./output/poem{cur_line}.txt", "x")
    output.write(text)
    output.close()

    cur_line += 1

  file.close()


def main():
  run_gen()


if __name__ == '__main__':
  main()
