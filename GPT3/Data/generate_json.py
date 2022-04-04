import jsonlines
import os

# update this depending on what your absolute path is!
path = "/Users/aguo/Desktop/cs152sp22/GPT3/Data/free-verse"
os.chdir(path)

prompt_text = "Write an award-winning poem."
output = []

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        text = (f.read())
        poem = {"prompt": prompt_text, "completion": text}
        output.append(poem)

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        # call read text file function
        read_text_file(file_path)

with jsonlines.open('output.jsonl', 'w') as writer:
    writer.write_all(output)

