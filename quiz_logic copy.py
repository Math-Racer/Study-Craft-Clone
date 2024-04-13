

def get_quiz(name, subject, difficulty):
    import os
    os.environ["OPENAI_API_KEY"] ="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"
    from langchain.llms import OpenAI
    llm = OpenAI(temperature=0.9)  # model_name="text-davinci-003"
    #print (llm("create a list of diagnostic test questions"))
    from langchain import PromptTemplate

    template = """You are a teacher who is tasked with creating student assessment to evaluate the knowledge of the student in the subject:{sub}. You have decided to give 5 multiple choice questions on this topic/subject. These questions must be of conceptual type. 

    You will respond in the following way exactly. You should not say any other thing. The first line of your response should be first question enclosed in double quotes and the second line should be a python list which contains multiple choice options for the first question. In similar way, the second question and muliple choice options for that question should be in 3rd and 4th line respectively. Thus the 10 lines will have questions and their choices. The 11th line will have text "Correct answers" and in the 12th line you will actually give the correct answers for the 5 questions you gave in the form of a python list. This list will have correct choice number. The template is given below for your clear understanding:-

    "Question 1"
    ["option 1", "option 2", "option 3"]
    "Question 2"
    ["option 1", "option 2", "option 3"]
    "Question 3"
    ["option 1", "option 2", "option 3"]
    "Question 4"
    ["option 1", "option 2", "option 3"]
    "Question 5"
    ["option 1", "option 2", "option 3"]
    "Correct answers"
    [1,2,2,1,3]
    """
    prompt = PromptTemplate(template=template, input_variables=["sub"])

    # Replace this with your logic to generate questions and answers based on input
    formatted_prompt = prompt.format(sub=subject)
    quiz = llm(formatted_prompt)
    print(quiz)
    list1 = quiz.strip().split("\n")
    questions = dict()
    counter = 0
    print(list1)
    print(len(list1))
    for i in range(5):
        questions[list1[counter].strip('"')] = list1[counter+1]
        counter += 2
    answers = list()
    answers = list1[-1]
    #print(question)
    #print(ans)
        # Replace this with your logic to generate questions and answers based on input
    questions = {
        "What is the capital of France?": {"A": "Berlin", "B": "Paris", "C": "London", "D": "Madrid"},
        "What is 2 + 2?": {"A": "1", "B": "2", "C": "4", "D": "5"},
    }
    answers = [2, 3]
    return questions, answers
