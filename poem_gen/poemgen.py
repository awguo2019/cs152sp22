import openai
import os
import sys
import shutil
import random

def poem_gen(adj, noun, name, tp = 1, temp = 1, pp = 2, fp = 2):
    openai.api_key = "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"
    prompt_text = f"Write a critically-acclaimed {adj} free-verse poem on {noun}. \n \n The {noun} \n \n by {name}"

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    top_p= tp,
    temperature= temp,
    max_tokens=1047,
    presence_penalty= pp,
    frequency_penalty=fp
  )
    return response['choices'][0]['text']

def data_in():
    nouns = []
    adjs = [] 
    file = open("nouns.txt", "r")
    '''
    if os.path.exists("output"):
        shutil.rmtree("output")
    os.mkdir("output")
    '''

    for line in file:
        nouns.append(line.strip())
        '''
        text = poem_gen(poem_args[0], poem_args[1])
        text.strip()

        output = open(f"./output/poem{cur_line}.txt", "x")
        output.write(text)
        output.close()
        '''

    file.close()

    file = open("adjectives.txt", "r")
    for line in file:
        if line != '\n':
            adjs.append(line.strip())
    
    return (nouns, adjs)


def run_gen():
    (nouns, adjs) = data_in()
    authors = [
        "Robert Hayden",
        "John Keats",
        "Maya Angelou",
        "Lord Byron",
        "Henry David Thoreau",
        "Alice Zheng",
        "Pablo Neruda"
    ]

    temps = [1]
    tps = [1, 0.5, 0]
    fps = [2, 1.6]
    pps = [2, 1.6]

    for temp in temps:
        for tp in tps:
            for fp in fps:
                for pp in pps:
                    for i in range(3):
                        adj_i = adjs[random.randint(0, len(adjs) - 1)]
                        noun_i = nouns[random.randint(0, len(nouns) - 1)]
                        author_i = authors[random.randint(0, len(authors) - 1)]
                        text = poem_gen(adj_i, noun_i, author_i)
                        text.strip()
                        print(tp, fp, pp, adj_i, noun_i, author_i)
                        output = open(f"./output/poem{temp}_{tp}_{fp}_{pp}_{adj_i}{noun_i}{author_i}.txt", "x")
                        output.write(text)
                        output.close()

   


run_gen()

'''
def main():
  run_gen()


if __name__ == '__main__':
  main()
'''