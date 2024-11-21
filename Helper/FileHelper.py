import csv
from pathlib import Path


def write_data(data) -> bool:
  is_create_file: bool = False
  if not Path("Datas/TimeSheet.csv").exists():
    is_create_file = True

  with open("Datas/TimeSheet.csv", "a", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    if is_create_file:
      writer.writeheader()
    writer.writerow(data)

  return True
