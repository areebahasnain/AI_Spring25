import random

class Server:
    def __init__(self, name):
        self.name = name
        self.load_state = random.choice(["Underloaded", "Balanced", "Overloaded"])

    def __str__(self):
        return f"Server {self.name}: {self.load_state}"


class LoadBalancer:
    def __init__(self):
        # initialize 5 servers with random load states
        self.servers = [Server(f"S{i + 1}") for i in range(5)]

    def display_system_state(self, message):
        # display the current load state of all servers
        print(f"\n{message}:")
        for server in self.servers:
            print(server)

    def balance_load(self):
        # redistribute load from overloaded to underloaded servers
        overloaded_servers = [s for s in self.servers if s.load_state == "Overloaded"]
        underloaded_servers = [s for s in self.servers if s.load_state == "Underloaded"]

        print("\nBalancing Load:")
        while overloaded_servers and underloaded_servers:
            overloaded = overloaded_servers.pop(0)  # Take first overloaded server
            underloaded = underloaded_servers.pop(0)  # Take first underloaded server

            # Balance both servers
            overloaded.load_state = "Balanced"
            underloaded.load_state = "Balanced"

            print(f"Moved tasks from {overloaded.name} to {underloaded.name}. Both are now Balanced.")

    def run(self):
        self.display_system_state("Initial Server Load")
        self.balance_load()
        self.display_system_state("Final Server Load")


agent = LoadBalancer()
agent.run()
