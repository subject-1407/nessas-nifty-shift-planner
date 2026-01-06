# Nessas Nifty Shift Planner

A Python tool to efficiently plan shifts for volunteers at an event my wife is co-hosting, taking into account the following aspects:
- Employee availability
- Friend preferences
- Minimum staff per shift
- Fair distribution of work

Features:

- CSV input for employee schedules
- Handles friend grouping for shifts
- Automatically fills shifts based on availability and requirements
- Prints clear schedule and remaining shifts per employee

Due to the complexity of the helpers, it cannot be guaranteed that every shift will be filled. For this reason, the tool prints how many shifts may still be available for manual rework.  

Unfortunately, I use constants according to my requirements. These have to be adjusted if necessary.

---

## Usage

Run the tool:
```bash
python3 ./nessas-nifty-shift-planner/main.py employees.csv
```

An example csv can be found at `docs/employees.csv`.

---

## Todo

- Change constants into a config file
- Output csv for easier manual rework
- Decompose main.py into modules for easier maintenance

_Will probably work on this the next time I need it._

---

## License

[MIT](https://choosealicense.com/licenses/mit/) 
