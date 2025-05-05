#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------
#Hello
import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("How many bones are there in the adult human body?","206"),
        ("Which planet is known as the 'Red Planet'?","Mars"),
        # Add more questions as tuples (question, answer)
    ], 
    "History": [("What year did world war II end?","1945"),
                ("Which wall came down in 1989?","Berlin Wall"),
                ("Who was the first president of the United States?","George Washington"),
    ],
    "Geography": [("What is the captial of Canada?","Ottawa"),
                  ("Which continent is the Sahara Desert in?","Africa"),
                  ("Which is the largest ocean in the world?","Pacific Ocean"),
    ],
    "Pop Culture": [("Who played Iron Man in Marvel movies?","Robert Downey Jr."),
                    ("Which series features a character named Eleven?","Stranger Things"),
                    ("What movie features the song 'Let It Go'?","Frozen"),
    ]
}

hints = {
    "Science": ["It contains Hydrogen and Oxygen.",
                "A little more than 200."
                "It is the fourth planet from the Sun.",
                ],
    "History" : ["It ended after the surrender of Germany and Japan."
                 "It divided East and West Germany."
                 "He appears on the US one-dollar bill.",
                ],
    "Geography" : ["Not Toronto.",
                   "It starts with the letter A.",
                   "It's named after peace.",
                ],
    "Pop Culture" : ["His initials are RDJ.",
                     "The title has two words and involves strange events.",
                     "It's a Disney movie featuring Elsa.",
                ]
        # Pair each question with a corresponding hint.
    
    # Repeat for other categories as needed.
} 

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    if category in questions and questions[category]:
        return random.choice(questions[category])
    else:
        print("No questions avaliable in this category.")
        return None, None
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return player_answer.strip().lower() == correct_answer.strip().lower()
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    for q in questions[category]:
        if q[0] == question:
            questions[category].remove(q)
            break
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Question: {question}")
    return input("Your Answer: ")
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    idx = None
    if category in questions:
        for i, q in enumerate(questions[category]):
            if q[0] == question:
                idx = i
                break
    if idx is not None and idx < len(hints[category]):
        return hints[category][idx]
    else:
        return "No hint avaliable."

    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"The correct answer was: {correct_answer}")
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------


