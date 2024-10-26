# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation
#
# # Set up the initial figure
# fig, ax = plt.subplots(figsize=(10, 10))
#
# # Provide initial dummy data for the scatter plot
# x_init = 100 * np.random.rand(10)
# y_init = 100 * np.random.rand(10)
# colors_init = np.random.rand(10)
# sizes_init = 1000 * np.random.rand(10)
# scatter = ax.scatter(x_init, y_init, c=colors_init, s=sizes_init, alpha=0.3, cmap='viridis')
#
#
# # Function to update the data of the scatter plot
# def update(frame):
#     x = 100 * np.random.rand(100)
#     y = 100 * np.random.rand(100)
#     colors = np.random.rand(100)
#     sizes = 1000 * np.random.rand(100)
#     scatter.set_offsets(np.c_[x, y])
#     scatter.set_sizes(sizes)
#     scatter.set_array(colors)
#
#
# # Create an animation that updates the plot every 1000 milliseconds (1 second)
# ani = FuncAnimation(fig, update, interval=1000, save_count=1)
#
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation
#
# # Set up the initial figure
# fig, ax = plt.subplots(figsize=(10, 10))
#
# # List of different marker shapes
# marker_shapes = ['o', 's', '^', '>', '<', 'v', '*', '+', 'x']
# current_marker = 0
#
#
# # Function to update the data of the scatter plot
# def update(frame):
#     global current_marker
#     ax.clear()  # Clear existing plot elements
#     # ax.set_xticks([])  # Remove x-axis ticks
#     # ax.set_yticks([])  # Remove y-axis ticks
#
#     x = np.random.rand(100)
#     y = np.random.rand(100)
#     colors = np.random.rand(100)
#     sizes = 1000 * np.random.rand(100)
#     current_marker = (current_marker + 1) % len(marker_shapes)
#
#     ax.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='prism', marker=marker_shapes[current_marker])
#     ax.figure.canvas.draw()  # Redraw the canvas
#
#
# # Create an animation that updates the plot every 1000 milliseconds (1 second)
# ani = FuncAnimation(fig, update, interval=300, save_count=1)
#
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation
#
#
# # Mandelbrot function
# def mandelbrot(c, max_iter):
#     z = 0
#     for n in range(max_iter):
#         if abs(z) > 2:
#             return n
#         z = z*z + c
#     return max_iter
#
#
# # Function to generate Mandelbrot set
# def generate_mandelbrot(iterations, xlim, ylim, resolution=0.005):
#     real = np.arange(xlim[0], xlim[1], resolution)
#     imag = np.arange(ylim[0], ylim[1], resolution)
#     real, imag = np.meshgrid(real, imag)
#     complex_numbers = real + 1j*imag
#
#     mandelbrot_set = np.zeros(complex_numbers.shape)
#     for x in range(complex_numbers.shape[0]):
#         for y in range(complex_numbers.shape[1]):
#             color = mandelbrot(complex_numbers[x, y], iterations)
#             mandelbrot_set[x, y] = color
#
#     return real, imag, mandelbrot_set
#
#
# # Set up the initial figure
# fig, ax = plt.subplots(figsize=(8, 6))
#
#
# # Update function
# def update(frame):
#     ax.clear()  # Clear existing plot elements
#     max_iter = np.random.randint(50, 200)  # Randomize max iterations
#     xlim = (-2, 1)
#     ylim = (-1.5, 1.5)
#     real, imag, mandelbrot_set = generate_mandelbrot(max_iter, xlim, ylim)
#
#     ax.imshow(mandelbrot_set.T, extent=[xlim[0], xlim[1], ylim[0], ylim[1]], cmap='prism')
#     # ax.set_xticks([])  # Remove x-axis ticks
#     # ax.set_yticks([])  # Remove y-axis ticks
#
#
# # Create an animation that updates the plot every 2000 milliseconds (2 seconds)
# ani = FuncAnimation(fig, update, interval=1000, save_count=1)
#
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation
#
#
# # Mandelbrot function
# def mandelbrot(c, max_iter):
#     z = 0
#     for n in range(max_iter):
#         if abs(z) > 2:
#             return n
#         z = z*z + c
#     return max_iter
#
#
# # Function to generate Mandelbrot set
# def generate_mandelbrot(iterations, xlim, ylim, resolution=0.005):
#     real = np.arange(xlim[0], xlim[1], resolution)
#     imag = np.arange(ylim[0], ylim[1], resolution)
#     real, imag = np.meshgrid(real, imag)
#     complex_numbers = real + 1j*imag
#
#     mandelbrot_set = np.zeros(complex_numbers.shape)
#     for x in range(complex_numbers.shape[0]):
#         for y in range(complex_numbers.shape[1]):
#             color = mandelbrot(complex_numbers[x, y], iterations)
#             mandelbrot_set[x, y] = color
#
#     return real, imag, mandelbrot_set
#
#
# # Set up the initial figure
# fig, ax = plt.subplots(figsize=(8, 6))
# xlim = (-2, 1)
# ylim = (-1.5, 1.5)
#
#
# # Update function for animation
# def update(frame):
#     ax.clear()  # Clear existing plot elements
#     real, imag, mandelbrot_set = generate_mandelbrot(frame, xlim, ylim)
#
#     ax.imshow(mandelbrot_set.T, extent=[xlim[0], xlim[1], ylim[0], ylim[1]], cmap='prism')
#     ax.set_xticks([])  # Remove x-axis ticks
#     ax.set_yticks([])  # Remove y-axis ticks
#
#
# # Create an animation
# ani = FuncAnimation(fig, update, frames=range(1, 20), interval=400)
#
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# def draw_sierpinski(ax, vertices, level):
#     if level == 0:
#         # Draw the triangle
#         triangle = plt.Polygon(vertices, edgecolor='black', facecolor='none')
#         ax.add_patch(triangle)
#     else:
#         # Calculate the midpoints of each side
#         v1 = (1.2 * vertices[0] + vertices[1]) / 2
#         v2 = (vertices[1] + 1.2 * vertices[2]) / 2
#         v3 = (1.2 * vertices[0] + vertices[2]) / 2
#
#         # Recursively draw smaller triangles
#         draw_sierpinski(ax, [vertices[0], v1, v3], level-1)
#         draw_sierpinski(ax, [v1, vertices[1], v2], level-1)
#         draw_sierpinski(ax, [v3, v2, vertices[2]], level-1)
#
# # Initialize plot
# fig, ax = plt.subplots()
# ax.set_aspect('equal', 'box')
# # ax.axis('off')
#
# # Triangle vertices and recursion level
# vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
# level = 4  # Recursion level
#
# # Draw the Sierpinski Triangle
# draw_sierpinski(ax, vertices, level)
#
# plt.show()