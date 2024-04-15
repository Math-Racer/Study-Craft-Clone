The backend of our web application is built using python flask. We use langchain to build a prompt template. And the user input is fetched from the /input page. The input is then passed to the prompt template and then it is sent to the LLM. We use OpenAI's GPT-4-TURBO model. The user is asked what subject he wants to study and corresponding days he wants to allocate for the subject. Then the user takes a quiz which evaluates his knowledge. The quiz score is again passed to the LLM. The results page is dynamically created for each session. You can view the GitHub repo here:- https://github.com/Math-Racer/Study_Craft/


<iframe width="420" height="315" src="https://youtu.be/WZwJbvHfC_M"></iframe>


