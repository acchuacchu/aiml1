import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

s1=pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/iris.csv")
print(pd.DataFrame(s1))

plt.scatter(s1["SepalLengthCm"],s1["PetalLengthCm"])
plt.title("scatter plot")
plt.xlabel("SepalLengthCm")
plt.ylabel("PetallengthCm")
plt.show()


plt.plot(s1["SepalLengthCm"])
plt.plot(s1["PetalLengthCm"])
plt.title("linechart")
plt.xlabel("sepalLengthCm")
plt.ylabel("PetalLengthCm")
plt.show()

plt.bar(s1["SepalLengthCm"],s1["PetalLengthCm"])
plt.title("bar graph")
plt.xlabel("sepalLengthCm")
plt.ylabel("PetalLengthCm")
plt.show()

plt.hist(s1["SepalLengthCm"]) 
print(s1["SepalLengthCm"].max())
plt.title("histogram")
plt.show()

print(s1['PetalWidthCm'].hist())
sns.set(style='darkgrid')
a=sns.countplot(x='PetalWidthCm',data=s1)


