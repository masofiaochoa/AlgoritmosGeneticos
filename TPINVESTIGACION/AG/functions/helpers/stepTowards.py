# stepTowards.py

from typing import Tuple, Optional

def distance(a: Tuple[int,int], b: Tuple[int,int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def stepTowards(goal: Tuple[int,int], options: list[Tuple[int,int]]) -> Optional[Tuple[int,int]]:
    # Elige el vecino que más acerca al goal (heurística Manhattan).
    if not options:
        return None
    return min(options, key=lambda p: distance(p, goal))