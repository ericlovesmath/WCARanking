import itertools  
fin = open ('Singles.txt', 'r')

Data = []
for x in range(370067):
  CurrentData = fin.readline().strip().split(", ")
  fout = open ("SingleTimes/" + CurrentData[1] + "Single.csv", 'a')
  fout.write(CurrentData[2] + ", ")
  Data.append(CurrentData)
fout.close()


#('2014CZAP01','222','49','1','1','1'), 370068