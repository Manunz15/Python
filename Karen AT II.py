import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


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
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci",
                                  command=parent.master.destroy)

        calc_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        calc_dropdown.add_command(label="Gravitazione",
                                  command=self.show_grav_notes)
        calc_dropdown.add_command(label="Energia cinetica",
                                  command=self.show_energy_notes)
        calc_dropdown.add_command(label="Spinta di Archimede",
                                  command=self.show_arch_notes)
        calc_dropdown.add_separator()
        calc_dropdown.add_command(label="Calcola",
                                  accelerator="Ctrl+R",
                                  command=parent.show_result)

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

    def show_grav_notes(self):
        box_title = "Gravitazione"
        box_message = "F=(GmM)/(r^2) \n(G=6,67x10^-11)"
        messagebox.showinfo(box_title, box_message)

    def show_energy_notes(self):
        box_title = "Energia Cinetica"
        box_message = "K=(1/2)mv^2"
        messagebox.showinfo(box_title, box_message)

    def show_arch_notes(self):
        box_title = "Spinta di Archimede"
        box_message = "F=dVg"
        messagebox.showinfo(box_title, box_message)

    def show_news_notes(self):
        box_title = "Novità"
        box_message = "Aggiunti: \n-Interfaccia Grafica \n-Editor testuale \n-Menubar \n-Statusbar \nRimossi: \n-Fattoriale \nMigliorati: \n-Calcolatrice"
        messagebox.showinfo(box_title, box_message)

    def show_karen_message(self):
        box_title = "Progetto Karen"
        box_message = "Il progetto Karen è iniziato il 22/07/2019 da Lorenzo Manunza con la versione Karen AT I. Questa versione è un semplice programma creato con Python e TkInter. Inoltre ogni versione a partire da questa avrà il nome di uno scienziato."
        messagebox.showinfo(box_title, box_message)

    def show_version_notes(self):
        box_title = "Versione"
        box_message = "Karen AT II-Newton \n28/07/2019-05/08/2019"
        messagebox.showinfo(box_title, box_message)


class Statusbar:
    def __init__(self, parent):
        font_specs = ("cambria", 10)

        self.status = tk.StringVar()
        self.status.set("Karen-Newton")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                         bg="lightgrey", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Il tuo File è stato salvato")
        else:
            self.status.set("Karen-Newton")


class Karen:
    def __init__(self, master):
        master.title("Karen")
        master.geometry("750x500")
        master.iconbitmap(r'K.ico')
        master.resizable(False, False)

        font_specs = ("cambria", 14)

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
                messagebox.showinfo(box_title, box_message)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("Tutti i File", "*.*"),
                           ("File di Testo", "*.txt"),
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
            messagebox.showinfo(box_title, box_message)

    def show_result(self, *args):
        textarea_content = self.textarea.get(1.0, tk.END)
        try:
            x = str(eval(textarea_content))
            box_title = "Risultato"
            box_message = x
            messagebox.showinfo(box_title, box_message)
        except Exception as e:
            box_title = "Errore"
            box_message = "C'è stato un errore"
            messagebox.showinfo(box_title, box_message)

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-r>', self.show_result)
        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    master = tk.Tk()
    pt = Karen(master)
    master.mainloop()