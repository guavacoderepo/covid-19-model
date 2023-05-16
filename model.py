import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

df = df.drop(['s/n'], axis=1)
df = df.drop(['doc_index'], axis=1)


# print(df.head)
sns.set(style='whitegrid')
# print(df.head)
# sns.barplot(df)
# sns.scatterplot(df)
sns.heatmap(df)
# sns.histplot(df)


# plt.hist(df)
plt.show()
