import numpy as np
from enum import Enum

class CellState(Enum):
    EMPTY = 0
    UNIGNITED = 1
    BURNING = 2
    BURNED = 3

class FireSimulation:
    """
    A class representing a simple fire spread simulation on a 2D lattice.

    Parameters:
    - N (int): The size of the square lattice (N x N).
    - p (float): The probability of a cell being initially on fire.
    """

    def __init__(self, N, p):
        self.N = N
        self.p = p
        self.grid = self.create_lattice()
        self.to_fire = []

    def create_lattice(self):
        """
        Creates a lattice with cells initialized based on the specified probability.

        Returns:
        - numpy.ndarray: A 2D array representing the initial state of the lattice.
        """

        m = np.zeros((self.N, self.N), dtype=int)
        m[np.random.rand(self.N, self.N) < self.p] = CellState.UNIGNITED.value
        return m

    def begin_fire(self):
        for column in range(self.N):
            if self.grid[0][column] == CellState.UNIGNITED.value:
                self.grid[0][column] = CellState.BURNING.value

    def spread_fire(self):
        """
        Propagates the fire to neighboring cells based on predefined rules.
        """
        self.to_fire.clear()  # Clear the list before populating it again
        for column in range(self.N):
            for row in range(self.N):
                if self.grid[row][column] == CellState.BURNING.value:
                    if (column < self.N - 1) and self.grid[row][column + 1] == CellState.UNIGNITED.value:
                        self.grid[row][column + 1] = CellState.BURNING.value
                    if (row < self.N - 1) and self.grid[row + 1][column] == CellState.UNIGNITED.value:
                        self.grid[row + 1][column] = CellState.BURNING.value
                    if (row > 0) and self.grid[row - 1][column] == CellState.UNIGNITED.value:
                        self.to_fire.append((row - 1, column))
                    if (column > 0) and self.grid[row][column - 1] == CellState.UNIGNITED.value:
                        self.to_fire.append((row, column - 1))

    def spread_fire_next_time(self):
        for element in self.to_fire:
            self.grid[element[0]][element[1]] = CellState.BURNING.value

    def simulate_fire_spread(self, steps):
        """
        Simulates the spread of fire over a specified number of time steps.

        Args:
        - steps (int): The number of time steps to simulate.
        """
        grid_configs = [np.copy(self.grid)] 
        self.begin_fire()
        for _ in range(steps):
            self.spread_fire()
            grid_configs.append(np.copy(self.grid))
            self.grid[self.grid == CellState.BURNING.value] = CellState.BURNED.value
            self.spread_fire_next_time()
            # Check if there are no more burning states or at least one burning state in the last row
            if not any(CellState.BURNING.value in row for row in self.grid[:-1]) or CellState.BURNING.value in self.grid[-1]:
                break
        return grid_configs

if __name__ == "__main__":
    # Example usage:
    N = 10
    p = 0.3
    steps = 5

    simulation = FireSimulation(N, p)
    simulation.simulate_fire_spread(steps)

