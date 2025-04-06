import matplotlib.pyplot as plt
import numpy as np

area =np.array( [11.7,10.4,1.9,9.4,3.3,6.9,7.9])
continents=np.array(["africa","asia","europe","north america","oceania","south america","soviet union"])
colors=["blue","orange","yellow","black","red","brown","pink"]
plt.bar(area,continents,label="areaof continents",color=colors)
plt.xlabel("continents")
plt.ylabel("area")
plt.title("areaof various continents")
plt.legend()
plt.grid(True,alpha=0.25)
plt.show()