import random
import time


def get_integer_input(prompt, min_val=None):
    """Get validated integer input from user."""
    while True:
        user_input = input(prompt).strip().lower()

        if user_input in ['q', 'quit', 'exit']:
            return None

        try:
            value = int(user_input)
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number or 'q' to quit")


def get_practice_ranges():
    """Get practice ranges from user."""
    print("\nMultiplication Table Trainer")
    print("-" * 30)
    print("Set up your practice ranges (type 'q' to quit):")

    min_a = get_integer_input("First number minimum: ", min_val=0)
    if min_a is None:
        return None

    max_a = get_integer_input(f"First number maximum (≥{min_a}): ", min_val=min_a)
    if max_a is None:
        return None

    min_b = get_integer_input("Second number minimum: ", min_val=0)
    if min_b is None:
        return None

    max_b = get_integer_input(f"Second number maximum (≥{min_b}): ", min_val=min_b)
    if max_b is None:
        return None

    print(f"\nPracticing: ({min_a}-{max_a}) × ({min_b}-{max_b})")
    print("Type 'q' anytime to quit\n")

    return min_a, max_a, min_b, max_b


def ask_question(min_a, max_a, min_b, max_b):
    """Ask a single multiplication question. Returns (continue, correct)."""
    time.sleep(0.1)

    num1 = random.randint(min_a, max_a)
    num2 = random.randint(min_b, max_b)
    correct_answer = num1 * num2

    user_input = input(f"{num1} × {num2} = ").strip().lower()

    if user_input in ['q', 'quit', 'exit']:
        return False, False

    try:
        user_answer = int(user_input)
        if user_answer == correct_answer:
            time.sleep(0.3)
            print("Correct!")
            return True, True
        else:
            time.sleep(0.3)
            print(f"Wrong. The answer is {correct_answer}")
            return True, False
    except ValueError:
        print("Please enter a valid number or 'q' to quit")
        return True, False


def practice_session(min_a, max_a, min_b, max_b):
    """Run a practice session and return (correct, total) scores."""
    correct = 0
    total = 0

    try:
        while True:
            continue_playing, is_correct = ask_question(min_a, max_a, min_b, max_b)
            if not continue_playing:
                break
            total += 1
            if is_correct:
                correct += 1
    except KeyboardInterrupt:
        print("\nSession interrupted")

    return correct, total


def main():
    """Main program loop."""
    print("Welcome to Multiplication Table Trainer!")

    total_correct = 0
    total_questions = 0

    try:
        while True:
            ranges = get_practice_ranges()
            if ranges is None:
                break

            min_a, max_a, min_b, max_b = ranges
            correct, questions = practice_session(min_a, max_a, min_b, max_b)

            total_correct += correct
            total_questions += questions

            if questions > 0:
                accuracy = (correct / questions) * 100
                print(f"\nSession: {correct}/{questions} correct ({accuracy:.1f}%)")

            if input("\nNew session? (y/n): ").strip().lower() not in ['y', 'yes', '']:
                break

    except KeyboardInterrupt:
        print("\nProgram interrupted")

    if total_questions > 0:
        overall_accuracy = (total_correct / total_questions) * 100
        print(f"\nOverall: {total_correct}/{total_questions} correct ({overall_accuracy:.1f}%)")

    print("Thanks for practicing!")


if __name__ == "__main__":
    main()
