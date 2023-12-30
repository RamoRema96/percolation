import numpy as np
from percolation import FireSimulation
from visualization import visualize_fire_sequence

# Parameter

N = 50 # NxN is the dimension of the matrix
p = 0.6 # The density of the trees
T = 20 # Time step montecarlo

simulation = FireSimulation(N=N, p=p)
configs = simulation.simulate_fire_spread(T)
visualize_fire_sequence(configs, save_path=f"../image/animation_{N}_{p}_{simulation.t}.gif")

print(f"Tempo di fine simulazione: {simulation.t}")
