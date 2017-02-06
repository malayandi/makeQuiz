"""
Given a TeX file containing a set of questions, each tagged by their difficulty
and topic, returns a list containing questions and a dictionary which maps each
question number to a tuple containing its difficulty and topic.

e.g. of an input block:

===
difficulty = 1
topic = 2
The question goes here. It should be in LaTeX form. It doesn't matter if the que-
stion is too long. You can use
\begin{enumerate}
    \item any blocks as you usually would
    \item and math notation too, like 4^3 = 64
\end{enumerate}
===

Each block must begin and end with "===" and must have a difficulty and topic
tag, exactly as given above.
"""

def reader(filename):
    with open(filename) as f:
        contents = f.readlines()

    contents = [x.strip() for x in contents]
    questions = []
    dt_map = {}

    while len(contents) > 1:
        index = contents.index("===")
        difficulty = int(contents[index + 1][-1])
        topic = int(contents[index + 2][-1])
        question = ""

        i = index + 3
        line = contents[i]
        while line != "===":
            if line[-1] == "-":
                question = question + line[:-1]
            else:
                question = question + line + " "
            i += 1
            line = contents[i]

        questions.append(question)
        q_number = len(questions) - 1
        dt_map[q_number] = (topic, difficulty)
        contents = contents[i + 1:]

    return questions, dt_map
