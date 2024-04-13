def get_quiz(days, subject, goal):

    import openai
    import markdown
    client = openai.OpenAI(api_key="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")
    str1 = "You are a teacher who is tasked with creating student assessment to evaluate the knowledge of the student in the subject:" + subject
    template = """You have decided to give 5 multiple choice questions on this topic/subject. These questions must be of conceptual type. 

You will respond in the following way exactly. You should not say any other thing. The first line of your response should contain a dictionary whose keys are the questions in string format and values are python lists that contain multiple choice options. In the second line followed by the text "Correct answers:", give the correct answers for the 5 questions you gave in the form of a python list. This list will have correct choice number. The template is given below for your clear understanding:-

{"1, Question": {"A":"option A", "B":"option B", "C":"option C", "D":"option D"}, "2, Question": {"A":"option A", "B":"option B", "C":"option C", "D":"option D"}, "3, Question":{"A":"option A", "B":"option B", "C":"option C", "D":"option D"}, "4, Question":{"A":"option A", "B":"option B", "C":"option C", "D":"option D"}, "5, Question":{"A":"option A", "B":"option B", "C":"option C", "D":"option D"}}
Correct answers: [1, 2, 3, 4, 2]

"""


    def get_output(prompt):
        stream = client.chat.completions.create(
        # model="gpt-4",
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": prompt}],
        stream=True,)
        Response = ""
        for chunk in stream:
            Response += (chunk.choices[0].delta.content or "")
        return Response
    quiz = get_output(str1 + template)


    # print(quiz)
    list1 = quiz.strip().split("\n")
    questions = dict()
    print(list1)

    questions = list1[0]
    questions = eval(questions)

    answers = list1[1]
    print(answers)
    answers = answers[16:]
    print(answers)
    answers = eval(answers)
    print(questions)


    




    # start of code related to html
    prompt1 = f"""You are a gpt which creates mermaid.js code for the following flowchart. You should respond only with the following code template and you would not say any other thing. It is my strict order.
The code template:-
```mermaid
flowchart TD
    id1("course 1") ===> id2
    id2("Course 2") ===> id3
    id3("Course 3") ===> id4
            .
            .
            .
    idn("Course n") ===> proj
    proj("Capstone Project: blah blah blah)

    style proj fill:#f96,stroke:#333,stroke-width:4px
```
Act as a e-Learning expert who specializes in suggesting online courses for students. Now your task is to create a list of online courses along with the platform to study {subject}. Put the courses in the mermaid.js code template and give me the flowchart code. In each node, in the place of "course i", there should be both course name followed by the platform from which it is offered given in paranthesis. Take this example for "course i" node:- "Flask Web Development with Python Tutorial (Udemy)"
Remember that the the number of nodes in the flowchart must be same as the number of courses you suggest. Make sure all characters in the mermaid flowchart code doesn't include trademark symbol and other symbol that couldn't be typed using a standard keyboard. 
"""

    def mermaid_chart(mindmap_code):
        html_code = f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
<div class="mermaid">
{mindmap_code}
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true}});</script>
"""
        return html_code

    result = get_output(prompt1)
    #print(result)
    result = result[10:-3]
    html_code = mermaid_chart(result)
    # print(html_code)
    prompt2 = f"""Act as a Learning Coach who specializes in creating study plans for students.
Now your task is to create a set of learning objectives in the form of active recall questions that the student uses to evaluate himself each day.
The subject we gonna study is {subject}. The reason for this studying endeavour is: {goal}. Please make sure your response is aligned to that.
The number of days the student is going to study is {days} days.
"""
    header1 = """<!DOCTYPE html>
<html>
<head>
  <title>Results</title>
</head>
<body>
<h1>Here are the courses you should take to master this subject:-</h1>
"""

    midtext = """
<hr width="100%" size="2">
<h1>Learning Objectives to make sure your learning is efficient throughout</h1>
"""
    endtext = """
<div class="gray-box">
  <div class="container" id="about">
    <h2>About Us</h2>
    <p>StudyCraft is a platform designed to help students master their subjects effectively. Our mission is to provide the tools and resources necessary for academic success.</p>
  </div>
  <div class="container" id="contact">
    <h2>Contact Us</h2>
    <p>If you have any questions or feedback, feel free to contact us at support@studycraft.com</p>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    objectives = get_output(prompt2)
    filename = "my_page.html"
    with open("templates/"+filename, "w") as f:
        f.write(header1)
        f.write(html_code)

        f.write("")
        f.write(midtext)
        f.write("")
        html_text = markdown.markdown(objectives)
        f.write(html_text)
        f.write(endtext)




    
    return questions, answers
