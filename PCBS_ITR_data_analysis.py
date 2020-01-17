import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from glob import glob

N_BLOCKS = 4

# Calculating the reaction time means
rt_data = {block: [] for block in range(1, N_BLOCKS+1)} # Range values chosen because block numbers start at 1, range iterator at 0
rt_means = {}

files = glob('reaction_times_*.csv')
for file in files:
    df = pd.read_csv(file)

    # Extracting the relevant values (RTs) for each block of each file
    for block in range(1, N_BLOCKS+1):
        df_block = df.loc[df['Block'] == block]
        rt_data[block].append(df_block['RT\ms'].mean())

for block, values in rt_data.items():
    rt_means[block] = np.mean(values)


# Plotting the figure
conditions = ['Ipsolateral', 'Contralateral']
mean_reaction_times_right = [rt_means[3], rt_means[1]]
mean_reaction_times_left = [rt_means[2], rt_means[4]]

# Plotting factorial plot for the right hand data
plt.plot(conditions, mean_reaction_times_right)
plt.scatter(conditions, mean_reaction_times_right)

# Plotting factorial plot for the left hand data
plt.plot(conditions, mean_reaction_times_left)
plt.scatter(conditions, mean_reaction_times_left)

plt.ylabel('Reaction Times [ms]')
plt.xlabel('Conditions')

plt.show()
