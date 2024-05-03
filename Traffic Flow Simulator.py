import json

class TrafficFlowSimulator:
    def _init_(self):
        self.traffic_data = {}

    def load_traffic_data_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.traffic_data = json.load(file)
            print("Traffic data loaded successfully.")
        except FileNotFoundError:
            print("File not found. No traffic data loaded.")
        except json.JSONDecodeError:
            print("Error decoding JSON. No traffic data loaded.")

    def save_traffic_data_to_file(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.traffic_data, file)
        print("Traffic data saved successfully.")

    def create_traffic_data(self, condition_id, data):
        self.traffic_data[condition_id] = data
        print(f"Traffic data created for condition ID {condition_id}")

    def update_traffic_data(self, condition_id, updated_data):
        if condition_id in self.traffic_data:
            self.traffic_data[condition_id] = updated_data
            print(f"Traffic data updated for condition ID {condition_id}")
        else:
            print(f"No traffic data found for condition ID {condition_id}")

    def simulate_traffic_conditions(self, condition_id):
        if condition_id in self.traffic_data:
            traffic_flow_data = self.traffic_data[condition_id]
            print(f"Simulating traffic conditions for condition ID {condition_id}")
        else:
            print(f"No traffic data found for condition ID {condition_id}")

    def suggest_traffic_management_solutions(self, solution_id):
        suggestions = {
            1: "Implement traffic signals at key intersections.",
            2: "Introduce roundabouts to improve traffic flow.",
            3: "Install traffic cameras for real-time monitoring."
        }
        if solution_id in suggestions:
            print(f"Suggested solution: {suggestions[solution_id]}")
        else:
            print(f"No solution found for solution ID {solution_id}")

    def analyze_traffic_conditions(self):
        print("Analyzing traffic conditions...")
        # Add analysis logic here

    def delete_traffic_data(self, condition_id):
        if condition_id in self.traffic_data:
            del self.traffic_data[condition_id]
            print(f"Traffic data deleted for condition ID {condition_id}")
        else:
            print(f"No traffic data found for condition ID {condition_id}")

# Example usage with file handling:
simulator = TrafficFlowSimulator()

while True:
    print("1. Create traffic data")
    print("2. Update traffic data")
    print("3. Simulate traffic conditions")
    print("4. Suggest traffic management solutions")
    print("5. Analyze traffic conditions")
    print("6. Delete traffic data")
    print("7. Save traffic data to file")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        condition_id = int(input("Enter condition ID: "))
        data = input("Enter traffic data: ")
        simulator.create_traffic_data(condition_id, data)
    elif choice == 2:
        condition_id = int(input("Enter condition ID to update: "))
        updated_data = input("Enter updated traffic data: ")
        simulator.update_traffic_data(condition_id, updated_data)
    elif choice == 3:
        condition_id = int(input("Enter condition ID to simulate: "))
        simulator.simulate_traffic_conditions(condition_id)
    elif choice == 4:
        solution_id = int(input("Enter solution ID to suggest: "))
        simulator.suggest_traffic_management_solutions(solution_id)
    elif choice == 5:
        simulator.analyze_traffic_conditions()
    elif choice == 6:
        condition_id = int(input("Enter condition ID to delete: "))
        simulator.delete_traffic_data(condition_id)
    elif choice == 7:
        file_name = input("Enter file name to save traffic data: ")
        simulator.save_traffic_data_to_file(file_name)
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")
