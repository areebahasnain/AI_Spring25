import random

class SecuritySystem:
    def __init__(self):
        # Initialize the system with 9 components (A through I)
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # Randomly assign each component as 'safe' or 'vulnerable'
        self.system_state = {component: random.choice(['safe', 'vulnerable']) for component in self.components}

    def display_state(self, message):
        # Display the current state of the system
        print(f"\n{message}:")
        for component, state in self.system_state.items():
            print(f"Component {component}: {state}")

    def scan_system(self):
        # Scan the system and identify vulnerable components
        vulnerable_components = []
        print("\nSystem Scan Results:")
        for component, state in self.system_state.items():
            if state == 'vulnerable':
                print(f"Warning: Component {component} is vulnerable.")
                vulnerable_components.append(component)
            else:
                print(f"Success: Component {component} is secure.")
        return vulnerable_components

    def patch_vulnerabilities(self, vulnerable_components):
        # Patch all vulnerable components
        print("\nPatching Vulnerabilities:")
        for component in vulnerable_components:
            self.system_state[component] = 'safe'
            print(f"Component {component} has been patched and is now safe.")


class SecurityAgent:
    def __init__(self):
        self.system = SecuritySystem()

    def run_exercise(self):
        self.system.display_state("Initial System State")
        vulnerable_components = self.system.scan_system()
        if vulnerable_components:
            self.system.patch_vulnerabilities(vulnerable_components)
        else:
            print("\nNo vulnerabilities found. System is secure.")

        self.system.display_state("Final System State")


agent = SecurityAgent()
agent.run_exercise()
