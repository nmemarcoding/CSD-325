# Name: Nima Memarzadeh
# Date: 013/12/2024
# Assignment: Module 10.2

import tkinter as tk
import tkinter.messagebox as msg

class TodoApp(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Set the window title
        self.title("YourLastName-ToDo")  # Replace 'YourLastName' with your actual last name
        self.geometry("300x400")

        # Create menu
        self.menu = tk.Menu(self, bg="purple", fg="white")  # Complementary colors
        self.file_menu = tk.Menu(self.menu, tearoff=0, bg="yellow", fg="black")  # Complementary colors
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu)

        # Create canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Add default label with instructions
        todo_label = tk.Label(
            self.tasks_frame,
            text="--- Right Click Item to Delete ---",
            bg="purple",
            fg="yellow",
            pady=10,
        )
        todo_label.bind("<Button-2>" if self.is_mac() else "<Button-3>", self.remove_task)  # Right-click to delete
        self.tasks.append(todo_label)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Key and mouse bindings
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Color schemes
        self.colour_schemes = [{"bg": "purple", "fg": "yellow"}, {"bg": "yellow", "fg": "purple"}]

    def is_mac(self):
        """Check if the app is running on macOS."""
        import platform
        return platform.system() == "Darwin"

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-2>" if self.is_mac() else "<Button-3>", self.remove_task)  # Right-click to delete
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def exit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
