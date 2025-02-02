import random

class HospitalEnvironment:
    def __init__(self):
        self.patient_rooms = {
            "Room_101": "Patient_A",
            "Room_102": "Patient_B",
            "Room_103": "Patient_C"
        }
        self.nurse_stations = ["Nurse_Station_1", "Nurse_Station_2"]
        self.medicine_storage = {"Medicine_A": 10, "Medicine_B": 5, "Medicine_C": 8}
        self.patient_schedules = {
            "Patient_A": {"Medicine": "Medicine_A", "Time": "10:00 AM"},
            "Patient_B": {"Medicine": "Medicine_B", "Time": "11:00 AM"},
            "Patient_C": {"Medicine": "Medicine_C", "Time": "12:00 PM"}
        }
        self.staff_available = random.choice([True, False])
        self.locations = ["Medicine Storage"] + list(self.patient_rooms.keys()) + self.nurse_stations

    def get_patient_info(self, room):
        return self.patient_rooms.get(room)

    def get_medicine_availability(self, medicine):
        return self.medicine_storage.get(medicine, 0) > 0

    def reduce_medicine_stock(self, medicine):
        if self.medicine_storage.get(medicine, 0) > 0:
            self.medicine_storage[medicine] -= 1

    def is_staff_available(self):
        return random.choice([True, False])


class DeliveryRobot:
    def __init__(self, environment):
        self.environment = environment
        self.current_location = "Nurse_Station_1"
        self.carrying_medicine = None

    def move_to(self, destination):
        if destination in self.environment.locations:
            print(f"Moving to {destination}...")
            self.current_location = destination
        else:
            print(f"Error: {destination} is not a valid location!")

    def pick_up_medicine(self, medicine):
        if self.environment.get_medicine_availability(medicine):
            self.carrying_medicine = medicine
            self.environment.reduce_medicine_stock(medicine)
            print(f"Picked up {medicine} from Medicine Storage.")
        else:
            print(f"{medicine} is out of stock!")

    def scan_patient_id(self, room):
        patient = self.environment.get_patient_info(room)
        if patient:
            print(f"Scanning ID for {patient}... Verified.")
            return True
        print("ID Scan Failed! Alerting staff...")
        self.alert_staff()
        return False

    def deliver_medicine(self, room):
        if self.carrying_medicine:
            if self.scan_patient_id(room):
                print(f"Delivering {self.carrying_medicine} to {self.environment.get_patient_info(room)} in {room}.")
                self.carrying_medicine = None
            else:
                print("Delivery aborted: ID verification failed.")
        else:
            print("Delivery failed: No medicine being carried.")

    def alert_staff(self):
        if not self.environment.is_staff_available():
            print("STAFF ALERT: Emergency situation detected! Assistance needed.")
        else:
            print("Staff notified for assistance.")

    def execute_delivery(self, room, medicine):
        print(f"\nStarting delivery for {room}...")
        self.move_to("Medicine Storage")
        self.pick_up_medicine(medicine)

        if self.carrying_medicine:
            self.move_to(room)
            self.deliver_medicine(room)

            if not self.environment.is_staff_available():
                self.alert_staff()

        print("Delivery completed.\n")



hospital = HospitalEnvironment()
robot = DeliveryRobot(hospital)

for room, patient in hospital.patient_rooms.items():
    schedule = hospital.patient_schedules[patient]
    print(f"Scheduled delivery for {patient} in {room} at {schedule['Time']}.")
    robot.execute_delivery(room, schedule["Medicine"])
