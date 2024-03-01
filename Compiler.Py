import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import subprocess

class IDE:
    def __init__(self, root):
        self.root = root
        self.root.title('Python IDE')
        self.root.iconbitmap("icon.ico")

        self.root.geometry('600x600')

        self.file_path = ''
        self.saved_files = []

        self.create_widgets()

    def create_widgets(self):
        self.create_menu_bar()
        self.create_frames()

    def create_menu_bar(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_as)
        file_menu.add_command(label='Save As', command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.exit_program)
        menu_bar.add_cascade(label='File', menu=file_menu)

        run_menu = Menu(menu_bar, tearoff=0)
        run_menu.add_command(label='Run', command=self.run_code)
        menu_bar.add_cascade(label='Run', menu=run_menu)
     #config menu bar
        self.root.config(menu=menu_bar)
    #create frames
    def create_frames(self):
        frame = Frame(self.root)
        frame.pack(fill=BOTH, expand=YES)

        file_explorer_frame = Frame(frame, width=10, bg='#2E2E2E')
        file_explorer_frame.pack(side=LEFT, fill=BOTH)

        file_explorer_label = Label(file_explorer_frame, text='Explorer', font=('Helvetica', 10, 'bold'), bg='#FFDAB9', fg='black')
        file_explorer_label.pack(pady=(10, 5))

        self.file_explorer_columns = ('File Name',)
        self.file_explorer = ttk.Treeview(file_explorer_frame, columns=self.file_explorer_columns, show='headings', height=10)
        self.file_explorer.heading('File Name', text='File Name')

        self.file_explorer.pack(fill=BOTH, expand=YES)
        self.file_explorer.bind('<ButtonRelease-1>', self.on_file_explorer_click)

    #create a decorative line using canvas
        canvas = Canvas(frame, width=2, bg='#333333', highlightthickness=0)
        canvas.pack(side=LEFT, fill=Y, padx=5)
        canvas.create_line(1, 0, 1, frame.winfo_height(), fill='#555555')  

        editor_frame = Frame(frame, bg='#87CEEB')
        editor_frame.pack(side=TOP, fill=BOTH, expand=YES)
        
        # create a decorative line using canva
        canvas = Canvas(frame, height=2, bg='#333333', highlightthickness=0)
        canvas.pack(side=TOP, fill=X, pady=5)
        canvas.create_line(0, 1, frame.winfo_width(), 1, fill='#555555')  

        output_frame = Frame(frame, bg='#FFFF00')
        output_frame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        #create a text widgets
        self.editor = Text(editor_frame, wrap='word', undo=True, bg='#ADD8E6', fg='black')
        self.editor.pack(side=LEFT, fill=BOTH, expand=YES)


        self.code_output = Text(output_frame, height=10, wrap='word', bg='#FFFFE0', fg='black')
        self.code_output.pack(side=LEFT, fill=BOTH, expand=YES)

    #add scrollbar
        editor_scroll = Scrollbar(editor_frame, command=self.editor.yview)
        editor_scroll.pack(side=RIGHT, fill=Y)
        self.editor.config(yscrollcommand=editor_scroll.set)

        output_scroll = Scrollbar(output_frame, command=self.code_output.yview)
        output_scroll.pack(side=RIGHT, fill=Y)
        self.code_output.config(yscrollcommand=output_scroll.set)

        #set colors
        
        frame.configure(bg='#87CEEB') 
        file_explorer_frame.configure(bg='#E6E6FA')  
        editor_frame.configure(bg='#87CEEB')  
        output_frame.configure(bg='#FFFF00')  
        self.editor.configure(bg='#ADD8E6', fg='black', insertbackground='black')  
        self.code_output.configure(bg='#FFFFE0', fg='black')  

    def open_file(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        if path:
            with open(path, 'r') as file:
                code = file.read()
                self.editor.delete('1.0', END)
                self.editor.insert('1.0', code)
                self.file_path = path
                self.update_saved_files(path)

    def save_as(self):
        if self.file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = self.file_path

        if path:
            with open(path, 'w') as file:
                code = self.editor.get('1.0', END)
                file.write(code)
                self.file_path = path
                self.update_saved_files(path)

    def update_saved_files(self, new_file):
        if new_file not in self.saved_files:
            self.saved_files.append(new_file)
            self.update_file_explorer()

    def update_file_explorer(self):
        self.file_explorer.delete(*self.file_explorer.get_children())
        for saved_file in self.saved_files:
            self.file_explorer.insert('', 'end', values=(os.path.basename(saved_file),))

    def on_file_explorer_click(self, event):
        item_id = self.file_explorer.selection()
        if item_id:
            selected_file = self.saved_files[int(item_id[0]) - 1]
            with open(selected_file, 'r') as file:
                code = file.read()
                self.editor.delete('1.0', END)
                self.editor.insert('1.0', code)
                self.file_path = selected_file

    def run_code(self):
        if self.file_path == '':
            messagebox.showinfo("Error", "Please save your code before running.")
            return

        command = f'python "{self.file_path}"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.code_output.delete('1.0', END)
        self.code_output.insert('1.0', f"Output:\n{output.decode('utf-8')}")
        self.code_output.insert('1.0', f"Error:\n{error.decode('utf-8')}")

    def exit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    ide = IDE(root)
    root.mainloop()
