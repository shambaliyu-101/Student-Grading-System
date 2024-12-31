import tkinter as tk
from tkinter import messagebox

class GradingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Grading System")

        # UI Setup
        self.create_ui()

    def create_ui(self):
        tk.Label(self.master, text="Student Grading System", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.master, text="Enter Grades (comma-separated):").grid(row=1, column=0, sticky="e")
        self.grades_entry = tk.Entry(self.master)
        self.grades_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.master, text="Calculate Average", command=self.calculate_average).grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_average(self):
        grades_text = self.grades_entry.get()
        try:
            grades = [float(grade.strip()) for grade in grades_text.split(",") if grade.strip()]
            if not grades:
                raise ValueError("No valid grades entered.")

            average = sum(grades) / len(grades)
            letter_grade = self.get_letter_grade(average)

            self.result_label.config(text=f"Average: {average:.2f} | Letter Grade: {letter_grade}")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def get_letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

if __name__ == "__main__":
    root = tk.Tk()
    app = GradingSystem(root)
    root.mainloop()
