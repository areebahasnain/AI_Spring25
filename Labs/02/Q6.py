class FirefightingRobot:
    def __init__(self):
        self.environment = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']  # Predefined movement path
        self.current_position = 'a'

    def display_environment(self):
        print(f"[{self.get_symbol('a')}][{self.get_symbol('b')}][{self.get_symbol('c')}]")
        print(f"[{self.get_symbol('d')}][{self.get_symbol('e')}][{self.get_symbol('f')}]")
        print(f"[{self.get_symbol('g')}][{self.get_symbol('h')}][{self.get_symbol('j')}]")

    def get_symbol(self, room):
        return "🔥" if self.environment[room] == "fire" else " "

    def move_and_extinguish(self):
        for room in self.path:
            self.current_position = room
            print(f"\nRobot moved to Room {room.upper()}")
            if self.environment[room] == "fire":
                print("Fire detected! Extinguishing...")
                self.environment[room] = "safe"
            self.display_environment()

        print("\nAll fires extinguished.")
        self.display_environment()


robot = FirefightingRobot()
robot.move_and_extinguish()
