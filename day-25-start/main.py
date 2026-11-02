# import csv
# with open("weather_data.csv") as csv_file:
#     csv=csv.reader(csv_file)
#     temp=[]
#     for row in csv:
#         if row[1] == "temp":
#             continue
#         else:
#             temp.append(int(row[1]))
#     print(temp)
import pandas
data=pandas.read_csv("weather_data.csv")

min_temp=data[data.temp==data.temp.min()].temp
c_to_f=(min_temp*(9/5))+32
print(c_to_f)


