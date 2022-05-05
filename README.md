# Logophile: A Free Verse Poetry Generator

## Abstract
Recently, AI-generated art has been a trendy topic in the technology field and has spurred much public attention and debate. In this project, we attempted to create a neural network that is capable of generating poetry, which could serve as an inspiration for aspiring writers. First of all, we built a neural network that, given an optional input, was able to produce free verse poetry related to the aforementioned input. Secondly, we were able to create a corpus of free verse poetry to fine-tune GPT-3 with. In order to analyze the quality of our model, we built a classifier to distinguish between human and AI-written poetry. Finally, we deployed our model into a full-stack web application, making it accessible for other users to try what we have made. The results revealed that after fine-tuning the model, GPT-3 produced impressive poetry, which could help many individuals who are pursuing creative careers. Looking forward, we want to expand our model to be able to generate different types of poetry as well as utilize languages other than English.

## Introduction 
Bridging the gap between computation and creativity, building a system that can produce creative works of 'art', has been the source of much discussion and interest throughout time. How can one artificially produce inspiration, and create art, through a systematic process? What separates machine-made and human-made art, and how can one determine this difference? Poetry is already difficult enough for humans to create. What makes a poem 'good' goes so much beyond word choice, sound, and rhythm; so much of it lies within the heart, the soul of the message being expressed. Needless to say, it seems quite difficult for an artificial source, a computer without a soul, to produce good poetry. But recently, there have been many exciting developments within the realm of computation, primarily with neural networks and natural language processing. Computers are now able to solve problems we could only dream of a few years before, from image classification to sentiment analysis. Programs were able to navigate the grey, fuzzy area of problems to be solved—and this grey area includes text generation. [GPT-3](https://openai.com/api/), which stands for generative pre-trained transformer is among these incredibly promising developments. It is an autoregressive language model that excels at generating text given a prompt using deep natural language processing. GPT-3 was created by Open-AI researchers and is able to generate text of fantastic quality that it can be difficult to determine whether the text was created by a human or a machine. By fine-tuning GPT-3, we hope to develop a neural network, a computer program, that is capable of producing high-quality free verse poetry that is hardly different from that produced by a human. 

## Literature Review
The majority of our papers present ways to generate novel poetry via recurrent neural networks, which is in the realm of what we wish to accomplish. One related work that helps in our understanding of this problem space is Automatic Poetry Composition through Recurrent Neural Networks with Iterative Polishing Schema by [Yan et. al.](https://docs.google.com/document/d/1tkzKsjO0iDMrHkXCsDCE7D3gaD9AI-qnp5vf0gpSVN0/edit?usp=sharing)
In this paper, researchers propose an original way to compose poetry based on recurrent neural network structures. The paper presents a new polishing schema for generating poems, which outputs a refined piece of work. In this way, due to multiple iterations that improve the wording, the poetry composition is more similar to the real human writing process. Similarly, a different paper titled Chinese Poetry Generation with Planning Based Neural Network by [Zhe Wang et. al.](https://www.researchgate.net/publication/309572681_Chinese_Poetry_Generation_with_Planning_based_Neural_Network) proposes a different yet effective way of training a neural network to generate poems. Yan presents a way to refine poetry via multiple iterations, while Wang presents a way to generate poetry via the generation of subtopics for each topic and subsequently generating content for each subtopic. Both present different ways to generate poetry, which are both useful to our task. However, our task is more suited towards the latter because we aim to generate novel freeform poetry via topic rather than to have a poem refined generation by generation. Our task will require a recurrent neural network similar to the networks described in each paper, though we will be using the network primarily to generate new freeform poetry rather than to refine it.

## Methods

### Models
After thorough research, we decided to find a relevant dataset rather than creating one from scratch. Our team was able to find this free verse poetry [dataset](https://www.kaggle.com/michaelarman/poemsdataset). Our intention with the dataset is to fine-tune the GPT-3 model to be able to generate the free verse poetry. Given an optional prompt, word count, and temperature value (how ‘creative’ or unique the output will be), the model will return a sample free verse poem according to the specifications outlined (and hopefully related to the prompt given). We will implement our model using [PyTorch](https://pytorch.org/hub/huggingface_pytorch-transformers/) and OpenAI GPT-3. Our method involves building a model by fine-tuning GPT-3 with poem data and seeing how well the model performs compared with a GPT-3 model that is not fine-tuned. Evaluating the model will also involve trying out different prompts such as “write a poem”, “generate a sonnet” among others. We can also evaluate performance using different models—using Davinci, Curie, Babbage, and Ada. Davinci is the most powerful model, being able to perform all tasks the other models are capable of but with less instruction. It provides the best results in terms of contextual understanding of text but costs the most resources and time to run. It is particularly suited for complex intent, cause and effect, and summarization. Curie is also powerful but runs faster than Davinci. It pales slightly in comparison when analyzing complex text, but it is quite skilled at language translation, complex classification, text sentiment, summarization, and other tasks that require a nuanced understanding of the given text. Babbage is not as capable as either Davinci or Curie, but it is faster and can perform well at classification and semantic search. Ada is the most lightweight and fastest model and is useful for simpler tasks, such as parsing text, simple classification, address correction, and keyword recognition.

### Analysis
In order to analyze the models, we will create a classification model that should be able to distinguish between AI-written poems and human-written poems. We will have a dataset of AI-generated poems, and human-written; We will train the model, so it is able to learn which one is which. As part of our analysis, we will determine whether the fine-tuned GPT3 model can confuse the classification model to think that an AI-written poem was written by a human.

## Discussion 

### Prompt-Design
GPT-3 is unique from all of its predecessors thus far in its ability to accurately "react" to a prompt and predict what's likely to come next, all without fine-tuning towards some desired output. However, this power comes at a cost: small changes in the prompt fed to GPT-3 can drastically change the resulting outputs. Thus, our task for prompt-design was to come up with a prompt that could enable GPT-3 to create the "best" poems, in our case being the most human-like and least robotic. We explore the various prompts and modifications we looked into throughout our prompt-design process, and share sample GPT-3 outputs from these respective prompts (all with temperature = 1, top-p = .87, frequency penalty = 1.5, presence penalty = 1.25, no cherry-picking!).

We start with a basic prompt: "Write a free-verse poem." [Here are 3 sample outputs.](https://docs.google.com/document/d/1Pi11v6BpMl4L34GgjaGr31vrndXU2re3qbq_RkN3VxA/edit?usp=sharing)

Not terrible! But we can do better. Let's try increasing the 'quality' of the poem by specifying that it's critically-acclaimed (which has reported to be relatively successful from [this article](https://arr.am/2020/07/31/gpt-3-using-fiction-to-demonstrate-how-prompts-impact-output-quality/)).

"Write a critically-acclaimed free-verse poem." [Here's the sample outputs.](https://docs.google.com/document/d/1gpApG-j5MSF9pHz03nZCIpBeHA9F6B7exPrCPHCnShQ/edit?usp=sharing)

Okay, we definitely went a step in the wrong direction here. Two of the poems sound basically the exact same, and one of them isn't a new poem, but rather an excerpt from a pre-existing critically-acclaimed poem! We realized what GPT-3 needs here is a sense of direction, guiding it towards what it should be writing about. Thus, we included a subject and tone into the prompt, or what the poem is about, and the tone we want the poem to have. Here's our new prompt:

"Write a critically-acclaimed {tone} poem on {subject}." [Here's the outputs, with tone = "wistful" and subject = "rain".](https://docs.google.com/document/d/1AbATDxcDGzbpYe7xzBApugB2tzPJOrXG1LDpZmqF6Gw/edit?usp=sharing)

Now we're getting somewhere! The poems are far more descriptive. But we can still do better. We add one more addition to the prompt: a title, and an author. This includes many different properties: we find that the author we provide drastically changes the style of the output! Thus, we explore 3 more outputs, with the same subject and tone, but with three authors: Robert Hayden (made-up name), Lord Byron (famous romantic poet), and Maya Angelou (female BIPOC contemporary poet). [Here's the results.](https://docs.google.com/document/d/1jr4V7qPSyV4YG6IstK4QqlDOOr4U4gBbBrR8uKqVWNc/edit?usp=sharing)

It's clear to see that this addition of author and title is a massive step up. The outputs are incredible now, full of style and description! Unique spacing, distinct form---it's fascinating to see how these poems are all generated by machines, not humans. Moreover, an interesting thing to note is the relationship to the author name to the style and content of the text. Another fascinating area to explore would be how names change GPT-3's outputs, with not only famous names, but also names relating to specific ethnicities (East Asian, Latinx, etc). This can all lead to incredibly interesting outputs: for instance, having "John Keats" (or GPT-3's impression of him) write on "crying in H-Mart" leads to some fascinating reads! However, there's still one last improvement.

Now, lets change up our perspective of the subject. Previously, our subject is very simple: "rain". But we can make it more specific, more interesting. This subject is the title of our poem! So let's add some flavor into it. Our new prompt: "daydreaming out into the rainy window", with the same "wistful" tone. [Here are the poems!](https://docs.google.com/document/d/1tkzKsjO0iDMrHkXCsDCE7D3gaD9AI-qnp5vf0gpSVN0/edit?usp=sharing)

Needless to say, these poems are very impressive. By making the subject more specific, GPT-3 is able to weave in the tone more clearly into the poem it generates! These poems are all similar in meaning, but highly different in style.

### Results

We found that our prompt-design poem generation script, which utilized a fine-tuned version of GPT-3's DaVinci engine trained on real-world examples of human-written poetry, was able to produce decent results, though not the results we were ideally looking for. Initially, we had hypothesized that we would be able to create a model that would be able to write poetry as "good" as an actual human would be able to. What this entails is that our best binary classifier (which classifies between "real" and "artificial" poetry) would have an accuracy of around 50%, thus indicating that human and AI-generated poetry are virtually indistinguishable, at least to a well-trained model. We trained multiple binary classifier models and ultimately selected the three best-performing models to use as our basis for determining whether there is a distinguishable difference between the two sorts of poetry. We trained our top three performers on a combination of human and AI data and found that our top three models performed with accuracies of 0.94, 0.82, and 0.94 for the baseline data and the fine-tuned data, respectively. 


Classification Model Try 5 (after fine-tuning with fit.one_cycle 2 times)

| epoch         | train_loss    | valid_loss    | accuracy      | fbeta_score   | time          |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 0             | 0.275677      | 0.363191      | 0.941176      | 0.928571      | 00:03         |

Classification Model Try 2 (after fine-tuning with fit.one_cycle 3 times)

| epoch         | train_loss    | valid_loss    | accuracy      | fbeta_score   | time          |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 0             | 0.238607      | 0.463249      | 0.941176      | 0.944444      | 00:03         |


Classification Model Try 4 (after fine-tuning with fit.one_cycle 4 times)

| epoch         | train_loss    | valid_loss    | accuracy      | fbeta_score   | time          |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 0             | 0.188131      | 0.438647      | 0.823529      | 0.842105      | 00:03         |
| 1             | 0.153211      | 0.399580      | 0.852941      | 0.871795      | 00:04         |


While this seems to imply that the models were able to pinpoint with relative accuracy what is and is not artificially-generated poetry, there are some other considerations we must make as well. Firstly, the models could very well be overfitting to certain types of poetry and classifying by genre, word-choice, or other extraneous factors. We see that this is a likely possibility by looking at the test results from each of our models. We tested our models by generating 100 examples of artificially-produced poetry both with our fine-tuned model and with the baseline model with the following hyperparameters set: temp=1, top_p={.75, 1}, freq_pen={.8, 1.2, 2}, pres_pen={.8, 1.2, 2}. We found these hyperparameters to work the best based on a grid search. Our first model misidentified 12/30 examples of the baseline generated data, while it misidentified 36/38 examples of the fine-tuned data. Our second model misidentified 7/30 examples of the baseline data and 36/38 of the fine-tuned examples. Our final model misidentified 7/30 of the baseline examples and 34/38 of the fine-tuned examples. 

Furthermore, this suggests that by fine-tuning the model, we are able to achieve results that more closely mimic poetry that would be written by a real person. This is all to say, while we may not have achieved a perfect model, the data suggests that there is definitely room for improvement on this front, that a more fine-tuned model may be able to get closer to producing poetry that is indistinguishable from that which a human would write. 

![Misidentified Poems](https://user-images.githubusercontent.com/78115104/166850553-5d4b0628-d30c-4f7e-a1c3-194645c6e294.png)


## Ethics
The main ethical questions for this project are: “Should we be even doing this?”, “Is there any harm, and what are the benefits of our idea?” We believe that this project is ethical and safe – in fact, the primary purpose of our project is to combat writer’s block and help writers receive inspiration from the constant flow of newly generated poetry. However, we think it is essential to consider specific questions and issues that could arise from this project. First of all, there is a question of who would be taking credit for the work generated by AI. This question is difficult to answer, and after a thorough discussion, we believe that credit should be given to the people who created a model, Open-AI, and to the artists who created their poems for the datasets we have used. In addition, it is vital to consider the potential cases of plagiarism, and whether it is intended or unintended, it could create a bad reputation for the tool and negatively affect the artist who is using this tool for inspiration. If we consider AI as a machine, it detaches accountability from the AI’s creator, and issues like plagiarism, sexism, or racism could go unnoticed, which raises ethical concerns about AI creation. Secondly, it is essential to examine how AI-generated poetry is going to influence independent writers and people who create poetry as their main source of income. Writers put time, effort, and ideas into creating high-quality original work, which means that producing too much AI-generated poetry could make it challenging for independent creators to compete with a machine. Artists could lose job opportunities, and dishonest individuals could take credit for AI-generated poetry. Ultimately, there are a lot of ethical implications to this project that are worth addressing. If not done properly, this model has the potential to perpetuate racism or sexism, financially harm independent writers, or negatively represent different cultures.  

## Reflection
One of the main things that we could have done better on this project is getting to start earlier. It could be deceiving to think that the project would be completed faster with a bigger group of people; however, we soon realized that logistically it was difficult to find a time that would work for the five of us. 

If we had more time on this project, we see a couple of directions we could continue our work. Firstly, it would be interesting to create a feature that allows people to share AI-generated poetry on social media. In modern society, social media holds a lot of power and sharing poetry on the platforms like Facebook or Twitter is common among people of our age. This feature would make poetry simple and accessible for many individuals, who could use it as a source of inspiration. However, it is important to consider how it would affect other people despite the benefits. The potential disadvantage of this feature could be a discouragement from writing original poetry. In some ways, it seems significantly easier to train a neural network model that can write unique and brilliant poetry than to write it yourself. Creators could overuse it and pretend like it is their work. Coming up with a solid plagiarism prevention strategy is one of the ways we hope to further our work. On the other hand, while it is difficult to prevent humans from plagiarizing content, it is essential to ensure that our AI model generates plagiarism-free content and does not include hurtful speech (sexism, racism, etc.). In order to build AI that makes unbiased poetry, we would have to clean our training dataset from conscious and unconscious assumptions about gender, race, and other ideological concepts. Lastly, we want our work to be accessible to all internet users, and at the current moment, our model can only produce free-verse poetry in English. Ideally, we want our model to be able to generate different types of poetry in different languages, which could significantly benefit a vast number of writers across the globe.   

## References
Chambers, America. “Generating Homeric Poetry with Deep Neural Networks.” Generating Homeric Poetry with Deep Neural Networks | Department of Classics, 1 May 2020, classics.stanford.edu/publications/generating-homeric-poetry-deep-neural-networks. 

Wang, Zhe, et al. “Chinese Poetry Generation with Planning Based Neural Network.” ArXiv.org, 7 Dec. 2016, arxiv.org/abs/1610.09889. 

Yan, Rui. “I, Poet: Automatic Poetry Composition through Recurrent Neural Networks ...” July, 2016.

Zhang, Tianyi, et al. “BERTScore: Evaluating Text Generation with Bert.” ArXiv.org, 24 Feb. 2020, arxiv.org/abs/1904.09675. 






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

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/]
basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/awguo2019/cs152sp22/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
--->

