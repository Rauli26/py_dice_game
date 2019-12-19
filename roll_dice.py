# Import numpy as np
import numpy as np
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Set the seeds
np.random.seed(123)
# Initialization
all_walks = []
# Simulate random walk 500 times
#print("Please enter number of times you want to simulate: ", end="")
#simulation_number = int(input())
simulation_number = int(input("Please enter number of times you want to simulate:"))
for i in range(simulation_number) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

visualize = True
while visualize == True:
    print("Please choose how you want to visualize:")
    print("Type 1 : For Line plot")
    print("Type 2 : For Histogram")
    #print("Please type number 1 or 2:", end="")
    #user_input = int(input())

    user_input =  int(input("Please type number 1 or 2:"))
    #print(user_input)
    # Plot random_walk
    if user_input == 1:
        plt.plot(np_aw_t)
    #plt.show()
    # Plot histogram of ends, display plot
    elif user_input == 2:
        plt.hist(ends)

# Show the plot
    plt.show()
    answer = input("Whould you like to visualize again:").lower()

    while answer == 'yes':
        visualize = True
        break
    else:
        visualize = False
        break


