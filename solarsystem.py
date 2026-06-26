import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------
# Initial conditions
# -------------------------

# Position of planet
x = 5.0
y = 0.0

# Velocity of planet
vx = 0.0
vy = 1.4

# Gravitational parameter (G*M)
GM = 10.0

# Time step
dt = 0.01

# -------------------------
# Plot setup
# -------------------------

fig, ax = plt.subplots()

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

ax.grid(True)

# Sun
sun, = ax.plot(0, 0, 'yo', markersize=15)

# Planet
planet, = ax.plot([], [], 'bo', markersize=8)

# Orbit trail
trail_x = []
trail_y = []

orbit_line, = ax.plot([], [], '-', lw=1)

# -------------------------
# Animation update
# -------------------------

def update(frame):
    global x, y, vx, vy

    # Multiple physics steps per frame
    for _ in range(5):

        dx = -x
        dy = -y

        r = np.sqrt(dx**2 + dy**2)

        # Gravity
        ax_g = GM * dx / r**3
        ay_g = GM * dy / r**3

        # Update velocity
        vx += ax_g * dt
        vy += ay_g * dt

        # Update position
        x += vx * dt
        y += vy * dt

    trail_x.append(x)
    trail_y.append(y)

    planet.set_data([x], [y])
    orbit_line.set_data(trail_x, trail_y)

    return planet, orbit_line

ani = FuncAnimation(
    fig,
    update,
    frames=5000,
    interval=10,
    blit=True
)

plt.show()