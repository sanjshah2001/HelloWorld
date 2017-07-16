import csv

class FormatData:
   def __init__(self, Name="", Age=0, Married=False):
      self.Name = Name
      self.Age = Age
      self.Married = Married

   def __str__(self):
      OutString = "'{0}', {1}, {2}".format(
         self.Name,
         self.Age,
         self.Married)
      return OutString
