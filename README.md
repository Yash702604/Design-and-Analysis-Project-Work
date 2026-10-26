# Design-and-Analysis-Project-Work
This page contains all the instructions required to implement the code in python language. This will also show some test cases as examples.

# Minimum Supervisor Visits

Finds the minimum number of visits a supervisor must make, at the given free times, so that every lecture (including ones that wrap past midnight) is checked at least once.

## Requirements

- Python 3.6 or newer.

## Run

- From the files in the main, open min_visits.py.
- Save the code as `min_visits.py` in a folder of your choice (for example `min_visits_project`).
- In the same folder, create a .txt file (say, `sample.txt`) which is used to store the input.

```
n m
t_1 t_2 ... t_m
s_1 e_1
...
s_n e_n
```

- `n` = number of lectures, `m` = number of free times
- Second line: the `m` free times
- Next `n` lines: start and end of each lecture
- Times can be `HH:MM` or minutes since midnight (`0` to `1439`)
- If start is later than end, the lecture wraps past midnight (e.g. `23:00 01:00`)

- Open your Windows terminal, and use the code `python --version` or `py --version` to check whether you have required version of Python.
- If you have the desired version of Python in Windows, then open the folder containing `min_visits_project` in terminal. You can achieve this by opening the folder in file explorer and then using shortcut keys `Alt+D` and then typing cmd or powershell.
- After this, we use the command:
  `bash      cd min_visits_project`.
- Then, we use the final command `python3 min_visits.py sample.txt` or `python min_visits.py sample.txt` or `py min_visits.py sample.txt` for executing the code with the input `sample.txt`.
- You can then interpret the output in the following manner:
  -1 means that no visits are possible, otherwise
  m
  Visits at: ...   , where m denotes the minimum number of visits required and the second line shows the time of such visits.

