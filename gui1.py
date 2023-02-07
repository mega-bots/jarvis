import tkinter as tk
from PIL import Image,ImageTk

class JarvisGUI:
    def __init__(self, master):
        print("hello")
        self.master = master
        self.master.geometry("700x500")
        self.master.title("Jarvis")

        # Load and set the background image
        self.background_image = Image.open("1.jpg")
        self.background_image = self.background_image.resize((1920,500),Image.Resampling.LANCZOS)
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.pack(fill = 'both',expand='yes')

        # Create the text box and associated button
        self.enter_command_button = tk.Button(self.background_label, text="Enter Command", foreground='black', background='white', font=("Helvetica", 16), command=self.get_command)
        self.enter_command_button.pack(side="bottom")
        self.text_box = tk.Entry(self.background_label, foreground='black', background='white', font=("Helvetica", 16))
        self.text_box.pack(side="bottom")
        

        # Create the scrollable list box
        self.scrollbar = tk.Scrollbar(self.background_label)
        self.scrollbar.pack(side='right', fill='y')
        self.list_box = tk.Listbox(self.background_label, yscrollcommand=self.scrollbar.set, font=("Helvetica", 16), bg='black', fg='green')
        self.list_box.pack(side='right')
        self.scrollbar.config(command=self.list_box.yview)

    def get_command(self):
        command = self.text_box.get()
        self.text_box.delete(0, 'end')
        self.list_box.insert('end', 'You: ' + command)
        print(command)

root = tk.Tk()  
jarvis = JarvisGUI(root)
root.mainloop
