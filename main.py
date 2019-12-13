from tkinter import Frame,Tk,Label,Button,END,ttk,scrolledtext,filedialog,Toplevel
from Analyzer import *
from ClipsEngine import *
from commands import *
import PIL.Image
import PIL.ImageTk
import logging
import cv2


class Application(Frame):

    # Constructor
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.analyzer = Analyzer()
        self.path_clp='test.clp'
        self.engine = ClipsEngine()
        self.engine._reload_clp(self.path_clp)
        self.create_widgets()
    
    # Get image file
    def get_image_file(self):
        self.analyzer = Analyzer()
        self.engine = ClipsEngine()
        self.engine._reload_clp(self.path_clp)
        # Open browse file window
        file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
            getphoto = PIL.Image.open(file)
            # self.logger.warn(self.item_text)
            self.analyzer._read_file(file=file.name)
            getphoto = getphoto.resize((250, 250), PIL.Image.ANTIALIAS) 
            print("I got %d bytes from this file." % len(data))
            self.display_image(getphoto)

            self.analyzer._detect_sudut()
            # self.analyzer._find_suduts()
            self.analyzer._find_simpul()
            facts = self.analyzer._extract_fact()
            self.engine._add_facts(facts)
    
    def open_text_editor(self):
        self.newWindow = Toplevel(root)
        self.app=TextEditor(self.newWindow)
        self.engine = ClipsEngine()
        self.engine._reload_clp(self.path_clp)

    def show_rules(self):
        self.newWindow = Toplevel(root)
        self.app=show_rules(self.newWindow)

    def show_facts(self):
        facts=self.analyzer._get_facts()
        self.newWindow = Toplevel(root)
        self.app=show_facts(self.newWindow,facts=facts)


    def run(self):
        result = self.engine._detect("("+self.item_text[0]+")")

        self.detectionResult.config(state='normal')
        self.matchedFacts.config(state='normal')
        self.hitRules.config(state='normal')

        self.detectionResult.delete('1.0', END)
        self.matchedFacts.delete('1.0', END)
        self.hitRules.delete('1.0', END)

        if(result):
            self.detectionResult.insert(INSERT,"true\n")
        else:
            self.detectionResult.insert(INSERT,"false\n")

        for fact in self.engine._get_facts():
            self.matchedFacts.insert(INSERT,str(fact)+'\n')

        im = self.analyzer._get_image()
        b,g,r = cv2.split(im)
        im = cv2.merge((r,g,b))

        img = PIL.Image.fromarray(im)
        img = img.resize((250, 250), PIL.Image.ANTIALIAS) 
        # img =  img.thumbnail((250, 250), PIL.Image.ANTIALIAS)
        imgtk = PIL.ImageTk.PhotoImage(image=img) 
        self.panel2.configure(image=imgtk)
        self.panel2.image = imgtk
        
        # Hit Rules
        hit_rules=self.engine._get_hit_rule()
        print("hit_rules")
        print(hit_rules)
        for hit_rule in hit_rules:
            print(hit_rule)
            self.hitRules.insert(INSERT,hit_rule.name+"\n")

        self.detectionResult.config(state=DISABLED)
        self.matchedFacts.config(state=DISABLED)
        self.hitRules.config(state=DISABLED)

    # Update chosen image on image widget
    def display_image(self,photo):
        img = PIL.ImageTk.PhotoImage(photo)
        self.panel1.configure(image=img)
        self.panel1.image = img 

    def create_widgets(self):

        # Set up image widget
        Label(root,text="Source Image",).grid(row=0, column=0)
        framet = Frame(root, bg="white", height="300", width="300")
        framet.grid(row=1, column=0, rowspan=9)
        framet.pack_propagate(False)
        self.panel1 = Label(framet, image=None,text="No image selected.\n Please Select an Image \n Click the Open Image Button to Open an Image", bg='white')
        self.panel1.pack()

        Label(root,text="Detection Image").grid(row=0, column=1)
        framet2 = Frame(root, bg="white", height="300", width="300")
        framet2.grid(row=1, column=1, rowspan=9)
        framet2.pack_propagate(False)
        self.panel2 = Label(framet2,text="No shape selected \n Please Select a Shape \n Click Shape Tree Item 2 Times \n to Detect Shape from Image",image=None, bg="white")
        self.panel2.pack()
        
        # Set up button list
        Button(text="Open Image",command=self.get_image_file).grid(row=1, column=2,pady=(4, 4),sticky="nesw")
        Button(text="Open Rule Editor",command=self.open_text_editor).grid(row=2, column=2,pady=(4, 4),sticky="nesw")
        Button(text="Show Rules",command=self.show_rules).grid(row=3, column=2,pady=(4, 4),sticky="nesw")
        Button(text="Show Facts",command=self.show_facts).grid(row=4, column=2,pady=(4, 4),sticky="nesw")
        # Button(text="Run",command=self.run).grid(row=5, column=2,pady=(4, 4),sticky="nesw")


        # Set up tree view
        self.tree = ttk.Treeview(root, show="tree")
        # Level 1
        triangle=self.tree.insert("",END, text="Segitiga", values=("bentuk_segitiga"))
        quadrilateral=self.tree.insert("",END, text="Segiempat", values=("bentuk_segiempat"))
        pentagon=self.tree.insert("",END, text="Segi lima", values=("bentuk_segilima"))
        hexagon=self.tree.insert("",END, text="Segi enam", values=("bentuk_segienam"))
        # Level 2
        triangle0 = self.tree.insert(triangle,END, text="beraturan",values=("segitiga_beraturan"))
        triangle1 = self.tree.insert(triangle,END, text="tidak beraturan",values=("segitiga_tidak_beraturan"))
        self.tree.insert(triangle0,END, text="lancip",values=("segitiga_lancip"))
        self.tree.insert(triangle0,END, text="tumpul", values=("segitiga_tumpul"))
        self.tree.insert(triangle0,END, text="siku-siku",values=("segitiga_siku"))
        folder5=self.tree.insert(triangle0,END, text="sama kaki", values=("segitiga_samakaki"))
        self.tree.insert(triangle0,END, text="sama sisi", values=("segitiga_samasisi"))

        self.tree.insert(folder5,END, text="siku-siku",values=("segitiga_siku_samakaki"))
        self.tree.insert(folder5,END, text="tumpul", values=("segitiga_tumpul_samakaki"))
        self.tree.insert(folder5,END, text="lancip",values=("segitiga_lancip_samakaki"))


        triangle2 = self.tree.insert(quadrilateral,END, text="Segiempat beraturan",values=("segiempat_beraturan"))
        triangle3 = self.tree.insert(quadrilateral,END, text="Segiempat tidak beraturan",values=("segiempat_tidak_beraturan"))
        folder6=self.tree.insert(triangle2,END, text="Jajaran Genjang",values=("jajarangenjang"))
        self.tree.insert(triangle2,END, text="Persegi",values=("persegi"))
        self.tree.insert(triangle2,END, text="Persegi Panjang",values=("persegi_panjang"))


        self.tree.insert(folder6,END, text="Jajaran Genjang beraturan",values=("jajar_genjang_beraturan"))
        self.tree.insert(folder6,END, text="Jajaran Genjang berbentuk layang-layang", values=("jajar_genjang_layang_layang"))

        folder7=self.tree.insert(triangle2,END, text="Trapesium", values=("trapesium"))

        self.tree.insert(folder7,END, text="Trapesium sama kaki",values=("trapesium_sama_kaki"))
        self.tree.insert(folder7,END, text="Trapesium rata sisi", values=("trapesium_rata_sisi"))

        triangle4 = self.tree.insert(pentagon,END, text="beraturan",values=("segilima_beraturan"))
        triangle5 = self.tree.insert(pentagon,END, text="tidak beraturan",values=("segilima_tidak_beraturan"))

        triangle6 = self.tree.insert(hexagon,END, text="beraturan",values=("segienam_beraturan"))
        triangle7 = self.tree.insert(hexagon,END, text="tidak beraturan",values=("segienam_tidak_beraturan"))

        self.chosen_shape = Label(root,text="Chosen shape :")
        self.chosen_shape.grid(row=5, column=2, sticky="nesw")

        self.tree.grid(row=6, column=2,rowspan=5,pady=(4, 4),sticky="nesw")
        self.tree.bind("<Double-1>", self.on_tree_select)

        # Set up scrolled text
        Label(root,text="Detection Result").grid(row=14, column=0)
        self.detectionResult = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.detectionResult.configure(font='TkFixedFont')
        self.detectionResult.grid(row=15, column=0,padx=(3, 3),pady=(0,5))
        
        Label(root,text="Matched Facts").grid(row=14, column=1)
        self.matchedFacts = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.matchedFacts.configure(font='TkFixedFont')
        self.matchedFacts.grid(row=15, column=1,padx=(3, 3),pady=(0,5))

        Label(root,text="Hit Rules").grid(row=14, column=2)
        self.hitRules = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.hitRules.configure(font='TkFixedFont')
        self.hitRules.grid(row=15, column=2,padx=(3, 3),pady=(0,5))
    
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree.selection():
            self.item_text = self.tree.item(item,"value")
            self.chosen_shape.config(text='Chosen shape : '+self.item_text[0])
        self.run()

root = Tk(className='KBS Shape Detector')
root.geometry("1060x600")
root.resizable(0, 0)

 
app = Application(master=root)
app.mainloop()
root.destroy()