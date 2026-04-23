import csv
from datetime import datetime
from pathlib import Path
import subprocess

class Log:
    def __init__(self, app_name="Drawer Counter", filename="drawer_log.csv"):
        self.app_name = app_name
        self.filename = filename
        self.last_logged_data = None

        self.log_dir = Path.home() / "Library" / "Application Support" / self.app_name
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.log_file = self.log_dir / self.filename


    def write_row(self, data):
        file_exists = self.log_file.exists()

        compare_data = data.copy()
        compare_data.pop("timestamp", None)

        if compare_data == self.last_logged_data:
            return

        self.last_logged_data = compare_data

        with open(self.log_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)


    def make_entry(self, values):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **values
        }
        return entry


    def open_log(self):
        if self.log_file.exists():
            subprocess.run(["open", str(self.log_file)])


    def read_log(self):
        if not self.log_file.exists():
            return []

        with open(self.log_file, newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
