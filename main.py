import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('all_youtube_analytics.csv')
df.info()

print(df.describe())


df["day"].plot(kind='hist')
plt.show()


