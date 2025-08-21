from typing import Tuple

class Grid:
    def __init__(self, rows: int, cols: int, cell_size: float, start: Tuple[int, int], goal: Tuple[int, int]):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.start = start
        self.goal = goal

    def get_start(self) -> Tuple[int, int]:
        return self.start

    def get_goal(self) -> Tuple[int, int]:
        return self.goal

    def in_bounds(self, position: Tuple[int, int]) -> bool:
        row, col = position
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_obstacle(self, position: Tuple[int, int]) -> bool:
        # Implement obstacle detection logic
        return False

    def apply_current(self, position: Tuple[int, int], step_idx: int) -> Tuple[int, int]:
        # Implement current application logic
        return position

    def wind_at(self, position1: Tuple[int, int], position2: Tuple[int, int]) -> Tuple[float, float]:
        # Implement wind detection logic
        return 0.0, 0.0

    def __str__(self) -> str:
        return f"Grid:(\n\t Cantidad Filas: {self.rows},\n\tCantidad Columnas: {self.cols},\n\tTamaño Celda: {self.cell_size},\n\tInicio: {self.start},\n\tMeta: {self.goal})"
