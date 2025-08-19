class Grid:
    def __init__(self, rows: int, cols: int, cell_size: float, start: tuple[int, int], goal: tuple[int, int]):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.start = start
        self.goal = goal

    def start(self) -> tuple[int, int]:
        return self.start

    def goal(self) -> tuple[int, int]:
        return self.goal

    def in_bounds(self, position: tuple[int, int]) -> bool:
        row, col = position
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_obstacle(self, position: tuple[int, int]) -> bool:
        # Implement obstacle detection logic
        return False

    def apply_current(self, position: tuple[int, int], step_idx: int) -> tuple[int, int]:
        # Implement current application logic
        return position

    def wind_at(self, position1: tuple[int, int], position2: tuple[int, int]) -> tuple[float, float]:
        # Implement wind detection logic
        return 0.0, 0.0

    def __str__(self) -> str:
        return f"Grid:(\n\t Cantidad Filas: {self.rows},\n\tCantidad Columnas: {self.cols},\n\tTamaño Celda: {self.cell_size},\n\tInicio: {self.start},\n\tMeta: {self.goal})"
