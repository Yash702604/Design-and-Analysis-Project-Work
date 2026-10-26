import sys
from bisect import bisect_left, bisect_right

P = 1440  # minutes in a day


def parse_time(tok):
    if ":" in tok:
        h, m = tok.split(":")
        return (int(h) * 60 + int(m)) % P
    return int(tok) % P


def in_arc(x, s, e):
    """Is point x inside the circular arc from s to e (clockwise, inclusive)?"""
    return (x - s) % P <= (e - s) % P


def count_in_arc(T, s, e):
    """Number of points of sorted list T inside arc [s, e]."""
    if s <= e:
        return bisect_right(T, e) - bisect_left(T, s)
    return (len(T) - bisect_left(T, s)) + bisect_right(T, e)


def solve(T, lectures):
    """T: free times, lectures: list of (s, e). Returns (count, visit_times) or (-1, [])."""
    T = sorted(set(T))
    m = len(T)
    if not lectures:
        return 0, []
    # Step 1: pick L0 = lecture with fewest free times; fail if some lecture has none.
    best_cnt, L0 = None, None
    for (s, e) in lectures:
        c = count_in_arc(T, s, e)
        if c == 0:
            return -1, []
        if best_cnt is None or c < best_cnt:
            best_cnt, L0 = c, (s, e)
    s0, e0 = L0
    candidates = [t for t in T if in_arc(t, s0, e0)]

    best = (float("inf"), [])
    for t in candidates:
        # Step 2: rotate so that t is at position 0.
        k = bisect_left(T, t)
        shifted = [(x - t) % P for x in T[k:] + T[:k]]   # sorted ascending, shifted[0] = 0
        # Step 3: keep lectures not containing t; they become intervals on a line.
        intervals = []
        for (s, e) in lectures:
            if in_arc(t, s, e):
                continue
            l, r = (s - t) % P, (e - t) % P              # l <= r because t not in arc
            r_snap = shifted[bisect_right(shifted, r) - 1]  # last free time <= r
            intervals.append((r_snap, l))
        intervals.sort()
        # Step 4: classic greedy (earliest right end).
        visits, last = [t], -1
        for r_snap, l in intervals:
            if l > last:                                  # not yet stabbed
                visits.append((r_snap + t) % P)
                last = r_snap
        if len(visits) < best[0]:
            best = (len(visits), visits)
    return best


def fmt(x):
    return f"{x // 60:02d}:{x % 60:02d}"


def main():
    usage = ("Input format:\n"
             "  n m\n"
             "  t_1 ... t_m        (free times, HH:MM or minutes)\n"
             "  s_1 e_1            (lecture start and end)\n"
             "  ... (n lectures)\n"
             "Example: python3 min_visits.py sample.txt")
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    data = src.read().split()
    if len(data) < 2:
        print("Error: no input received (need at least 'n m').\n" + usage)
        return
    try:
        n, m = int(data[0]), int(data[1])
        if len(data) < 2 + m + 2 * n:
            print(f"Error: expected {2 + m + 2 * n} values but got {len(data)}.\n" + usage)
            return
        T = [parse_time(x) for x in data[2:2 + m]]
        rest = data[2 + m:]
        lectures = [(parse_time(rest[2 * i]), parse_time(rest[2 * i + 1])) for i in range(n)]
    except ValueError:
        print("Error: could not read the numbers/times.\n" + usage)
        return
    cnt, visits = solve(T, lectures)
    if cnt == -1:
        print("-1  (some lecture contains no free time)")
    else:
        print(cnt)
        print("Visit at:", " ".join(fmt(v) for v in sorted(visits)))


if __name__ == "__main__":
    main()
