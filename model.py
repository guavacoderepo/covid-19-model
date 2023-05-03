import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

df = df.drop(['s/n'], axis=1)

# print(df.head)

# print(df.head)
sns.catplot(df, x="doc_index", kind="bar")
# plt.hist(df)
plt.show()
