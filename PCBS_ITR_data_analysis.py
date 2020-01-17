import matplotlib.pyplot as plt
import pandas as pd

# Calculating mean RTs
df = pd.read_csv('reaction_times_14-01-2020T13-53.csv')



conditions = ['Ipsolateral', 'Contralateral']
#mean_reaction_times_right = insert the 4 mean reaction times for the right hand here
#mean_reaction_times_left = insert the 2 mean reaction times for the left hand here
reaction_times_provisory_right = [250, 310]
reaction_times_provisory_left = [270, 350]

# Plotting factorial plot for the right hand data
plt.plot(conditions, reaction_times_provisory_right)
plt.scatter(conditions, reaction_times_provisory_right)

# Plotting factorial plot for the left hand data
plt.plot(conditions, reaction_times_provisory_left)
plt.scatter(conditions, reaction_times_provisory_left)

plt.ylabel('Reaction Times [ms]')
plt.xlabel('Conditions')

plt.show()
