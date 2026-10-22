
print("=== Self-Review Assistant ===")

# 1. Receive a task or topic
task = input("Enter a task or topic: ").strip()

MAX_RETRIES = 3
attempt = 0

# 2. Generate the initial solution
solution = "I will explain " + task + "."

while attempt <= MAX_RETRIES:

    print("\nGenerated response:", solution)

    # 3. Critic evaluates the response
    word_count = len(solution.split())

    if word_count >= 10:
        print("\nCritic: PASS")
        print("Validated result:", solution)
        break

    else:
        print("\nCritic: REVISE")

        if attempt == MAX_RETRIES:
            print("Retry limit reached.")
            print("Could not validate the response.")
            break

        # Regenerate the response
        solution = (
            f"{task} is an important topic to learn. "
            f"Start by understanding the basics of {task}. "
            f"Practice simple examples and review what you learn."
        )

        attempt += 1
        print("Retry attempt:", attempt)

print("\nProject completed!")
