import tkinter as tk
from tkinter import messagebox, font
from hobby import fuzzy_inference, hobbies, get_learning_paths
from evolutionary_algo import run_evolutionary_algorithm
from learning_path import hobby_tasks
from hobby_tracker import HobbyTracker

class HobbyRecommendationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interest Explorer!")
        self.master.geometry("800x600")  # Set the window size
        self.master.configure(bg="#A3D8FF")

        # Set default font size
        default_font = font.Font(family="Space Mono", size=12)
        master.option_add("*Font", default_font)

        title_font = font.Font(family="Times New Roman", size=20, weight="bold")
        self.title_label = tk.Label(master, text="Interest Explorer!", font=title_font, fg="#FF76CE", bg="#2C3E50")
        self.title_label.pack(pady=20)  # Add padding to center the title at the top

        # Frame for input fields
        input_frame = tk.Frame(master, bg="#A3D8FF")  # Match the main background
        input_frame.pack(pady=10)

        # Initialize the HobbyTracker
        self.hobby_tasks = hobby_tasks  # Load your tasks here
        self.tracker = HobbyTracker(self.hobby_tasks)  # Initialize HobbyTracker

        self.age_label = tk.Label(input_frame, text="Age:", fg="#EE4266", bg="#FDFFC2")
        self.age_label.grid(row=0, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(input_frame,bg="#ECF0F1", fg="#2C3E50")
        self.age_entry.grid(row=0, column=1, padx=5, pady=5)

        self.skill_label = tk.Label(input_frame, text="Skill Level (0-100):", fg="#EE4266", bg="#FDFFC2")
        self.skill_label.grid(row=1, column=0, padx=5, pady=5)
        self.skill_entry = tk.Entry(input_frame, bg="#ECF0F1", fg="#2C3E50")
        self.skill_entry.grid(row=1, column=1, padx=5, pady=5)

        self.interest_label = tk.Label(input_frame, text="Interest Level (0-100):", fg="#EE4266", bg="#FDFFC2")
        self.interest_label.grid(row=2, column=0, padx=5, pady=5)
        self.interest_entry = tk.Entry(input_frame)
        self.interest_entry.grid(row=2, column=1, padx=5, pady=5)

        self.creativity_label = tk.Label(input_frame, text="Creativity Level (0-100):", fg="#EE4266", bg="#FDFFC2")
        self.creativity_label.grid(row=3, column=0, padx=5, pady=5)
        self.creativity_entry = tk.Entry(input_frame)
        self.creativity_entry.grid(row=3, column=1, padx=5, pady=5)

        self.physical_activity_label = tk.Label(input_frame, text="Physical Activity Level (0-100):", fg="#EE4266", bg="#FDFFC2")
        self.physical_activity_label.grid(row=4, column=0, padx=5, pady=5)
        self.physical_activity_entry = tk.Entry(input_frame)
        self.physical_activity_entry.grid(row=4, column=1, padx=5, pady=5)

        # Time Allocation
        self.time_allocation_label = tk.Label(input_frame, text="Time Allocation (1-8 hours):", fg="#EE4266", bg="#FDFFC2")
        self.time_allocation_label.grid(row=5, column=0, padx=5, pady=5)
        self.time_allocation_entry = tk.Entry(input_frame)
        self.time_allocation_entry.grid(row=5, column=1, padx=5, pady=5)

        # Social Preference
        self.social_pref_label = tk.Label(input_frame, text="Social Preference (0: Solo, 1: Group):", fg="#EE4266", bg="#FDFFC2")
        self.social_pref_label.grid(row=6, column=0, padx=5, pady=5)
        self.social_pref_entry = tk.Entry(input_frame)
        self.social_pref_entry.grid(row=6, column=1, padx=5, pady=5)

        # Button to get recommendations
        self.recommend_button = tk.Button(master, text="Get Recommendations", command=self.get_recommendations,
                                          bg="#F4538A", fg="#5E1675")
        self.recommend_button.pack(pady=10)

        self.recommendation_label = tk.Label(master, text="", font=("Space Mono", 14), bg="#A3D8FF")
        self.recommendation_label.pack()

        # Add a label to display learning paths
        self.learning_path_label = tk.Label(master, text="", font=("Space Mono", 12),bg="#A3D8FF")
        self.learning_path_label.pack()

        # Placeholder for tasks and progress tracking
        self.tasks = []
        self.completed_tasks = 0

    def clear_recommendation_widgets(self):
        """Clear existing widgets before displaying new ones."""
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Radiobutton) or isinstance(widget, tk.Button):
                widget.pack_forget()

    def validate_input(self, value, min_value, max_value):
        """Helper function to validate numeric input."""
        try:
            val = int(value)
            if min_value <= val <= max_value:
                return val
            else:
                raise ValueError
        except ValueError:
            return None

    def get_recommendations(self):
        # Get input values with validation
        age = self.validate_input(self.age_entry.get(), 0, 100)
        skill = self.validate_input(self.skill_entry.get(), 0, 100)
        interest = self.validate_input(self.interest_entry.get(), 0, 100)
        creativity = self.validate_input(self.creativity_entry.get(), 0, 100)
        physical_activity = self.validate_input(self.physical_activity_entry.get(), 0, 100)
        social_pref = self.validate_input(self.social_pref_entry.get(), 0, 1)
        time_allocation = self.validate_input(self.time_allocation_entry.get(), 1, 8)

        if None in [age, skill, interest, creativity, physical_activity, social_pref, time_allocation]:
            messagebox.showerror("Input Error", "Please enter valid numeric values in the correct ranges.")
            return

        # Call the fuzzy inference function
        recommendations = fuzzy_inference(age, skill, interest, creativity, physical_activity, social_pref, time_allocation)

        if recommendations:
            self.clear_recommendation_widgets()  # Clear previous widgets
            self.selected_hobby = tk.StringVar(value=recommendations[0][0])  # Default to first recommendation
            self.recommendation_label.config(text="Top Recommendations:", fg="#FF76CE", bg="#2C3E50",font=("Times New Roman", 20) )

            # Create radio buttons for each recommendation
            for hobby, score in recommendations:
                hobby_radiobutton = tk.Radiobutton(
                    self.master,
                    text=hobby,
                    variable=self.selected_hobby,
                    value=hobby,
                    bg="#FDFFC2",  # Background color for the button
                    fg="#EE4266",  # Text color for the button
                    font=("Space Mono", 15),  # Set the font and size
                    padx=10,  # Horizontal padding
                    pady=5  # Vertical padding
                )
                hobby_radiobutton.pack(pady=5)

            select_button = tk.Button(self.master, text="Select Hobby", command=self.select_hobby,  bg="#F4538A", fg="#5E1675")
            select_button.pack()
        else:
            messagebox.showinfo("No Recommendations", "No hobbies could be recommended.")

    def select_hobby(self):
        selected_hobby = self.selected_hobby.get()
        learning_paths_info = get_learning_paths(selected_hobby)

        if learning_paths_info:
            learning_paths_display = "\n".join([f"{path}: {info}" for path, info in learning_paths_info.items()])
            # Create a new window for level selection
            level_window = tk.Toplevel(self.master)
            level_window.title("Let's get you a learning path!")
            level_window.geometry("400x300")  # Set custom window size
            level_window.configure(bg="#A3D8FF")

            title_font = font.Font(family="Times New Roman", size=20, weight="bold")
            title_label = tk.Label(level_window, text="Let's get you\n a learning path!", font=title_font, fg="#FF76CE",
                                   bg="#2C3E50")
            title_label.pack(pady=20)

            # Set font style
            font_style = ("Space Mono", 14)  # Font with larger size

            # Label for skill level selection
            level_label = tk.Label(
                level_window,
                text="Select your skill level:",
                font=font_style,
                bg="#FDFFC2",  # Background color (matching the window or desired color)
                fg="#FF76CE"  # Foreground color (text color)
            )
            level_label.pack(pady=10)

            # Dropdown menu for skill level selection
            self.level_var = tk.StringVar(level_window)
            self.level_var.set("Choose one!")  # Default value
            level_options = ["Beginner", "Intermediate", "Advanced"]
            level_menu = tk.OptionMenu(level_window, self.level_var, *level_options)
            level_menu.config(
                font=("Space Mono", 14),  # Increase font size
                bg="#94FFD8",  # Background color
                fg="#EE4266"
            )
            level_menu.pack(pady=(10, 5))  # Add vertical space (10 above, 5 below)

            confirm_button = tk.Button(
                level_window,
                text="Confirm Level",
                command=lambda: self.confirm_level(level_window),
                font=("Space Mono", 14),  # Increase font size
                bg="#F4538A", fg="#5E1675"
            )
            confirm_button.pack(pady=(5, 10))
        else:
            self.learning_path_label.config(text=f"No learning paths available for {selected_hobby}.")

    def confirm_level(self, level_window):
        selected_level = self.level_var.get()
        selected_hobby = self.selected_hobby.get()

        # Get user profile data
        user_profile = {
            'age': int(self.age_entry.get()),
            'skill_level': int(self.skill_entry.get()),
            'interest_level': int(self.interest_entry.get()),
            'creativity_level': int(self.creativity_entry.get()),
            'physical_activity': int(self.physical_activity_entry.get()),
            'social_pref': int(self.social_pref_entry.get()),
            'time_allocation': int(self.time_allocation_entry.get()),
        }

        # Fetch learning paths information for the selected hobby
        learning_paths_info = get_learning_paths(selected_hobby)

        # Clear any previous content in the level_window
        for widget in level_window.winfo_children():
            widget.destroy()

        level_window.geometry("800x900")  # Set width and height

        title_label = tk.Label(
            level_window,
            text="Congratulations,\n You have been assigned a hobby!",
            font=("Times New Roman", 22, "bold"),
            fg="#FF76CE", bg="#2C3E50")
        title_label.pack(pady=20)

        if learning_paths_info:
            # Display the learning paths information
            duration = learning_paths_info[selected_level]['duration']
            goals = learning_paths_info[selected_level]['goals']
            milestones = learning_paths_info[selected_level]['milestones']

            # Prepare the message with the hobby details
            hobby_label = tk.Label(level_window, text=f"Hobby: {selected_hobby}", font=("Space Mono", 14), bg="#FDFFC2",
                                   fg="#347928")
            hobby_label.pack(pady=5)

            level_label = tk.Label(level_window, text=f"Level: {selected_level}", font=("Space Mono", 14), bg="#FDFFC2",
                                   fg="#347928")
            level_label.pack(pady=5)

            duration_label = tk.Label(level_window, text=f"Duration: {duration}", font=("Space Mono", 14),bg="#FDFFC2",
                                   fg="#347928")
            duration_label.pack(pady=5)

            goals_label = tk.Label(level_window, text=f"Goals: {', '.join(goals)}", font=("Space Mono", 14),
                                   bg="#FDFFC2",fg="#347928")
            goals_label.pack(pady=5)

            milestones_label = tk.Label(level_window, text=f"Milestones: {', '.join(milestones)}",
                                        font=("Space Mono", 14), bg="#FDFFC2",fg="#347928")
            milestones_label.pack(pady=5)

            # Run the evolutionary algorithm to get a personalized learning path
            best_learning_path = run_evolutionary_algorithm(user_profile, selected_hobby, selected_level)

            # Check if best_learning_path is valid
            if best_learning_path and isinstance(best_learning_path, list):
                # Use the HobbyTracker's display_tasks method to show tasks
                self.tracker.display_tasks(selected_hobby, selected_level,
                                           level_window)  # Assuming this method adds the tasks directly to the window

            else:
                no_paths_label = tk.Label(
                    level_window,
                    text=f"No learning paths available for {selected_hobby}.",
                    font=("Space Mono", 12),  # Set font to Space Mono
                    bg="#A3D8FF"
                )
                no_paths_label.pack(pady=20)

        else:
            no_paths_label = tk.Label(
            level_window,
            text=f"No learning paths available for {selected_hobby}.",
            font=("Space Mono", 12),  # Set font to Space Mono
            bg="#A3D8FF"
            )
            no_paths_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = HobbyRecommendationApp(root)
    root.mainloop()
