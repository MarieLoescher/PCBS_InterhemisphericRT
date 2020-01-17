import matplotlib.pyplot as plt
import pandas as pd
from glob import glob

N_BLOCKS = 4

# Reading the data from all output files
files = glob('reaction_times_*.csv')
for file in files:
    df = pd.read_csv(file)

# Extracting the relevant values (RTs) for each block of each file
    rt_data = {}
    for block in range(1, N_BLOCKS+1): #Because blocks start at 1, but iteration at 0
        df_block = df.loc[df['Block'] == block]
        rt_data[block] = df_block['RT\ms']



# Calculating mean RTs




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
