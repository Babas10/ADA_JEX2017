# Title
Healthy Habits

# Abstract
## A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?
Our goal is to extract information about healthy pattern in a dataset. More precisely we would like to found articles with health related subject, rate their importance and get more specific information. For example We could then plot a health impact in term of different  discrete "problems": fast food, gluten, etc.. by region and by period if possible. 
Secondly we would like to see if new problem have appeared and other dissapeared or have been solved. It would be possible to analyse this by finding sudden increase/decrease in frequency of specific terms.

Story:

    ⋅⋅* Health is a key factor that follows us along through life. Epochs pay different attention to it, but still were always concerned a moment or another. 
    Through the evolution of technologies and with the expansion of the knowledge through the internet,  people became much more concerned. 
    With it new theories, lobbies and trends, appeared in society, changing definitively the way of life of people and the link with health. 
    We will by analysing web news of different countries try to perceive the changes of the meaning of the word "health" and try to identify which are the key factor related to those changes.

Motivation:

  ⋅⋅*  It would be very interesting to see if some problems appeared / dissapeared in some part of the world before other.
  ⋅⋅*  How did our percpetion of healthy has evolved ? (When a developing country becomes a developed country people can focus on different problems. Before the bottom of the pyramid is fullfilled it is not possible to address problems in the top of the pyramid)



# Research questions
## A list of research questions you would like to address during the project.
- What are important health issues of the 21st century?
- Impact of different behaviour/habits on health?
- Malnutrition, undernourishment or overconsumption of specific food could have an impact on the health issues.

# Dataset
## List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

New on the web, contains downloadable, full-text corpus data set from ( NOW, Wikipedia, COCA, COHA, GloWbE) that are in English and the Corpus del Español data set. From the English data set there are two of them that contains 20 English speaking countries. In order to have a quick overview of the available data, we check how many times some key words "Intolerance", "Gluten", "Health" appear in 3 data sets.

| Data Set | Countries | # Health | # Gluten | # Intolerant |
|----------|-----------|----------|----------|--------------|
| NOW      | 20        |  605000  |   8331   | 5116         |
| COCA     | 1         |  183000  |    661   | 816          |
| COHA     | 1         |   43000  |    200   | 1230         |


By adding the 3 others data set we think we will have enough material to make an analysis of the trends and its propagation. It will be possible for us to go further in the trend propagation by analysing how the health issues cross the barrier of language by including the Spanish dataset.
The data set are provided in 3 different ways i.e as a raw data set, words/lemma, or linear text. 


-200 years of News : Information more localized but can be a strength whether our project wants to identify the questions on country scale.
-Wikipedia


# A list of internal milestones up until project milestone 2
## Add here a sketch of your planning for the next project milestone.
The project milestone should contain a notebook with data collection and descriptive analysis.

Week #1 : 
- Agree on the dataset and what information to extract
- Discuss with the TA about our work plan.
- Find function to handle text extraction (only important words, without articles words such as the, a, for ...)

Week #2 :
- Data collection
- Find correlation to answer the questions

Week #3 :
- Work on a possible data story
- Work on the descriptive analysis
Week #4
- Finalize the notebook
- Structured and informed plan for the next milestones.
- Start to work on our data story or report
- Start to discuss about the presentation fo the poster

# Questions for TAa
Add here some questions you have for us, in general or project-specific.

- DO YOU GUYS LOVE OUR PROJECT PROPOSAL ?
