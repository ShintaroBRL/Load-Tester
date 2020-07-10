#   by: Juliano Lira
#   Started: 09/07-08:00
#   Time Spend: 11:30

from Tkinter import *
from lxml import html
import requests
import logging
import threading
import time

# Acho que tem forma melhor de escrever tudo isso aqui

def menu_bar_setup(master):
    #isso e necessario?
    menu_widget = Menu(master)
    menu_widget.add_command(label="Sistema")
    menu_widget.add_command(label="Salvar")
    menu_widget.add_command(label="Carregar")
    master.config(menu=menu_widget)

def config_section(master):
    config_labelframe = LabelFrame(master, text="Config")
    config_labelframe.grid(row=0, column=0, sticky=N+E, padx=10, pady=10)
    
    link_label = Label(config_labelframe, text="Link WEB:")
    link_label.grid(row=0, column=0, sticky='W', padx=(0,10), pady=(0,10))
    config_section.link = Entry(config_labelframe)
    config_section.link.config(width=39)
    config_section.link.grid(row=0, column=1, sticky='W', padx=(0,10), pady=(0,10))

    login_label = Label(config_labelframe, text="login field:")
    login_label.grid(row=1, column=0, sticky='W', padx=(0,10), pady=(0,10))
    config_section.login = Entry(config_labelframe)
    config_section.login.config(width=39)
    config_section.login.grid(row=1, column=1, sticky='W', padx=(0,10), pady=(0,10))

    senha_field = Label(config_labelframe, text="password field:")
    senha_field.grid(row=2, column=0, sticky='W', padx=(0,10), pady=(0,10))
    config_section.senha = Entry(config_labelframe)
    config_section.senha.config(width=39)
    config_section.senha.grid(row=2, column=1, sticky='W', padx=(0,10), pady=(0,10))

    min_users_label = Label(config_labelframe, text="Min Users:")
    min_users_label.grid(row=3, column=0, sticky='W', padx=(5,10), pady=(5,10))
    config_section.min_users = Entry(config_labelframe)
    config_section.min_users.config(width=39)
    config_section.min_users.grid(row=3, column=1, sticky='W', padx=(0,10), pady=(0,10))

    max_users_label = Label(config_labelframe, text="Max Users:")
    max_users_label.grid(row=4, column=0, sticky='W', padx=(5,10), pady=(5,10))
    config_section.max_users = Entry(config_labelframe)
    config_section.max_users.config(width=39)
    config_section.max_users.grid(row=4, column=1, sticky='W', padx=(0,10), pady=(0,10))

    config_section.checked = IntVar()
    logintoken = Checkbutton(config_labelframe, text="use Login Token?", variable=config_section.checked)
    logintoken.grid(row=5, column=1, sticky='W', padx=(5,10), pady=(5,10))

    logintoken_fielddata_label = Label(config_labelframe, text="Login token Data:")
    logintoken_fielddata_label.grid(row=6, column=0, sticky='W', padx=(5,10), pady=(5,10))
    config_section.logintoken_fielddata = Entry(config_labelframe)
    config_section.logintoken_fielddata.config(width=39)
    config_section.logintoken_fielddata.grid(row=6, column=1, sticky='W', padx=(0,10), pady=(0,10))

    config_section.simunt = IntVar()
    logintoken = Checkbutton(config_labelframe, text="Simultaneos?", variable=config_section.simunt)
    logintoken.grid(row=7, column=1, sticky='W', padx=(5,10), pady=(5,10))

def execute_section(master):
    config_labelframe = LabelFrame(master, text="Relatorio")
    config_labelframe.grid(row=0, column=1, sticky=N+W+E, padx=1, pady=10)
    
    exec_button = Button(config_labelframe, text="Executar", command=exec_button_click)
    exec_button.grid(row=0, column=0, sticky=W, padx=(5,10), pady=(5,10))
    execute_section.clear_button = Button(config_labelframe, text="Limpar Saida", command=clear_button_click)
    execute_section.clear_button.grid(row=0, column=0, sticky=W, padx=(62,10), pady=(5,10))

    scrollbar = Scrollbar(config_labelframe)
    scrollbar.grid(row=1, column=1, sticky=N+S+W)
    execute_section.listbox = Listbox(config_labelframe, width=47, height=26)
    execute_section.listbox.grid(row=1, column=0)
    execute_section.listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=execute_section.listbox.yview)

def exec_button_click():
    execute_section.clear_button.config(state="disabled")
    position = 0
    for i in range(int(config_section.min_users.get()), int(config_section.max_users.get())):
        if config_section.simunt:
            x = threading.Thread(target=execute, args=(i,position,))
            x.start()
        else:
            execute(i,position)
        position += 1

def execute(i, position):
    execute_section.listbox.insert(position,"Iniciando "+str(position))
    execute_section.listbox.itemconfig(position, {'bg':'yellow'})
    url = config_section.link.get()
    logintoken = ""

    if config_section.checked.get():
        login_form = {"'"+config_section.login.get()+"'": i, "'"+config_section.senha.get()+"'": i, 'logintoken': logintoken}
    else:
        login_form = {"'"+config_section.login.get()+"'": i, "'"+config_section.senha.get()+"'": i}

    print(url)
    time.sleep(1+position)
    execute_section.listbox.delete(position)
    execute_section.listbox.insert(position,login_form)
    execute_section.listbox.itemconfig(position, {'bg':'green'})
    
def validate_config():
    # escrever aqui uma forma de validar os campos de configuracoes
    pass

def clear_button_click():
    execute_section.listbox.delete(0,'end')
class Application:
    def __init__(self, master=None):
        menu_bar_setup(master)
        config_section(master)
        execute_section(master)

root = Tk()
root.title("Login Flood")
root.geometry("750x500")
root.resizable(width=False, height=False)
Application(root)
root.mainloop()
