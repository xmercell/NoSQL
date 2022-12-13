
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
rethink = [0.03488708000004408*1000, 0.008060239999940677*1000, 0.007283520000055432*1000, 0.040916100000049485*1000]
mongo = [0.0019293200000902288*1000, 0.0020061199998963274*1000, 0.0019584400000894676*1000, 0.006232370010204435*1000]
 
# Set position of bar on X axis
br1 = np.arange(len(rethink))
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, rethink, color ='r', width = barWidth,
        edgecolor ='grey', label ='RethinkDB')
plt.bar(br2, mongo, color ='g', width = barWidth,
        edgecolor ='grey', label ='MongoDB')
 
# Adding Xticks
plt.xticks([r + barWidth for r in range(len(rethink))],
        ['INSERT', 'REMOVE', 'UPDATE', 'LIST'])
plt.xlabel('Operations', fontweight ='bold', fontsize = 15)
plt.ylabel('Time in mili-seconds', fontweight ='bold', fontsize = 15)
 
plt.legend()
plt.show()