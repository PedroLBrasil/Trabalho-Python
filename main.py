#Pedro Lourenço Brasil de Oliveira
#202002679761
#Infelizmente não consegui fazer as abas funcionarem

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

root = Tk()
root.title("Notas de alunos")
width = 800
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

root.config(bg="#6666ff")

materia = StringVar()
matricula = StringVar()
nome = StringVar()
notaAv1 = StringVar()
notaAv2 = StringVar()
notaAv3 = StringVar()
updateWindow = None
id = None
newWindow = None

#media = 0
#if notaAv3 >= notaAv2 > notaAv1 or notaAv2 >= notaAv3 > notaAv1:
# media = (notaAv3 + notaAv2) /2
#else:
# if notaAv3 >= notaAv1 > notaAv2 or notaAv1 >= notaAv3 > notaAv2:
#  media = (notaAv3 + notaAv1) /2
# else:
#     media = (notaAv1 + notaAv2) /2

def database():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'alunos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                materia TEXT, matricula TEXT, nome TEXT, notaAv1 TEXT, notaAv2 TEXT, notaAv3 TEXT) """
    cursor.execute(query)
    cursor.execute('SELECT * FROM alunos ORDER BY materia')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def submitData():

    if materia.get() == "" or matricula.get() == "" or nome.get() == "" or notaAv1.get() == "" or notaAv2.get() == "" or\
            notaAv3.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("alunos.db")
        cursor = conn.cursor()
        query = """INSERT INTO 'alunos' (materia, matricula, nome, notaAv1, notaAv2, notaAv3) VALUES (?, ?, ?, ?, ?, 
        ?) """
        cursor.execute(query, (str(materia.get()), str(matricula.get()),
                               str(nome.get()), str(notaAv1.get()), str(notaAv2.get()), str(notaAv3.get())))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY materia')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        materia.set("")
        matricula.set("")
        nome.set("")
        notaAv1.set("")
        notaAv2.set("")
        notaAv3.set("")


def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    query = """UPDATE 'alunos' SET materia = ?, matricula = ?, nome = ?, notaAv1 = ?, notaAv2 = ?, notaAv3 = ? WHERE 
    id = ? """
    cursor.execute(query, (str(materia.get()), str(matricula.get()),
                           str(nome.get()), str(notaAv1.get()), str(notaAv2.get()), str(notaAv3.get()), int(id)))
    conn.commit()
    cursor.execute('SELECT * FROM alunos ORDER BY materia')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    materia.set("")
    matricula.set("")
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")
    updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo["values"]
    id = selectedItem[0]
    materia.set("")
    matricula.set("")
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")
    materia.set(selectedItem[1])
    matricula.set(selectedItem[2])
    nome.set(selectedItem[3])
    notaAv1.set(selectedItem[4])
    notaAv2.set(selectedItem[5])
    notaAv3.set(selectedItem[6])


    updateWindow = Toplevel()
    updateWindow.title("Atualizar Aluno")
    width = 480
    heigth = 200
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)


    formTitle = Frame(updateWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(updateWindow)
    formContact.pack(side=TOP, pady=10)

    lbl_title = Label(formTitle, text="Atualizar aluno", font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_materia = Label(formContact, text="Materia", font=('arial', 12))
    lbl_materia.grid(row=0, sticky=W)
    lbl_matricula = Label(formContact, text="Matricula", font=('arial', 12))
    lbl_matricula.grid(row=1, sticky=W)
    lbl_nome= Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=2, sticky=W)
    lbl_notaAv1 = Label(formContact, text="Nota Av1", font=('arial', 12))
    lbl_notaAv1.grid(row=3, sticky=W)
    lbl_notaAv2 = Label(formContact, text="Nota Av2", font=('arial', 12))
    lbl_notaAv2.grid(row=4, sticky=W)
    lbl_notaAv3 = Label(formContact, text="Nota Av3", font=('arial', 12))
    lbl_notaAv3.grid(row=5, sticky=W)


    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=0, column=1)
    matriculaEntry = Entry(formContact, textvariable=matricula, font=('arial', 12))
    matriculaEntry.grid(row=1, column=1)
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=2, column=1)
    notaAv1Entry = Entry(formContact, textvariable=notaAv1, font=('arial', 12))
    notaAv1Entry.grid(row=3, column=1)
    notaAv2Entry = Entry(formContact, textvariable=notaAv2, font=('arial', 12))
    notaAv2Entry.grid(row=4, column=1)
    notaAv3Entry = Entry(formContact, textvariable=notaAv3, font=('arial', 12))
    notaAv3Entry.grid(row=5, column=1)


    bttn_update = Button(formContact, text="Atualizar", width=50, command=updateData)
    bttn_update.grid(row=6, columnspan=2, pady=10)


def deletarData():
    if not tree.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar esse aluno?")
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("alunos.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'alunos' WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def inserirData():
    global newWindow
    materia.set("")
    matricula.set("")
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")


    newWindow = Toplevel()
    newWindow.title("Inserir Aluno")
    width = 480
    heigth = 200
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)


    formTitle = Frame(newWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(newWindow)
    formContact.pack(side=TOP, pady=10)

    lbl_title = Label(formTitle, text="Inserir aluno",
                      font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_materia = Label(formContact, text="Materia", font=('arial', 12))
    lbl_materia.grid(row=0, sticky=W)
    lbl_matricula = Label(formContact, text="Matricula", font=('arial', 12))
    lbl_matricula.grid(row=1, sticky=W)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=2, sticky=W)
    lbl_notaAv1 = Label(formContact, text="Nota Av1", font=('arial', 12))
    lbl_notaAv1.grid(row=3, sticky=W)
    lbl_notaAv2 = Label(formContact, text="Nota Av2", font=('arial', 12))
    lbl_notaAv2.grid(row=4, sticky=W)
    lbl_notaAv3 = Label(formContact, text="Nota Av3", font=('arial', 12))
    lbl_notaAv3.grid(row=5, sticky=W)


    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=0, column=1)
    matriculaEntry = Entry(formContact, textvariable=matricula, font=('arial', 12))
    matriculaEntry.grid(row=1, column=1)
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=2, column=1)
    notaAv1Entry = Entry(formContact, textvariable=notaAv1, font=('arial', 12))
    notaAv1Entry.grid(row=3, column=1)
    notaAv2Entry = Entry(formContact, textvariable=notaAv2, font=('arial', 12))
    notaAv2Entry.grid(row=4, column=1)
    notaAv3Entry = Entry(formContact, textvariable=notaAv3, font=('arial', 12))
    notaAv3Entry.grid(row=5, column=1)


    bttn_inserir = Button(formContact, text="Inserir",
                          width=50, command=submitData)
    bttn_inserir.grid(row=6, columnspan=2, pady=10)


def sobreApp():
    pass



top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#6666ff")
mid.pack(side=TOP)
midLeft = Frame(mid, width=100)
midLeft.pack(side=LEFT)
midLeftPadding = Frame(mid, width=350, bg="#6666ff")
midLeftPadding.pack(side=LEFT)
midRight = Frame(mid, width=100)
midRight.pack(side=RIGHT)
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargim = Frame(root, width=500)
tableMargim.pack(side=TOP)


lbl_title = Label(top, text="Cadastro de Notas de Alunos ", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alt = Label(bottom, text="Para alterar clique duas vezes no aluno desejado.", font=('arial', 12), width=200)
lbl_alt.pack(fill=X)


bttn_add = Button(midLeft, text="Inserir", bg="OliveDrab1", command=inserirData)
bttn_add.pack()
bttn_del = Button(midRight, text="Deletar",
                  bg="orange red", command=deletarData)
bttn_del.pack(side=RIGHT)

scrollbarX = Scrollbar(tableMargim, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargim, orient=VERTICAL)

tree = ttk.Treeview(tableMargim, columns=("ID", "Materia", "Matricula", "Nome", "NotaAv1", "NotaAv2", "NotaAv3"),
                    height=400,selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Materia", text="Materia", anchor=W)
tree.heading("Matricula", text="Matricula", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("NotaAv1", text="NotaAv1", anchor=W)
tree.heading("NotaAv2", text="NotaAv2", anchor=W)
tree.heading("NotaAv3", text="NotaAv3", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

menu_bar = Menu(root)
root.config(menu=menu_bar)

fileMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="Criar Novo", command=inserirData)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=root.destroy)

menuSobre = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Se não fizer Av3, coloque 0", command=sobreApp)

if __name__ == '__main__':
    database()
    root.mainloop()
