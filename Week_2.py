# Constants
COST_PER_PERSON = {
    "12-16": {"coach": 150, "meal": 14.00, "ticket": 21.00},
    "17-26": {"coach": 190, "meal": 13.50, "ticket": 20.00},
    "27-39": {"coach": 225, "meal": 13.00, "ticket": 19.00}
}
MIN_REQUIRED_PEOPLE = 10
MAX_PEOPLE = 36
MIN_CARERS = 2
ADDITIONAL_CARERS_THRESHOLD = 24
ADDITIONAL_CARERS = 1


# Function to calculate total cost and cost per person
def calculate_cost(num_people):
    if num_people < MIN_REQUIRED_PEOPLE or num_people > MAX_PEOPLE:
        return None, None
    elif num_people <= 16:
        cost_info = COST_PER_PERSON["12-16"]
    elif num_people <= 26:
        cost_info = COST_PER_PERSON["17-26"]
    else:
        cost_info = COST_PER_PERSON["27-39"]

    total_cost = cost_info["coach"]
    total_cost += cost_info["meal"] * num_people
    total_cost += cost_info["ticket"] * num_people

    total_carers = MIN_CARERS + (1 if num_people > ADDITIONAL_CARERS_THRESHOLD else 0)
    total_cost -= total_carers * cost_info["meal"]

    cost_per_person = total_cost / num_people

    return total_cost, cost_per_person


# Task 1
def task_1():
    num_people = int(input("Enter the number of senior citizens interested in the outing: "))
    total_cost, cost_per_person = calculate_cost(num_people)
    if total_cost is None:
        print("Invalid number of people.")
    else:
        print(f"Total cost of the outing: ${total_cost:.2f}")
        print(f"Cost per person: ${cost_per_person:.2f}")


# Task 2
def task_2(total_cost):
    people = []
    total_collected = 0
    while True:
        name = input("Enter the name of the person (leave blank to finish): ").strip()
        if not name:
            break
        amount_paid = float(input(f"Enter the amount paid by {name}: $"))
        people.append((name, amount_paid))
        total_collected += amount_paid

    print("\nList of people on the outing:")
    for name, amount_paid in people:
        print(f"{name}: ${amount_paid:.2f}")

    return total_collected


# Task 3
def task_3(total_cost, total_collected):
    if total_collected >= total_cost:
        print(f"\nThe outing has broken even.")
    else:
        print(f"\nThe outing has made a profit of ${total_collected - total_cost:.2f}.")


# Main function
def main():
    print("TASK 1:")
    task_1()

    total_cost, _ = calculate_cost(int(input("\nEnter the number of senior citizens going on the outing: ")))

    print("\nTASK 2:")
    total_collected = task_2(total_cost)

    print("\nTASK 3:")
    task_3(total_cost, total_collected)


if __name__ == "__main__":
    main()
