import random


class SecuritySystem:
    def __init__(self):
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.vulnerability_levels = ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"]
        self.system_state = {comp: random.choice(self.vulnerability_levels) for comp in self.components}

    def display_state(self, message):
        print(f"\n{message}:")
        for component, state in self.system_state.items():
            print(f"Component {component}: {state}")

    def scan_system(self):
        low_risk = []
        high_risk = []

        print("\nSystem Scan Results:")
        for component, state in self.system_state.items():
            if state == "Low Risk Vulnerable":
                print(f"Warning: {component} has a LOW risk vulnerability.")
                low_risk.append(component)
            elif state == "High Risk Vulnerable":
                print(f"ALERT: {component} has a HIGH risk vulnerability! Premium service required.")
                high_risk.append(component)
            else:
                print(f"Success: {component} is Safe.")

        return low_risk, high_risk

    def patch_vulnerabilities(self, low_risk_components):
        print("\nPatching Low Risk Vulnerabilities:")
        for component in low_risk_components:
            self.system_state[component] = "Safe"
            print(f"{component} has been patched and is now Safe.")

    def run_security_check(self):
        self.display_state("Initial System State")
        low_risk, high_risk = self.scan_system()

        if low_risk:
            self.patch_vulnerabilities(low_risk)
        else:
            print("\nNo Low Risk Vulnerabilities found.")

        if high_risk:
            print("\nSome High Risk Vulnerabilities remain! Premium service is required to patch them.")
        else:
            print("\nAll components are secure!")

        self.display_state("Final System State")


security_agent = SecuritySystem()
security_agent.run_security_check()
