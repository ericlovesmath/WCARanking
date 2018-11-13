import itertools
fin = open ('WCAexpSin.csv', 'r')
fout = open ('WCAexpSing.txt', 'w')

Data = []
for x in range(370068):
  CurrentData = str(fin.readline().replace("[","").replace("]","").replace("'",""))
  fout.write(str(CurrentData))
  Data.append(CurrentData)
fout.close()


#('2014CZAP01','222','49','1','1','1'),