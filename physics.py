import math

def calculateForce(mass, accelaration):
    """to calculate force: f = m*a"""
    return mass * accelaration


def calculate_work(force, distance, angle=0):
    """Calculate work done"""
    return force * distance * math.cos(math.radians(angle))

def calculate_velocity(initial_velocity, time, acceleration):
    """Calculate final velocity"""
    return initial_velocity + acceleration * time

def calcultateDisplacement(initialVelocity, time, acceleration):
    """Calculate displacement: s= ut + 0.5 * a t^2"""
    return initialVelocity * time + 0.5 * acceleration * time ** 2

def calculateKineticEnergy(mass, velocity):
    """Calculate   kinetic: KE 0.5 * m * v^2"""
    return 0.5 * mass * velocity **2

def main():
    print("Choose from the physics menu")
    print("1. Calculate Force")
    print("2. Calculate Work")
    print("3. Calculate Velocity")
    print("4. Calculate Displacement")
    print("5. Calculate kinetic energy")

    choice = int(input("Enter the operation you want to perform: "))
    if choice == 1:
        mass = float(input("Enter mass : "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        print("Force:", calculateForce(mass,acceleration), "N")
    elif choice == 2:
        force = float(input("Enter force (N): "))
        distance = float (input("Enter distance (m): "))
        angle = float(input("Enter angle (degree): "))
        print("work Done:", calculate_work(force, distance, angle), "J")

    elif choice == 3:
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity (m/s): "))
        print("kinetic Energy:", calculate_velocity(mass, velocity), "J")

    elif choice == 4:
        initialVelocity = float(input("Enter initial velocity (m/s): "))
        time = float(input("Enter time (s): "))
        acceleration = float(input("Enter acceleration (m/s^2: "))
        print("Final Velocity:", calculate_velocity(initialVelocity, acceleration, time))

    elif choice ==5:
        mass = float(input("Enter mas (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        print("Kinetic Energy:", calculateKineticEnergy(mass,velocity))


    else:
        print("Invalid choice")

if __name__ == "__main__":
 main()





