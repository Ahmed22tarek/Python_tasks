import random
import matplotlib.pyplot as plt
import numpy as np

days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
degrees = np.random.randint(0,51,size=7)

plt.plot(days,degrees,marker='X',linestyle='-',color='red')
plt.title('This Week Tempreature')
plt.xlabel('Days Per Week')
plt.ylabel('Degrees in Celsius')
plt.show()