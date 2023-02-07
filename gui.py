import tkinter as tk
def store_value():
    val = entry.get()
    print(val)
    entry.delete(0,'end')
    return val
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
main_frame = tk.Frame(master=root)
chat_listbox = tk.Listbox(master=main_frame, height=200, width=50)
scroll_bar = tk.Scrollbar(master=main_frame)
btn = tk.Button(root,text ="enter command : ",command = lambda: None,compound='right')
btn.pack(side='top')
speak_button = tk.Button(master=root, text='Speak', command=lambda: None,bg='grey')
def set_speak_command(command):
    print(command)
    speak_button.configure(command=command)
def set_btn(command):
    btn.configure(command=command)



speak_button.pack(side=tk.LEFT, anchor=tk.SW)


def speak(text):
    chat_listbox.insert('end', f'Assistant: {text}')


scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.pack(fill=tk.Y, side=tk.RIGHT)
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)
main_frame.pack(fill=tk.BOTH)
root.geometry('700x500')
root.minsize(700, 500)
root.wm_title('Jarvis')
root.resizable(False, True)
mainloop = root.mainloop