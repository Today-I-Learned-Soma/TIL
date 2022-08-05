from calendar import month
from pathlib import Path
import pandas as pd

def list_subdir(dir):
    subdirs = filter( Path.is_dir, dir.iterdir() )
    return [ *sorted(subdirs) ]

def dir_contains_file(dir, file):
    return (dir / file).is_file()

CURR_DIR = Path(__file__).parent
YEAR_DIR = CURR_DIR / "2022"

BOOL_TO_EMOJI = ["❌", "⭕️"]
WRITERS = ["woosuk", "soyeon", "hyunjo", "jonghyuk"]

attendance = { writer:[] for writer in WRITERS }
total_day_dirs = []

for month_dir in list_subdir(YEAR_DIR):
    if not month_dir.is_dir():
        pass

    day_dirs = list_subdir(month_dir)
    total_day_dirs += day_dirs

    for day_dir in day_dirs:
        for idx, writer in enumerate(WRITERS):
            did_write = dir_contains_file(day_dir, f"{writer}.md")
            attendance[writer].append(did_write)

attendance_df = pd.DataFrame(data=attendance, index=total_day_dirs)

print_df = attendance_df.applymap( lambda x: BOOL_TO_EMOJI[x] )
print_df.index = print_df.index.map( lambda x: x.name )

print(print_df.to_markdown(stralign="center"))