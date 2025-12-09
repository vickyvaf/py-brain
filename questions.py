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
    },
    {
        "id": 6,
        "question": "Which method adds an element to the end of a list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": "append()"
    },
    {
        "id": 7,
        "question": "How do you check if key 'k' exists in dictionary 'd'?",
        "options": ["k in d", "d.has(k)", "exists(k, d)", "d.contains(k)"],
        "answer": "k in d"
    },
    {
        "id": 8,
        "question": "What signifies a block of code in Python?",
        "options": ["Brackets {}", "Indentation", "Semicolons ;", "Keywords"],
        "answer": "Indentation"
    },
    {
        "id": 9,
        "question": "Which statement stops a loop completely?",
        "options": ["stop", "return", "break", "continue"],
        "answer": "break"
    },
    {
        "id": 10,
        "question": "What function gives the length of a list?",
        "options": ["count()", "size()", "len()", "length()"],
        "answer": "len()"
    },
    {
        "id": 11,
        "question": "Which operator returns True only if both operands are True?",
        "options": ["or", "not", "and", "xor"],
        "answer": "and"
    },
    {
        "id": 12,
        "question": "Which character starts a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "id": 13,
        "question": "What does range(3) generate?",
        "options": ["1, 2, 3", "0, 1, 2", "1, 2", "0, 1, 2, 3"],
        "answer": "0, 1, 2"
    },
    {
        "id": 14,
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple"
    },
    {
        "id": 15,
        "question": "Which keyword is used to bring a library into your code?",
        "options": ["include", "using", "import", "require"],
        "answer": "import"
    },
    {
        "id": 16,
        "question": "What corresponds to the constructor method in a class?",
        "options": ["__init__", "__new__", "constructor", "init"],
        "answer": "__init__"
    },
    {
        "id": 17,
        "question": "Which library is famous for Machine Learning algorithms?",
        "options": ["Django", "Scikit-learn", "Flask", "BeautifulSoup"],
        "answer": "Scikit-learn"
    },
    {
        "id": 18,
        "question": "What is the basic processing unit of a Neural Network?",
        "options": ["Electron", "Neuron", "Pixel", "Kernel"],
        "answer": "Neuron"
    },
    {
        "id": 19,
        "question": "Which is an example of Supervised Learning?",
        "options": ["Clustering", "Spam Classification", "Reinforcement Learning", "Dimensionality Reduction"],
        "answer": "Spam Classification"
    },
    {
        "id": 20,
        "question": "What is 'pip' used for?",
        "options": ["Running Python", "Installing packages", "Writing code", "Debugging"],
        "answer": "Installing packages"
    },
    {
        "id": 21,
        "question": "What is the output of 'Python'[0]?",
        "options": ["P", "y", "n", "Error"],
        "answer": "P"
    },
    {
        "id": 22,
        "question": "How do you check a variable's type?",
        "options": ["typeof()", "type()", "check()", "class()"],
        "answer": "type()"
    },
    {
        "id": 23,
        "question": "Which block catches errors in Python?",
        "options": ["if/else", "try/except", "do/catch", "try/catch"],
        "answer": "try/except"
    },
    {
        "id": 24,
        "question": "Which mode opens a file for writing, erasing existing content?",
        "options": ["'r'", "'a'", "'w'", "'x'"],
        "answer": "'w'"
    },
    {
        "id": 25,
        "question": "What causes a while loop to run forever?",
        "options": ["Condition is False", "break statement", "Condition is always True", "continue statement"],
        "answer": "Condition is always True"
    }
]

def get_question(q_id):
    for q in questions_data:
        if q['id'] == q_id:
            return q
    return None
