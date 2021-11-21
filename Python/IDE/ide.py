from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import tkinter.scrolledtext
import tkinter.messagebox as msg
import platform
import sys
import subprocess
import os

icondir = f'{sys.base_prefix}/Lib/idlelib/Icons'
compiler = Tk()
name = 'VisualCharm'
compiler.title(f"*untitled* - {name}")
file_path = ''
iconfile = os.path.join(icondir, 'idle.ico')
compiler.wm_iconbitmap(default=iconfile)

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    try:
        with open(path,'r') as file:
            code = file.read()
            editor.delete('1.0',END)
            editor.insert('1.0',code)
            set_file_path(path)
            compiler.title(f"{path} - {name}")
    except:
        pass

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)
        compiler.title(f"{path} - {name}")

def run():
    if file_path == '':
        msg.showinfo('Please save your code','Please save your code')
    else:
        command = f'python {file_path}'
        save_as()
        process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        output,error = process.communicate()
        code_output.config(state='normal')
        code_output.insert('1.0',output)
        code_output.insert('1.0',error)
        code_output.insert('1.0',f'==== {file_path} ====\n')
        code_output.config(state='disabled')

def update_label():
    row, col = editor.index('insert').split('.')
    label.config(text=f'Python {platform.python_version()}   Line {row}, Column {col}')
    compiler.after(100, update_label)


def get_text_coord(s: str, i: int):
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'
        
        i -= len(line)

def _sphinx_version():
    major, minor, micro, level, serial = sys.version_info
    release = '%s%s' % (major, minor)
    release += '%s' % (micro,)
    if level == 'candidate':
        release += 'rc%s' % (serial,)
    elif level != 'final':
        release += '%s%s' % (level[0], serial)
    return release

def open_manuals():
    dir = chmfile = os.path.join(sys.base_prefix, 'Doc','Python%s.chm' % _sphinx_version())
    os.system(f'{dir}')

def open_demo():
    os.system(f'{sys.base_prefix}/Lib/turtledemo/__main__.py')

editor = tkinter.scrolledtext.ScrolledText(undo=True)
editor.pack()

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save as',command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label="Run",menu=run_bar)

edit_bar = Menu(menu_bar,tearoff=0)
edit_bar.add_command(label='Undo',command=editor.edit_undo)
edit_bar.add_command(label='Redo',command=editor.edit_redo)
menu_bar.add_cascade(label="Edit",menu=edit_bar)

manual_bar = Menu(menu_bar,tearoff=0)
manual_bar.add_command(label='Python docs',command=open_manuals)
manual_bar.add_command(label='Turtle demo',command=open_demo)
menu_bar.add_cascade(label="Help",menu=manual_bar)

compiler.config(menu=menu_bar)

code_output = tkinter.scrolledtext.ScrolledText(height=10,state='disabled')
code_output.pack()

label = Label(compiler, anchor='e')
label.pack(fill='x')

update_label()
compiler.mainloop()
