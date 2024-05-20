def calculate_average():
  """
  This function calculates the average of three grades.
  """
  grade1 = float(input("Enter Grade 1: "))
  grade2 = float(input("Enter Grade 2: "))
  grade3 = float(input("Enter Grade 3: "))

  average = (grade1 + grade2 + grade3) / 3

  print("The average grade is:", average)

calculate_average()
