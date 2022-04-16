# Logophile: A Free Verse Poetry Generator

## Introduction and Related Works
Bridging the gap between computation and creativity, building a system that can produce creative works of 'art', has been the source of much discussion and interest throughout time. How can one artificially produce inspiration, create art, through a systematic process? What separates machine-made and human-made art, and how can one determine this difference? Poetry is already difficult enough for humans to create. What makes a poem 'good' goes so much beyond word choice, sound, rhythm; so much of it lies within the heart, the soul of the message being expressed. Needless to say, it seems quite difficult for an artificial source, a computer without a soul, to produce good poetry. But recently, there have been many exciting developments within the realm of computation, primarily with neural nets and natural language processing. Computers are now able to solve problems we could only dream of a few years before, from image classification to sentiment analysis. Programs were able to navigate the grey, fuzzy area of problems to be solved--and this grey area includes text generation. 

GPT is among these incredibly promising developments, a model that excels at generating text given a prompt using natural language processing. By fine-tuning GPT-3, we hope to develop a neural network, a computer program, that is capable of producing free-verse poetry nearly indistinguishable from that produced by a human. The majority of our papers present ways to generate novel poetry view recursive neural networks, which is in the realm of what we wish to accomplish. One related work that helps in our understanding of this problem space is Automatic Poetry Composition through Recurrent Neural Networks with Iterative Polishing Schema by Yan et. al. In this paper, researchers propose an original way to compose poetry based on recurrent neural network structures. The paper presents a new polishing schema for generating poems, which outputs a refined piece of work. In this way, due to multiple iterations that improve the wording, the poetry composition is more similar to the real human writing process. Similarly, a different paper titled Chinese Poetry Generation with Planning Based Neural Network by Zhe Wang et. al. proposes a different yet effective way of training a neural network to generate poems. Yan presents a way to refine poetry via multiple iterations, while Wang presents a way to generate poetry via the generation of subtopics for each topic and subsequently generating content for each subtopic. Both present different ways to generate poetry, which are both useful to our task. However, our project is more suited towards the latter because we aim to generate novel freeform poetry via topic rather than to have a poem refined generation by generation. Our task will require a recursive neural network similar to the networks described in each paper, though we will be using the network primarily to generate new freeform poetry rather than to refine it.

## Project Outline
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

## Methods

### Models
After thorough research, we decided to find a relevant dataset rather than creating one from scratch. Our team was able to find this free verse poetry dataset (https://www.kaggle.com/michaelarman/poemsdataset). Our intention with the dataset is to fine-tune the GPT3 model to be able to generate the free verse poetry. Given an optional prompt, word count, and temperature value (how ‘creative’ or unique the output will be), the model will return a sample free verse poem according to the specifications outlined (and hopefully related to the prompt given). We will implement our model using PyTorch and OpenAI GPT-3. Our method involves building a model by fine-tuning GPT3 with poem data and seeing how well the model performs compared with a GPT3 model that is not fine-tuned. Evaluating the model will also involve trying out different prompts such as “write a poem”, “generate a sonnet” among others. We can also evaluate performance using different models—using Davinci, Curie, Babbage, and Ada. Davinci is the most powerful model, being able to perform all tasks the other models are capable of but with less instruction. It provides the best results in terms of contextual understanding of text but costs the most resources and time to run. It is particularly suited for complex intent, cause and effect, and summarization. Curie is also powerful but runs faster than Davinci. It pales slightly in comparison when analyzing complex text, but it is quite skilled at language translation, complex classification, text sentiment, summarization, and other tasks that require a nuanced understanding of the given text. Babbage is not as capable as either Davinci or Curie, but it is faster and can perform well at classification and semantic search. Ada is the most lightweight and fastest model and is useful for simpler tasks, such as parsing text, simple classification, address correction, and keyword recognition.

### Analysis
In order to analyze the models, we will create a classification model that should be able to distinguish between AI-written poems and human-written poems. We will have a dataset of AI-generated poems, and human-written; We will train the model, so it is able to learn which one is which. As part of our analysis, we will determine whether the fine-tuned GPT3 model can confuse the classification model to think that an AI-written poem was written by a human.

### Discussion 

We found that our prompt-design poem generation script, which utilized GPT-3's DaVinci engine was able to produce [GOOD/DECENT] results. We also fine-tuned the engine by training it on real world examples of handwritten free verse poetry. We found that the model performed better than the baseline GPT-3 model by a margin of _____. Initially, we had hypothesized that we would be able to create a model that would be able to write poetry as "good" as an actual human would be able to. What we found was that _______. We validated this by running a classification model, which showed that ____% of the time, the model was able to accurately predict what was a human written poem versus what was an artificially generated poem. Initially, we had hoped and hypothesized that we would be able to generate poems that would be nearly indistinguishable from computer-generated poems. Given that the model was able to detect the difference between the two types of poems ___% of the time, our hypothesis was ultimately proven [TRUE/FALSE].




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

