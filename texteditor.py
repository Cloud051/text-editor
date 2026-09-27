from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("650x590")
root.title("Phantom Notes")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_info = Text(
    root,
    yscrollcommand=scrollbar.set,
    font=("sans-serif", 20),
    selectbackground="gray",
    wrap="word"
)

text_info.pack(fill=BOTH)
scrollbar.config(command=text_info.yview)

app_icon = PhotoImage(file="lgo.png")
root.iconphoto(True, app_icon)

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_info.get("1.0", "end-1c"))

root.bind("<Control-s>", save_file)

root.mainloop()