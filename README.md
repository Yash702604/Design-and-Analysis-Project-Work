# Design-and-Analysis-Project-Work
This page contains all the instructions required to implement the code in python language. This will also show some test cases as examples.

# Minimum Supervisor Visits

Finds the minimum number of visits a supervisor must make, at the given free times, so that every lecture (including ones that wrap past midnight) is checked at least once.

## Requirements

- Python 3.6 or newer (standard library only, nothing to install)

## Run

From the files in the main: 

- Open min_visits.py
- Copy the code written in the file. 
- Open Python 3.6 or newer and paste the code in there.
- Then execute the code.


## Input format

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

### Example (`sample.txt`)

```
5 5
00:00 04:00 08:00 12:00 16:00
00:00 04:00
04:00 08:00
08:00 12:00
12:00 16:00
16:00 00:00
```

## Output

```
3
Visit at: 00:00 08:00 16:00
```

- First line: the minimum number of visits
- Second line: one optimal set of visit times
- If some lecture contains no free time, the output is `-1  (some lecture contains no free time)`

