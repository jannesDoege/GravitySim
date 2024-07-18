# TODO: collisions (normal forces)


dt = 0.1
grav_constant = 6.674e-11
grav_constant = 1


class Object:
    def __init__(self, mass, x, v) -> None:
        self.mass = mass
        self.x = x
        self.v = v


def calc_grav_force(o1, o2):
    f = grav_constant * o1.mass * o2.mass / (o1.x - o2.x)**2
    # add direction
    f *= (o2.x - o1.x) / abs(o2.x-o1.x)
    return f


def grav_forces(objects):
    forces = []
    for o1 in objects:
        for o2 in objects:
            if o1 != o2:
                forces.append(calc_grav_force(o1, o2))

    return  forces


def harm_osci_forces(objects, k=0.001):
    # force due to potential of form k*x**2
    forces = []
    for o in objects:
        f = -o.x * k
        forces.append(f)
    
    return forces


def calc_forces(objects, oscillation=False):
    # Gravity
    forces = grav_forces(objects)
    
    if oscillation:
        forces = harm_osci_forces(objects)

    return forces


# assuming 1D case
def simulate(objects, steps=1):
    for _ in range(steps):
        # update forces
        forces = calc_forces(objects)

        # update objects
        for o, f in zip(objects, forces):
            o.v += f/o.mass*dt
            o.x += o.v*dt

    return objects


if __name__ == "__main__":
    # objects = [Object(1, 1, 0), Object(1, -1, 0)]
    objects = [Object(1, 0, -1)]

    for _ in range(100):
        objects = simulate(objects)
        positions = [round(o.x, 2) for o in objects]
        velocities = [round(o.v, 2) for o in objects]
        print(positions, velocities)



