import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between the given minimum and maximum values.
 
    
    Args:
    - min_value (int): The lower bound of the random number range.
    - max_value (int): The upper bound of the random number range.
    
    Returns:
    - int: A random integer between min_value and max_value.
 
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Selects a random mathematical operator from the list ['+', '-', '*'].
    Returns:
    - str: A randomly selected operator.
 
    """
    return random.choice(['+', '-', '*'])


def generate_problem(n1, n2, operator):
    """
    Generates a math problem and computes the answer based on the operator.
 

    
    Args:
    - n1 (int): The first number in the math problem.
    - n2 (int): The second number in the math problem.
    - operator (str): The mathematical operator ('+', '-', '*').
    
    Returns:
    - tuple: A tuple containing the string representation of the problem and the correct answer.
 
    """
    problem = f"{n1} {operator} {n2}"
    
    # Handling the operation and calculating the correct answer
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:  # operator == '*'
        answer = n1 * n2
    
    return problem, answer


def math_quiz():
    """
    Main function that runs the math quiz game, presenting problems to the user.
    
    In this game, the user will solve simple math problems and receive feedback on their answers.
    """
    score = 0  # Keep track of the player's score
    total_questions = 5  # Set the total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_questions):
        # Generate two random numbers and an operator
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)  # n2 should be an integer, adjusted the range
        operator = generate_random_operator()

        # Generate the problem and get the correct answer
        problem, correct_answer = generate_problem(n1, n2, operator)
        
        print(f"\nQuestion: {problem}")
        
        # Get the user's answer with error handling for invalid input
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)  # Convert the input to an integer
                
                # Break the loop if the input is valid
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        # Check the user's answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1  # Increment score if correct
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
    
    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()