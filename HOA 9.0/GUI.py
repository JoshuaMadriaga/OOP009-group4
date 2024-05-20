from tkinter import Tk, Label, Entry, Button

def calculate_average():
  """
  This function calculates the average of three grades and displays it on the GUI.
  """
  grade1 = float(grade1_entry.get())
  grade2 = float(grade2_entry.get())
  grade3 = float(grade3_entry.get())

  average = (grade1 + grade2 + grade3) / 3

  average_label.config(text="Average: " + str(average))

window = Tk()
window.title("Grade Calculator")

grade1_label = Label(window, text="Grade 1:")
grade1_label.pack()

grade1_entry = Entry(window)
grade1_entry.pack()

grade2_label = Label(window, text="Grade 2:")
grade2_label.pack()

grade2_entry = Entry(window)
grade2_entry.pack()

grade3_label = Label(window, text="Grade 3:")
grade3_label.pack()

grade3_entry = Entry(window)
grade3_entry.pack()

calculate_button = Button(window, text="Calculate Average", command=calculate_average)
calculate_button.pack()

average_label = Label(window, text="Average: ")
average_label.pack()

window.mainloop()
