import itertools 
from math import *
fin = open ('AverageTimes/AllAverages.csv', 'r')
fout = open ("RANKINGAVERAGES.csv", 'w')
Data = []
Events = ["222","333","333bf","333fm","333ft","333oh","444","555","666","777","clock","minx","pyram","skewb","sq1"]
for x in range(14):
  CurrentData = fin.readline().strip().split(", ")[1:]
  Data.append(CurrentData)
Percentiles = []
for x in range(14):
  Percentiles.append([Events[x],int(Data[x][int(len(Data[x])/100)]), int(Data[x][int(len(Data[x])/20)]), int(Data[x][int(len(Data[x])/10)]), int(Data[x][int(len(Data[x])/(10/3))]), int(Data[x][int(len(Data[x])/2)]), int(Data[x][int(len(Data[x])/1.25)])])
  fout.write(Events[x] + ": " + Data[x][int(len(Data[x])/100)] + ", " + Data[x][int(len(Data[x])/20)] + ", " + Data[x][int(len(Data[x])/10)] + ", " + Data[x][int(len(Data[x])/(10/3))] + ", " + Data[x][int(len(Data[x])/2)] + ", " + Data[x][int(len(Data[x])/1.25)])
  fout.write("\n")
  
print(Percentiles)

fout.close()


#('2014CZAP01','222','49','1','1','1'), 370068