import random

class BackupManager:
    def __init__(self, num_tasks=10):
        self.backup_tasks = {f"Task {i+1}": random.choice(["Completed", "Failed"]) for i in range(num_tasks)}

    def display_backup_status(self, message):
        print(f"\n{message}:")
        for task, status in self.backup_tasks.items():
            print(f"{task}: {status}")

    def retry_failed_backups(self):
        print("\nRetrying Failed Backups:")
        for task, status in self.backup_tasks.items():
            if status == "Failed":
                print(f"Retrying {task}... Success!")
                self.backup_tasks[task] = "Completed"

    def run(self):
        self.display_backup_status("Initial Backup Status")
        self.retry_failed_backups()
        self.display_backup_status("Final Backup Status")


backup_agent = BackupManager(num_tasks=10)
backup_agent.run()
