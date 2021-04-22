import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D

print("Choose a function")
print("1. Three-hump camel function.")
print("2. Booth function.")
print("3. Beale function.")
print("4. Exit")

chooseFunction = int(input("Choose: "))

while chooseFunction != 4:

    if chooseFunction == 1:
        print("=== Three-hump camel function ===")
        alh = SwarmPackagePy.pso(50, tf.three_hump_camel_function, -5, 5, 20, 100, w=0.5, c1=1, c2=1)
        print(alh.get_Gbest())
        animation3D(alh.get_agents(), tf.three_hump_camel_function, -5, 5)

    elif chooseFunction == 2:
        print("=== Booth function ===")
        alh = SwarmPackagePy.pso(50, tf.booth_function, -10, 10, 20, 100, w=0.5, c1=1, c2=1)
        print(alh.get_Gbest())
        animation3D(alh.get_agents(), tf.booth_function, -10, 10)

    elif chooseFunction == 3:
        print("=== Beale function ===")
        alh = SwarmPackagePy.pso(50, tf.beale_function, -4.5, 4.5, 20, 100, w=0.5, c1=1, c2=1)
        print(alh.get_Gbest())
        animation3D(alh.get_agents(), tf.beale_function, -4.5, 4.5)

    else:
        print("???")

    chooseFunction = int(input("Choose: "))
