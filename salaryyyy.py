import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"11prog_3Salary_Data.csv")
plt.plot(df['YearsExperience'],df['Salary'])
plt.ylabel('YearsExperience')
plt.xlabel('Index')
plt.legend()
plt.show()
sns.lineplot(y=df['YearsExperience'],x=df['Salary'])
plt.show()
