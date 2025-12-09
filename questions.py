questions_data = [
    {
        "id": 1,
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "id": 2,
        "question": "Which library is commonly used for data manipulation in Python?",
        "options": ["Pandas", "Requests", "Flask", "PyGame"],
        "answer": "Pandas"
    },
    {
        "id": 3,
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "id": 4,
        "question": "Which of these is NOT a valid variable name in Python?",
        "options": ["my_var", "_var", "2var", "var2"],
        "answer": "2var"
    },
    {
        "id": 5,
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "Automated Interface", "Apple Inc", "Advanced Iteration"],
        "answer": "Artificial Intelligence"
    }
]

def get_question(q_id):
    for q in questions_data:
        if q['id'] == q_id:
            return q
    return None
