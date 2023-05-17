import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

# df = df.drop(['index'], axis=1)
# df = df.drop(['doc_index'], axis=1)


# print(df.head)
sns.set(style='whitegrid')
# print(df.head)
# sns.barplot(df)
# sns.scatterplot(df)
# sns.countplot(data=df, y="china", x="index")
# sns.countplot(x=df["scale-free"], )
# sns.countplot(x=df["china"])

# plt.scatter(x=df["index"], y=df["machine learning"])
# plt.scatter(x=df["index"], y=df["covid"])
# plt.scatter(x=df["index"], y=df["scale-free"])
# plt.scatter(x = df["index"], y=df["china"])

# plt.legend(["machile learning", "covid 19", "scale-free", "china"])


# plt.scatter(x=df["index"], y=df["machine learning"], )


# plt.scatter(x=df["index"], y=df["covid"])
# plt.scatter(x=df["index"], y=df["scale-free"])
plt.scatter(x=df["index"], y=df["china"])

plt.grid(color='green', linewidth=0.5)

plt.xlabel("Document index")
plt.ylabel("China")

plt.show()


# plt.hist(df)
plt.show()
