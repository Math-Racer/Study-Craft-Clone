The backend of our web application is built using python flask. The app relies on foundational model such as gpt-4-turbo. The model is prompt tuned by our prompt template built using Langchain. To which the user input is passed. The LLM is given instructions on how to create the output, this technique is similar to few-shot prompting technique, even though is is not its direct application. LLM creates the quiz to evaluate user's prior knowledge. Based on the user's input, we create the learning path along with a list of learning objectives. 


https://github.com/Math-Racer/Study_Craft/assets/123105406/2d60a088-28d4-4357-abe6-d6b1d8aec66a

