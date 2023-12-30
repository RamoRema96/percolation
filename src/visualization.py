
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import LinearSegmentedColormap

def visualize_fire_sequence(matrix_list):
    """
    Visualize a sequence of matrices as an animation using Tkinter and Matplotlib.

    Parameters:
    - matrix_list (list of 2D arrays): A list containing matrices to be visualized as frames in the animation.

    Usage:
    - Call this function with a list of matrices to display an animated visualization.
    - The visualization will be displayed in a Tkinter window with a Matplotlib plot.
    - Each matrix in the sequence is displayed as a frame in the animation.
    
    Notes:
    - The animation loops through the frames indefinitely.
    - The default frame duration is set to 1 second (1000 milliseconds).

    Example:
    ```python
    # Example usage:
    matrices = [matrix1, matrix2, matrix3, ...]
    visualize_fire_sequence(matrices)
    ```

    """

    root = tk.Tk()
    root.title("Matrix Visualization")

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    colors = [(1, 1, 1), (0, 1, 0), (1, 0, 0), (0, 0, 0)]  # White, Green, Red, Black
    cmap_name = 'custom'
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=4)

    def update_visualization(frame):
        ax.clear()
        matrix1 = matrix_list[frame]
        ax.imshow(matrix1, cmap=custom_cmap, interpolation='nearest', vmin=0, vmax=3)
        ax.set_title(f"Frame {frame}")
        canvas.draw()

    def animate(frame):
        update_visualization(frame)
        frame = (frame + 1) % len(matrix_list)
        root.after(1000, animate, frame)

    animate(0)
    root.mainloop()


