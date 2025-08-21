# insertDetours.py

import random
from typing import Tuple

from grid import Grid
from .neighbors import neighbors
from .greedyConnect import greedyConnect

def insertDetours(grid: Grid, path: list[Tuple[int,int]], goal: Tuple[int,int], max_detours: int) -> list[Tuple[int,int]]:
    """
    Inserta hasta `max_detours` desvíos cortos en segmentos existentes para diversificar.
    Desvío = 1 ó 2 nodos intermedios válidos, luego retomar hacia el segmento original o reconectar greedy.
    """
    if len(path) < 3 or max_detours <= 0:
        return path[:]
    p = path[:]
    detours = 0
    attempts = 0
    while detours < max_detours and attempts < 8 and len(p) >= 3:
        attempts += 1
        i = random.randrange(1, len(p)-1)   # mutar nodo intermedio
        anchor_prev = p[i-1]
        anchor_next = p[i+1]
        # Probar perturbar el punto p[i] hacia un vecino de anchor_prev o p[i]
        candidates = list(set(neighbors(grid, p[i]) + neighbors(grid, anchor_prev)))
        random.shuffle(candidates)
        chosen = None
        for cand in candidates:
            if cand != anchor_prev and cand != p[i] and cand != anchor_next:
                chosen = cand
                break
        if chosen is None:
            continue
        # Insertar chosen entre prev y next, y si quedó no-vecino de next, reconectar corto
        new_segment = [anchor_prev, chosen]
        if chosen != anchor_next and anchor_next not in neighbors(grid, chosen):
            # reconectar chosen -> anchor_next con greedy (corto)
            recon = greedyConnect(grid, chosen, anchor_next, max_steps=6)
            if not recon or recon[-1] != anchor_next:
                continue  # desvío falló, probá otra cosa
            new_segment += recon  # incluye anchor_next
        else:
            new_segment.append(anchor_next)
        # reconstruir path: ... prev + chosen (+ recon) + next ...
        p = p[:i-1] + new_segment + p[i+2:]
        detours += 1
    return p