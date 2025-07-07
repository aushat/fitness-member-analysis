class Member:
    def __init__(self, name, weight, height, heart_rate):
        self.name = name
        self.weight = weight
        self.height = height
        self.heart_rate = heart_rate
        self.bmi = self.calculate_bmi()
        self.bmi_category = self.get_bmi_category()
        self.fitness_level = self.get_fitness_level()
        self.workout_preference = self.get_workout_preference()

    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def get_bmi_category(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif bmi <= 24.9:
            return "Healthy weight"
        elif bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"

    def get_fitness_level(self):
        hr = self.heart_rate
        if hr < 60:
            return "Athlete"
        elif hr <= 72:
            return "Good"
        elif hr <= 84:
            return "Acceptable"
        else:
            return "Needs improvement"

    def get_workout_preference(self):
        if (self.bmi_category in ["Underweight", "Obese"]) and self.fitness_level == "Needs improvement":
            return "Mixed workout with cardio emphasis"
        elif self.bmi_category == "Healthy weight" and self.fitness_level == "Athlete":
            return "Strength training emphasis"
        else:
            return "Balanced workouts"

def get_valid_input(prompt, min_value, max_value, value_type=float):
    while True:
        try:
            value = value_type(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a valid value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_summary(members):
    print("\nSummary of Member Fitness and Workout Recommendations:")
    print("      | %-10s | %-6s | %-20s | %-30s" % ('Name', 'BMI', 'Heart Rate', 'Workout'))
    print("-"*80)
    for idx, member in enumerate(members, 1):
        print("%d     | %-10s | %-6.2f | %-20d | %-30s" %
              (idx, member.name, member.bmi, member.heart_rate, member.workout_preference))

def list_needing_approval(members):
    print("\nMembers requiring physician's approval:")
    for member in members:
        if member.heart_rate > 84:
            print(f"{member.name} with a resting heart rate of {member.heart_rate} bpm")

def print_member_details(members):
    name = input("Enter the member's name: ")
    for member in members:
        if member.name.lower() == name.lower():
            print(f"\nDetails for {member.name}:")
            print(f"BMI: {member.bmi:.2f}")
            print(f"Resting Heart Rate: {member.heart_rate} bpm")
            print(f"Workout Preference: {member.workout_preference}")
            return
    print("Member not found.")

def main():
    print("*" * 70)
    print("\nWelcome to the Fitness Member Analysis System!")
    print("We help trainers understand members better.\n")
    print("*" * 70)

    members = []
    amt = get_valid_input("How many gym members do you want to analyze? ", 1, 100, int)

    for i in range(amt):
        name = input(f"\nEnter member {i+1} name: ")
        weight = get_valid_input(f"Enter {name}'s weight (20kg - 200kg): ", 20, 200)
        height = get_valid_input(f"Enter {name}'s height in cm (50 - 250 cm): ", 50, 250)
        heart_rate = get_valid_input(f"Enter {name}'s resting heart rate (30 - 200 bpm): ", 30, 200, int)

        member = Member(name, weight, height, heart_rate)
        members.append(member)

    while True:
        print("\nWhat would you like to do next?")
        print("1. Print summary")
        print("2. List members needing physician approval")
        print("3. Print specific member details")
        print("4. Exit")

        option = input("Choose an option (1/2/3/4): ")

        if option == "1":
            print_summary(members)
        elif option == "2":
            list_needing_approval(members)
        elif option == "3":
            print_member_details(members)
        elif option == "4":
            print("\nThank you for using the Fitness Member Analysis System!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


