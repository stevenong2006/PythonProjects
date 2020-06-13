import collections as collect
import pandas as pd

# Employee is namedtuple
Employee = collect.namedtuple('Person', 'Name Age Gender ID')
Team = [] # Team is a list

Team.append(Employee(Name='Bob', Age=30, Gender='male', ID=234))
Team.append(Employee(Name='Jane', Age=29, Gender='female', ID=134))
Team.append(Employee(Name='Tom', Age=35, Gender='male', ID=122))

print(Team)

df = pd.DataFrame(Team)

print(df)

print(df.iloc[2])





