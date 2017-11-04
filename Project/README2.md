# Title : The food symphony

ADA's Food Symphony

(The perfood harmony) perfect + food = perfood ?

Taste Affinities

# Abstract

Have you ever wondered while cooking whether these ingredients could be great together ? A good example is certaintly the hawaiian pizza(Ham + pineaple)

Thus, using the big dataset gathering cooking recipes all around the world, our project's goal is to extract the combination of ingredients and try to find an interconnection between them.

First of all, the firt step will be to extract the essence of each ingredient in a recipe and then analyse what the ingredient bring to the recipe (sweet, spicy, ...). 
The second step, will be to find correlation between recipes in order to map which combinations of different ingredients blend the best together to give tasteful meals. 
Finally, we imagine an interface where users will give as input a series of ingredients and constraints, i.e. (vegan, with meat, with fish, etc.) and a recipe will be suggested to them. From there we can use machine learning to create new recipes from what we have learned. Theoretically, this mechanism will consider all ingredients seen in the learning phase, thus new unknown mixtures of ingredients can emerge giving rise to the best recipe ever (hopefully).
To achieve our goals, we will use Cooking recipes dataset, where we can get the list of ingredients, ingredients bag of words, ingredient categories, the total amount of calories and the calories by group, i.e. fat, protein, sugar, as well as the sodium and cholesterol content.

Story: 
We believe that ingredients in a recipe are like harmonies in music, separated they are pleasant to hear, but when perfectly combined harmonies can come up with something special (Schubert' Symphonies).
Therefore, we are convinced that the best combinations have never been done and also that special combinations have yet to be found. 
Indeed, best chef in the world always tries when making a creation, to have all ingredients in osmosis. What if the best combination is a fish from Tahti, a spice from Tierra del Fuego, some exotic vegetable from Vietnam and olive oil from Italy. How would be able to produce it?     

Motivation: We are three students that enjoy cooking and eating, however, as students, it's not always easy to take the time to check for a recipe, look at the ingredients we already have and what we are missing. Also, it's not easy to have new ideas or to know whether what are left in our fridges could be cooked together. We believe this project is a good idea, to speed up process, indeed one would need to give as input the ingredients and a new tasty recipe would pop up.


# Research questions
## A list of research questions you would like to address during the project.

1. Are common ingredients (like meats, rice or pasta) essential for a good meal ? Or whether exotic ingredients make it special ?

2. What is the essence of each ingredient and what do they bring in a recipe ? 

3. Are the high calorie recipes are the most popular ?

4. What kind of correlation between ingredient will be the best to find the harmony in a recipe ? 

5. What are the processus of the best chef in the world to find new recepies ? And could we apply this to our project ?

4. What should we implement in our interface to make it interactive and friendly using ?


# Dataset
## List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.




# A list of internal milestones up until project milestone 2
## Add here a sketch of your planning for the next project milestone.
The project milestone should contain a notebook with data collection and descriptive analysis.

Week #1 :
- Agree on the dataset and what information to extract.
- Discuss with the TA about our work plan.
- Find function to handle text extraction (only important words, without articles words such as the, a, for ...)

Week #2 :
- Data collection
- Group ingredients into categories
- Characterize the essence and role of each ingredients
- Start to find correlation between them
- Work on possible combinations

Week #3 :
- Come up with a solution to measure the harmony of our recipes
- Start to work on the learning phase
- Work on chef's processus to find new recipes
- Work on our data story
- Work on the descriptive analysis

Week #4
- Finalize the notebook
- Structured and informed plan for the next milestones.
- Start to work on our data story or report
- Start to discuss about the presentation for the poster

# Questions for TAa
Add here some questions you have for us, in general or project-specific.

- Would it be possible along with the poster to bring some meals cooked based our project ?

- We really want to do something interactive, Would you have any recommandations (website or interface on computer) ?

- We will need powerful tools of natural language processing and machine learning to extract ingredients and come up with new combinaison. Is it doable?
