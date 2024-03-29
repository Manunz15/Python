import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from fpdf import FPDF

#Ciao

class Menubar:
    def __init__(self, parent):
        font_specs = ("cambria", 10)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="Nuovo File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Apri File",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Salva",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Salva come...",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_command(label="Salva come PDF",
                                  accelerator="Ctrl+P",
                                  command=parent.save_pdf)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci",
                                  command=parent.master.destroy)

        calc_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        calc_dropdown.add_command(label="Calcola",
                                  accelerator="Ctrl+R",
                                  command=parent.show_result)
        calc_dropdown.add_command(label="Fattoriale",
                                  accelerator="Ctrl+F",
                                  command=parent.show_factorial)
        
        calc_dropdown.add_separator()
        calc_dropdown.add_command(label="Convertitore",
                                 accelerator="Ctrl+D",
                                  command=parent.conv)
        calc_dropdown.add_command(label="Deconvertitore",
                                 accelerator="Ctrl+Shift+D",
                                  command=parent.deconv)
        calc_dropdown.add_separator()
        calc_dropdown.add_command(label="Informazioni",
                                  command=self.show_oper)
        
        info_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        info_dropdown.add_command(label="Novità",
                                  command=self.show_news_notes)
        info_dropdown.add_command(label="Progetto Karen",
                                  command=self.show_karen_message)
        info_dropdown.add_separator()
        info_dropdown.add_command(label="Versione",
                                  command=self.show_version_notes)

        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Calcolatrice", menu=calc_dropdown)
        menubar.add_cascade(label="Informazioni", menu=info_dropdown)

    def show_oper(self):
        box_title = "Informazioni"
        box_message = "I simboli matematici che puoi usare sono:\nAddizione +\nSottrazione -\nMoltiplicazione *\nDivisione /\nPotenza **\nParentesi e simboli matematici usati su Python"
        messagebox.showinfo(box_title, box_message)

    def show_news_notes(self):
        box_title = "Novità"
        box_message = "Aggiunti: \n-Fattoriale \n-I risultati della calcolatrice\nora appriranno sull'area di testo\n-Convertitore in codice binario\n-Convertitore da codice binario\n-Convertitore in PDF\nRimossi: \n-Formule matematiche"
        messagebox.showinfo(box_title, box_message)

    def show_karen_message(self):
        box_title = "Progetto Karen"
        box_message = "Il progetto Karen è iniziato il 22/07/2019 da Lorenzo Manunza con la versione Karen AT I. Questa versione è un semplice programma creato con Python e TkInter. Inoltre ogni versione a partire da questa avrà il nome di uno scienziato."
        messagebox.showinfo(box_title, box_message)

    def show_version_notes(self):
        box_title = "Versione"
        box_message = "Karen AT III-Gauss \n03/04/2020-09/05/2020"
        messagebox.showinfo(box_title, box_message)


class Statusbar:
    def __init__(self, parent):
        font_specs = ("cambria", 10)

        self.status = tk.StringVar()
        self.status.set("Karen-Gauss")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                         bg="lightgrey", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Il tuo File è stato salvato")
        else:
            self.status.set("Karen-Gauss")


class Karen:
    def __init__(self, master):
        master.title("Karen")
        master.geometry("750x500")
        master.iconbitmap(r'Karen.ico')
        master.resizable(False, False)


        font_specs = ("Cambria", 14)
 
        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)

        self.bind_shortcuts()

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Tutti i file", "*.*"),
                       ("File di Testo", "*.txt"),
                       ("File JavaScript", "*.js"),
                       ("Script Python", "*.py"),
                       ("Markdown Text", "*.md"),
                       ("Documenti HTML", "*.html"),
                       ("Documenti CSS", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                box_title = "Errore"
                box_message = "C'è stato un errore"
                messagebox.showerror(box_title, box_message)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("Tutti i File", "*.*"),
                           ("File di Testo", "*.txt"),
                           ("File di Doc", "*.docx"),
                           ("File JavaScript", "*.js"),
                           ("Script Python", "*.py"),
                           ("Markdown Text", "*.md"),
                           ("Documenti HTML", "*.html"),
                           ("Documenti CSS", "*.css")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.statusbar.update_status(True)
        except Exception as e:
            box_title = "Errore"
            box_message = "C'è stato un errore"
            messagebox.showerror(box_title, box_message)
#pdf
    def save_pdf(self, *args):
        textarea_content = self.textarea.get(1.0, tk.END)
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200,10,txt=textarea_content, ln=1,align="L")
        if self.filename:
            try:
                pdf.output(self.filename+".pdf")
            except Exception as e:
                box_title = "Errore"
                box_message = "C'è stato un errore"
                messagebox.showerror(box_title, box_message)    
        else:
            try:
                new_file = filedialog.asksaveasfilename(
                    initialfile="Untitled.pdf",
                    defaultextension=".pdf",
                    filetypes=[("Tutti i File", "*.*"),
                                ("File PDF", "*.pdf")])
                self.filename = new_file
                pdf.output(self.filename)
                self.statusbar.update_status(True)
            except Exception as e:
                box_title = "Errore"
                box_message = "C'è stato un errore"
                messagebox.showerror(box_title, box_message)
        
#Calcolatrice
    def show_result(self, *args):
        textarea_content = self.textarea.get(1.0, tk.END)
        try:
            x = str(eval(textarea_content))
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(1.0, x)
        except Exception as e:
            box_title = "Errore"
            box_message = "C'è stato un errore"
            messagebox.showerror(box_title, box_message)
#Fattoriale
    def show_factorial(self, *args):
        textarea_content = self.textarea.get(1.0, tk.END)
        def factorial(x):
                    if x == 1 or x == 0:
                        return 1
                    else:
                        return x * factorial(x - 1)
        try:
            x = str(factorial(eval(textarea_content)))
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(1.0, x)
        except Exception as e:
            box_title = "Errore"
            box_message = "C'è stato un errore"
            messagebox.showerror(box_title, box_message)
            
#Convertitore
    def conv (self, *args):
        try:
            x=int(self.textarea.get(1.0, tk.END))
            y=""
            while x>0:
                y=str(x%2)+y
                x=x//2
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(1.0, y)
        except Exception as e:
            box_title = "Errore"
            box_message = "Devi inserire solo numeri"
            messagebox.showerror(box_title, box_message)
            
#Deconvertitore
    def deconv (self, *args):
        textarea_content = self.textarea.get(1.0, tk.END)
        try:
            x = str(eval(textarea_content))
            y=0
            for digit in x:
                y=y*2+int(digit)
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(1.0, str(y))
        except Exception as e:
            box_title = "Errore"
            box_message = "Devi inserire solo numeri in codice binario"
            messagebox.showerror(box_title, box_message)


    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-p>', self.save_pdf)
        self.textarea.bind('<Control-r>', self.show_result)
        self.textarea.bind('<Control-f>', self.show_factorial)
        self.textarea.bind('<Control-d>', self.conv)
        self.textarea.bind('<Control-D>', self.deconv)
        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    master = tk.Tk()
    pt = Karen(master)
    master.mainloop()
