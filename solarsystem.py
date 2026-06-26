import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Physical Planet Data (Mercury to Neptune)
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
r_real = np.array([5.79e10, 1.082e11, 1.496e11, 2.279e11, 7.786e11, 1.43e12, 2.87e12, 4.49e12])
omega = np.array([8.24e-7, 3.24e-7, 1.99e-7, 1.05e-7, 1.67e-8, 9.29e-9, 2.37e-9, 1.21e-9])
colors = ['gray', 'orange', 'blue', 'red', 'brown', 'gold', 'lightblue', 'darkblue']

# 2. Dynamic Scaling: Use log-scaling so all planets fit beautifully on screen
# We map the real distances into a clean visual range (e.g., 1 to 10 units away from the Sun)
r_visual = np.log10(r_real)
r_visual = 1 + 9 * (r_visual - r_visual.min()) / (r_visual.max() - r_visual.min())

# 3. Setup Plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Set clean limits around our visual radius range
max_v = max(r_visual) * 1.1
ax.set_xlim(-max_v, max_v)
ax.set_ylim(-max_v, max_v)
ax.set_aspect('equal')
ax.axis('off') # Hide axes for a clean space look

# Draw the Sun
ax.plot(0, 0, 'wo', markersize=12, label="Sun")

# Draw orbits and initialize planet markers using lists
orbits = []
planets = []
for i in range(8):
    # Draw orbit path
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(r_visual[i]*np.cos(theta), r_visual[i]*np.sin(theta), color=colors[i], alpha=0.2, linestyle='--')
    
    # Create planet marker
    line, = ax.plot([], [], 'o', color=colors[i], markersize=6, label=planet_names[i])
    planets.append(line)

# Add a clean dark-themed legend
ax.legend(loc="upper left", facecolor='black', edgecolor='gray', labelcolor='white')

# 4. Vectorized Animation Update
def update(frame):
    # 172.8 seconds per frame * 500 frames/sec = 86,400 seconds (1 day) per real-world second
    t = frame * 172.8 * 100
    
    # Calculate all positions at once using NumPy vectorization
    x_positions = r_visual * np.cos(omega * t)
    y_positions = r_visual * np.sin(omega * t)
    
    # Update each planet marker using a loop
    for i in range(8):
        planets[i].set_data([x_positions[i]], [y_positions[i]])
        
    return planets

# interval=2 ms creates 500 frames per second
ani = FuncAnimation(fig, update, frames=5000, interval=2, blit=True)

plt.show()

