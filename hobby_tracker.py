from learning_path import hobby_tasks
import tkinter as tk
from tkinter import messagebox,filedialog
import json

class HobbyTracker:
    import json
    from tkinter import messagebox, filedialog

    def save_progress(self, hobby, level):
        """Save the current progress of tasks to a text file."""
        progress = self.calculate_progress(hobby, level)
        if progress is not None:
            # Get the path for the .txt file
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Save Progress As"
            )

            if file_path:  # If the user didn't cancel the dialog
                try:
                    with open(file_path, 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding
                        tasks = self.hobby_tasks[hobby][level]
                        file.write(f"Progress for {hobby} - {level}:\n\n")
                        for task in tasks:
                            status = "✔️" if task.get('completed', False) else "❌"
                            file.write(f"• {status} {task['task']}\n")

                    # Notify user of successful save
                    messagebox.showinfo("Progress Saved", f"Progress for {hobby} - {level} saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not save progress: {str(e)}")
        else:
            messagebox.showerror("Error", "Could not save progress due to an error.")

    def __init__(self, hobby_tasks):
        self.hobby_tasks = hobby_tasks
        self.tasks_vars =0  # Store references to task variables for tracking completion

    def display_tasks(self, hobby, level, parent_window):
        """Display all tasks for a specified hobby and level, and allow the user to mark them as completed."""
        try:
            tasks = self.hobby_tasks[hobby][level]

            # Create a new frame for displaying tasks
            task_frame = tk.Frame(parent_window, bg="#A3D8FF")  # Set background color for the task frame
            task_frame.pack(pady=10)

            # Clear previous task variables
            self.tasks_vars = []

            header_label = tk.Label(
                task_frame,
                text=f"Tasks for {hobby}:",
                font=("Times New Roman", 20, "bold"),
                fg="#FF76CE", bg="#2C3E50"
            )
            header_label.pack(pady=10)

            for i, task in enumerate(tasks):
                var = tk.BooleanVar(value=task.get('completed', False))  # Set initial value from task completion status
                self.tasks_vars.append(var)  # Store the reference to the variable

                # Create the checkbox for the task
                task_checkbox = tk.Checkbutton(
                    task_frame,
                    text=task['task'],
                    variable=var,
                    command=lambda idx=i: self.mark_task_completed(hobby, level, idx),
                    bg="#FEFFA7",  # Background color for the checkbox
                    fg="#1679AB",  # Foreground color for checkbox text
                    font=("Space Mono", 22)  # Font size for the checkbox text (missing closing parenthesis fixed)
                )

                task_checkbox.pack(anchor='w', pady=20)  # Add vertical space between tasks

            # Add a button to save progress
            save_button = tk.Button(
                parent_window,
                text="Save Progress",
                command=lambda: self.save_progress(hobby, level),
                font=("Space Mono", 17),  # Font size for the button text
                bg="#F4538A", fg="#5E1675"
            )
            save_button.pack(pady=5)

        except KeyError:
            messagebox.showerror("Error", "Invalid hobby or level.")

    def mark_task_completed(self, hobby, level, task_index):
        """Mark a specified task as completed."""
        try:
            task = self.hobby_tasks[hobby][level][task_index]
            task['completed'] = self.tasks_vars[task_index].get()  # Update task completion status based on checkbox
            status = "completed" if task['completed'] else "not completed"
            print(f"Task '{task['task']}' marked as {status}.")
        except (KeyError, IndexError):
            messagebox.showerror("Error", "Invalid hobby, level, or task index.")

    def calculate_progress(self, hobby, level):
        """Calculate the completion percentage of tasks for a specified hobby and level."""
        try:
            tasks = self.hobby_tasks[hobby][level]
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task['completed'])
            progress_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            return progress_percentage
        except KeyError:
            print("Invalid hobby or level.")
            return None