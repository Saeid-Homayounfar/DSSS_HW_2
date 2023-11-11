import random


def generate_random_integer(min_val, max_val):
    """
    Generate a random integer.
    """
    return random.randint(min_val, max_val)


def generate_operator():
    """
    Generate a random operator.
    """
    return random.choice(['+', '-', '*'])


def generate_problem(n1, n2, operator):
    """
    Generate a math problem.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)
        operator = generate_operator()

        problem, answer = generate_problem(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    print("\n")
   
    if score == total_questions:
        print(f"Congratulations!!! Your point is {score}/{total_questions}. Your performance was excellent!, hope enjoy it")
    elif score == 2:
        print(f"Just a mistake!!! Your point is {score}/{total_questions}. Hope get total points next time!")
    else:
        print(f"You can act better!!! Your point is {score}/{total_questions}. Don't give up and come again!")


if __name__ == "__main__":
    math_quiz()