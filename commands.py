from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
import os

class TextEditor(Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        self.frm = Frame(parent)
        self.frm.pack(fill=X)
        # self.create_title()
        parent.title('Rules Editor')
        self.create_button()
        self.main_text()
        self.set_text(text='',file=file)
        self.kolomTeks.config(font=('DejaVu Sans Mono', 10))
        self.path = ''
        text = self.readFile('test.clp')
        self.kolomTeks.delete('0.1',END)
        self.kolomTeks.insert(END, text)

    def create_button(self):
        Button(self.frm, text='Simpan',relief='flat',  command=self.save_command).pack(side=LEFT)

    def main_text(self):
        scroll = Scrollbar(self)
        kolomTeks = Text(self, relief=SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        kolomTeks.pack(side=LEFT, expand=YES, fill=BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=YES, fill=BOTH)

    def save_command(self):
        print(self.path)
        if self.path:
            alltext = self.get_text()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'Selamat File telah tersimpan ! ')
        else:
            tipeFile = [('Text file', '*.txt'), ('Python file', '*asdf.py'), ('All files', '.*')]
            alltext = self.get_text()
            open('test.clp', 'w').write(alltext)
            self.master.destroy()

    def set_text(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.kolomTeks.delete('1.0', END)
        self.kolomTeks.insert('1.0', text)
        self.kolomTeks.mark_set(INSERT, '1.0')
        self.kolomTeks.focus()

    def get_text(self):
        return self.kolomTeks.get('1.0', END+'-1c')

    def create_title(self):
        top = Frame(root)
        top.pack(fill=BOTH, expand=1, padx=17, pady=5)
        judul = Label(top, text="Judul : ")
        judul.pack(side="left")
        self.kolomJudul = Entry(top)
        self.kolomJudul.pack(side="left")

    def open_file(self):
        extensiFile = [ ('All files', '*'), ('Text files', '*.txt'),('Python files', '*.py')]
        buka = filedialog.askopenfilename(filetypes = extensiFile)

    def readFile(self, filename):
        try:
            f = open(filename, "r")
            text = f.read()
            return text
        except:
            messagebox.showerror("Error!!","Maaf file tidak dapat dibuka ! :) \nsabar ya..")
            return None

class show_facts(Frame):
    def __init__(self, parent=None, file=None,facts=None):
        Frame.__init__(self, parent)
        parent.title('Show Facts')
        self.show_facts = scrolledtext.ScrolledText(parent, state='normal',width=40,height=20)
        self.show_facts.configure(font='TkFixedFont')
        self.show_facts.grid(row=0, column=0,padx=(5, 5),pady=(5,5))
        for fact in facts:
            self.show_facts.insert(INSERT,fact+'\n')
        self.show_facts.config(state=DISABLED)

class show_rules(Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        parent.title('Show Rules')
        self.show_rules = scrolledtext.ScrolledText(parent, state='normal',width=40,height=20)
        self.show_rules.configure(font='TkFixedFont')
        self.show_rules.grid(row=0, column=0,padx=(5, 5),pady=(5,5))
        rules = open('test.clp', 'r').read()
        self.show_rules.delete('1.0', END)
        self.show_rules.insert('1.0', rules)
        self.show_rules.mark_set(INSERT, '1.0')
        self.show_rules.focus()
        self.show_rules.config(state=DISABLED)