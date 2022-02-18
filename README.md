# Logophile: A Free Verse Poetry Generator

## Project Outline
Bridging the gap between computation and creativity, building a system that can produce creative works of 'art', has been the source of much discussion and interest throughout time. How can one artificially produce inspiration, create art, through a systematic process? What separates machine-made and human-made art, and how can one determine this difference? 

Poetry is already difficult enough for humans to create. What makes a poem 'good' goes so much beyond word choice, sound, rhythm; so much of it lies within the heart, the soul of the message being expressed. Needless to say, it seems quite difficult for an artificial source, a computer without a soul, to produce good poetry. 

But recently, there have been many exciting developments within the realm of computation, primarily with neural nets and natural language processing. Computers are now able to solve problems we could only dream of a few years before, from image classification to sentiment analysis. Programs were able to navigate the grey, fuzzy area of problems to be solved--and this grey area includes text generation. GPT is among these incredibly promising developments, a model that excels at generating text given a prompt using natural language processing. By fine-tuning GPT-3, we hope to develop a neural network, a computer program, that is capable of producing free-verse poetry nearly indistinguishable from that produced by a human. 

We hope to a) be able to create a corpus of free-verse poetry to fine-tune GPT-3 with, b) build a neural network model that given optional input, can produce free-verse poetry relating to aforementioned optional input, and c) evaulate this poetry by either 1) having humans classify AI-generated poetry from man-made poetry, or 2) build a neural network classifier distinguishing AI and human poetry. Lastly, we hope to deploy our model(s) into a full-stack web application so that other users can play around with what we built. 

Some ethical questions: Should we be doing this? I don't see why not--this project is all in good fun, and its main impact (to us) is just to see if we can create art from a computational source. What might be the accuracy of a simple non-ML alternative? Probably very poor--I can't imagine a non-ML alternative could see much variation in sentence structure, syntax, etc. Is our data valid for its intended use? We hope to grab all our data from the public domain of the internet as 'inspiration' for our model, so we believe yes. What bias could be in our data, and how can we minimize said bias? I forsee bias being prevalent in the voices we take in our dataset--it can be likely for us to sample mostly caucasian male poets, thus creating a bias in the writing form and topics of our AI. In order to combat this, we need to sample poets of different cultures, gender idenitities, and ethnicities in order to build a full picture of the breadth free-verse poetry covers. Lastly, we need to be careful of content warnings/profanity--some possible solutions include 1) filters (or sentiment analysis models) detecting possible hurtful speech, or 2) including content warnings if necessary. 

## Project Description

I'd like to train neural networks / utilize OpenAI's GPT-3 model to generate poetry, or more specifically [free verse poetry](https://en.wikipedia.org/wiki/Free_verse). Given an optional prompt, word count, and temperature value (how 'creative' or unique the output will be), the model will return a sample free verse poem according to the specifications outlined (and hopefully related to the prompt given). A dataset of free verse poetry will need to be created, probably through scraping internet forums (reddit api?) and webpages, alongside famous free verse poem books.

The trained model will be deployed as a web application where you can generate poems according to the specifications listed above, and if so desired, can share generated poems on social media platforms (additional feature if time permits). Additional extensions can include attempting to branch out to alternate forms of poetry (haiku, sonnet, etc), which would all require modifications to the dataset.

The longer-term goal of the project is to see if a computer, or neural net, is capable of producing art, writing that inspires meaning to the reader. I wonder if AI can shed new perspectives, new approaches to theese creative fields of generating written works, and if there's anything we can learn from an AI's writing style (which has been trained by humans). I hope to have fun with the model and see what it comes up with, and also see how to improve it as we go! This emerging field of text generation is incredibly exciting, and I hope to get a taste through this project.

## Project Goals
1. Create a dataset/corpus of free verse poems for our NN to "draw inspiration from".
2. Explore methods for making the writing more "human", and for making it more "creative".
3. Train a NN that is capable of generating a free verse poem (related to an optional prompt the user enters in). 
4. Deploy the NN as a web-app that the user can freely interact with.


## Related Works
1: Yan, R. (n.d.). I, poet: Automatic Poetry Composition through Recurrent Neural Networks with Iterative Polishing Schema. Retrieved February 17, 2022, from http://cslt.riit.tsinghua.edu.cn/mediawiki/images/c/c7/Automatic_poetry_composition_through_recurrent_neural_networks_with_iterative_polishing_schema.pdf 

Researchers propose an original way to compose poetry based on recurrent neural network structures. The paper presents a new polishing schema for generating poems, which outputs a refined piece of work. In this way, due to multiple iterations that improve the wording, the poetry composition is more similar to the real human writing process. 

2: Chinese Poetry Generation with Planning based Neural Network (pdf in the chat)

The paper discusses techniques used to generate unique Chinese poetry by first generating the subtopics of the poem and then generating the content for each subtopic.
3: Generating Homeric Poetry with Deep Neural Networks
A. Lamar and A. Chambers, "Generating Homeric Poetry with Deep Neural Networks," 2019 First International Conference on ​Transdisciplinary AI (TransAI), 2019, pp. 68-75, doi: 10.1109/TransAI46475.2019.00020.

4: Evaluating Text Generation with BERT (https://arxiv.org/pdf/1904.09675v3.pdf)

The paper discusses pitfalls with modern text generation evaluation metrics and introduces BERTScore, a deep learning metric, and shares testing data on image captioning.




<!---
```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/awguo2019/cs152sp22/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
--->

