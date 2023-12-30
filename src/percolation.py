import numpy as np


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
        self.to_fire = set()

    def create_lattice(self):
        """
        Creates a lattice with cells initialized based on the specified probability.

        Returns:
        - numpy.ndarray: A 2D array representing the initial state of the lattice.
        """

        m = np.zeros((self.N, self.N))
        m[np.random.rand(self.N, self.N) < self.p] = 1
        return m

    def begin_fire(self):
        for column in range(self.N):
            if self.grid[0][column] == 1:
                self.grid[0][column] = 2

    def spread_fire(self):
        """
        Propagates the fire to neighboring cells based on predefined rules.
        """
        self.to_fire.clear()  # Clear the set before populating it again
        for column in range(self.N):
            for row in range(self.N):
                if self.grid[row][column] == 2:
                    if (column < self.N - 1) and self.grid[row][column + 1] == 1:
                        self.grid[row][column + 1] = 2
                    if (row < self.N - 1) and self.grid[row + 1][column] == 1:
                        self.grid[row + 1][column] = 2
                    if (row > 0) and self.grid[row - 1][column] == 1:
                        self.to_fire.add((row - 1, column))
                    if (column > 0) and self.grid[row][column - 1] == 1:
                        self.to_fire.add((row, column - 1))

    def spread_fire_next_time(self):
        for element in self.to_fire:
            self.grid[element[0]][element[1]] = 2

    def simulate_fire_spread(self, steps):
        """
        Simulates the spread of fire over a specified number of time steps.

        Args:
        - steps (int): The number of time steps to simulate.
        """
        self.begin_fire()
        grid_configs = [np.copy(self.grid)] 
        for _ in range(steps):
            self.spread_fire()
            self.grid_this_time = np.copy(self.grid)
            self.grid[self.grid == 2] = 3
            self.spread_fire_next_time()
            grid_configs.append(np.copy(self.grid))
        return grid_configs


if __name__ == "__main__":
    # This block will be executed only if the script is run directly, not when imported as a module

    # Example usage:
    N = 10
    p = 0.3
    steps = 5

    simulation = FireSimulation(N, p)
    simulation.simulate_fire_spread(steps)
