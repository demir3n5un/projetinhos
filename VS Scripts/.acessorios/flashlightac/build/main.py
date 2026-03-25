import threading
import time
import pyautogui
from pynput import keyboard
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# =========================
# CONFIGURAÇÕES INICIAIS
# =========================
tecla_ativacao = keyboard.Key.f6
intervalo = 0.1
botao_mouse = "left"
clicando = False
always_on_top = False

# =========================
# AUTO CLICK
# =========================
def auto_click():
    global clicando
    while True:
        if clicando:
            pyautogui.click(button=botao_mouse)
            time.sleep(intervalo)
        else:
            time.sleep(0.1)

def on_press(key):
    global clicando
    if key == tecla_ativacao:
        clicando = not clicando
        status_label.config(text=f"Status: {'ON' if clicando else 'OFF'}")

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x200")

# Fundo
try:
    bg_image = Image.open("1.png")
    bg_image = bg_image.resize((300, 200))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("Imagem 1.png não encontrada.")

# Status
status_label = tk.Label(root, text="Status: OFF", bg="black", fg="white")
status_label.pack(pady=10)

# Always on top toggle
def toggle_top():
    global always_on_top
    always_on_top = not always_on_top
    root.attributes("-topmost", always_on_top)

top_btn = tk.Button(root, text="Always on Top", command=toggle_top)
top_btn.pack(pady=5)

# =========================
# CONFIGURAÇÕES
# =========================
def abrir_config():
    config_win = tk.Toplevel(root)
    config_win.title("Configurações")
    config_win.geometry("250x200")

    tk.Label(config_win, text="Tecla de ativação:").pack(pady=5)
    tecla_entry = tk.Entry(config_win)
    tecla_entry.pack()
    tecla_entry.insert(0, "f6")

    tk.Label(config_win, text="Botão do mouse:").pack(pady=5)
    botao_combo = ttk.Combobox(config_win, values=["left", "right", "middle"])
    botao_combo.pack()
    botao_combo.set(botao_mouse)

    def salvar():
        global tecla_ativacao, botao_mouse

        tecla = tecla_entry.get().lower()

        try:
            tecla_ativacao = getattr(keyboard.Key, tecla)
        except:
            print("Tecla inválida")

        botao_mouse = botao_combo.get()
        config_win.destroy()

    tk.Button(config_win, text="Salvar", command=salvar).pack(pady=10)

config_btn = tk.Button(root, text="Configurações", command=abrir_config)
config_btn.pack(pady=5)

# =========================
# MINIMIZAR AO FECHAR
# =========================
def minimizar_ao_fechar():
    root.withdraw()

root.protocol("WM_DELETE_WINDOW", minimizar_ao_fechar)

# =========================
# THREADS
# =========================
thread = threading.Thread(target=auto_click)
thread.daemon = True
thread.start()

listener = keyboard.Listener(on_press=on_press)
listener.start()

# =========================
# START GUI
# =========================
root.mainloop()