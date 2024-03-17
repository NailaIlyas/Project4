# A school keeps records of the weights of each pupil. The weight, in kilograms,
# of each pupil is recorded on the first day of term. Input and store the weights and names
# recorded for a class of 30 pupils. You must store the weights in a one-dimensional array
# and the names in another one dimensional array. All the weights must be validated on
# entry and any invalid weights rejected.
# You must decide your own validation rules. You may assume that the pupils’ names are
# unique. Output the names and weights of the pupils in the class.
#               TASK 1

# def validate_weight(weight):
#     try:
#         weight = float(weight)
#         if weight <= 0:
#             return False
#         return True
#     except ValueError:
#         return False
#
# def main():
#     num_pupils = 30
#     names = []
#     weights = []

#     for i in range(num_pupils):
#         name = input(f"Enter the name of pupil {i + 1}: ")
#         names.append(name)
#
#         while True:
#             weight = input(f"Enter the weight of {name} (in kilograms): ")
#             if validate_weight(weight):
#                 weights.append(float(weight))
#                 break
#             else:
#                 print("Invalid weight. Please enter a valid positive weight.")
#
#     print("\nNames and Weights of Pupils:")
#     for i in range(num_pupils):
#         print(f"{names[i]}: {weights[i]} kg")
# # if __name__ == "__main__":
# #    main()


#             TASK 2

# The weight, in kilograms, of each pupil is recorded again on the last day of term. Calculate and store
# the difference in weight for each pupil.


# def validate_weight(weight):
#     try:
#         weight = float(weight)
#         if weight <= 0:
#             return False
#         return True
#     except ValueError:
#         return False
#
# def main():
#     num_pupils = 30
#     names = []
#     first_day_weights = []
#     last_day_weights = []
#
#     # Input weights for the first day
#     print("Enter weights for the first day:")
#     for i in range(num_pupils):
#         name = input(f"Enter the name of pupil {i + 1}: ")
#         names.append(name)

    #     while True:
    #         weight = input(f"Enter the weight of {name} (in kilograms): ")
    #         if validate_weight(weight):
    #             first_day_weights.append(float(weight))
    #             break
    #         else:
    #             print("Invalid weight. Please enter a valid positive weight.")
    #
    # # Input weights for the last day
    # print("\nEnter weights for the last day:")
    # for i in range(num_pupils):
    #     while True:
    #         weight = input(f"Enter the weight of {names[i]} (in kilograms): ")
    #         if validate_weight(weight):
    #             last_day_weights.append(float(weight))
    #             break
    #         else:
    #             print("Invalid weight. Please enter a valid positive weight.")

    # Calculate and store the difference in weight
#     weight_differences = [last - first for first, last in zip(first_day_weights, last_day_weights)]
#
#     # Output names, weights for the first and last day, and the difference
#     print("\nNames, Weights, and Weight Differences:")
#     for i in range(num_pupils):
#         print(f"{names[i]}: First day - {first_day_weights[i]} kg, Last day - {last_day_weights[i]} kg, Difference - {weight_differences[i]} kg")
#
# if __name__ == "__main__":
#     main()


#                TASK 3

# For those pupils who have a difference in weight of more than 2.5 kilograms, output, with a suitable
# message, the pupil’s name, the difference in weight and whether this is a rise or a fall.
# Your program must include appropriate prompts for the entry of data. Error messages and other
# outputs need to be set out clearly and understandably. All variables, constants and other identifiers
# must have meaningful names. Each task must be fully tested.

def validate_weight(weight):
    try:
        weight = float(weight)
        if 20 <= weight <= 200:  # Assuming weights should be between 20 and 200 kg
            return True
        else:
            print("Invalid weight! Weight should be between 20 and 200 kg.")
            return False
    except ValueError:
        print("Invalid weight! Please enter a valid number.")
        return False

# Initialize arrays
names = []
first_day_weights = []
last_day_weights = []
weight_differences = []

# Input names and weights on the first day
for i in range(1, 31):
    name = input(f"Enter the name of pupil {i}: ")
    weight_input = input(f"Enter the weight of pupil {i} on the first day (in kg): ")

    # Validate weight
    while not validate_weight(weight_input):
        weight_input = input(f"Re-enter the weight of pupil {i} on the first day (in kg): ")

    # Store in array
    names.append(name)
    first_day_weights.append(float(weight_input))

# Input weights on the last day and calculate differences
for i in range(30):
    weight_input = input(f"Enter the weight of pupil {i+1} on the last day (in kg): ")

    # Validate weight
    while not validate_weight(weight_input):
        weight_input = input(f"Re-enter the weight of pupil {i+1} on the last day (in kg): ")

    # Store in array
    last_day_weights.append(float(weight_input))

    # Calculate and store the difference in weight
    weight_difference = last_day_weights[i] - first_day_weights[i]
    weight_differences.append(weight_difference)

# Output names, first-day weights, last-day weights, and differences
print("\nNames, Weights, and Differences:")
for name, first_weight, last_weight, difference in zip(names, first_day_weights, last_day_weights, weight_differences):
    print(f"{name}: First Day - {first_weight} kg, Last Day - {last_weight} kg, Difference - {difference} kg")

# Output pupils with a difference in weight of more than 2.5 kilograms
print("\nPupils with a Difference in Weight of More Than 2.5 Kilograms:")
for name, difference in zip(names, weight_differences):
    if abs(difference) > 2.5:
        status = "rise" if difference > 0 else "fall"
        print(f"{name}: Difference - {abs(difference)} kg, {status}")
