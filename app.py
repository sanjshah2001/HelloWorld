import csv
from FormattedData import FormatData

NewData = [FormatData("Ashish", 65, True),
           FormatData("Sally", 47, False),
           FormatData("Doug", 52, True)]

for Entry in NewData:
   print(Entry)

def SaveData(Filename = "", DataList = []):
   with open(Filename,
             "w") as csvfile:
      DataWriter = csv.writer(
         csvfile,
         delimiter='\n',
         quotechar=" ",
         quoting=csv.QUOTE_NONNUMERIC)
      DataWriter.writerow(DataList)
      csvfile.close()
      print("Data saved!")

SaveData("TestFile.csv", NewData)
