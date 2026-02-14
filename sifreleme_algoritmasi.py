import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from collections import Counter
import re
import pygame
import numpy as np
import threading


# SES

pygame.mixer.init(frequency=44100, size=-16, channels=1)

nota_frekans = {
    "Do": 261.63,
    "Re": 293.66,
    "Mi": 329.63,
    "Fa": 349.23
}

def ses_uret(frekans, sure=0.3, volume=0.5, enstruman="C"):
    sample_rate = 44100
    n_samples = int(sample_rate * sure)
    t = np.linspace(0, sure, n_samples, False)
    
    if enstruman == "C": # PiYano tarzı 
        dalga = np.sin(frekans * t * 2 * np.pi) + 0.5 * np.sin(2 * frekans * t * 2 * np.pi)
        fade_val = 2000
    elif enstruman == "H": # keman tarzı 
        dalga = 0.6 * (np.sin(frekans * t * 2 * np.pi) + 0.3 * np.sin(3 * frekans * t * 2 * np.pi))
        fade_val = 1000
    elif enstruman == "O": # Flüt tarzı 
        dalga = np.sin(frekans * t * 2 * np.pi)
        fade_val = 3000
    else: 
        dalga = np.sin(frekans * t * 2 * np.pi)
        fade_val = 1000

    # tık sesni önlem 
    fade = np.ones(n_samples)
    fade[-fade_val:] = np.linspace(1, 0, fade_val)
    dalga = dalga * fade

    ses = (dalga * 32767 * volume).astype(np.int16)
    ses_stereo = np.column_stack((ses, ses)) 
    return pygame.sndarray.make_sound(ses_stereo)

def nota_dinlet_thread():
    sifreli_icerik = text_sifreli.get("1.0", tk.END).strip()
    if not sifreli_icerik: return

    def cal():
        
        nota_to_el = {v: k for k, v in element_nota.items()}
        
        satirlar = sifreli_icerik.split("\n")
        for satir in satirlar:
            if "|" in satir:
                _, notalar = satir.split("|")
                for n in notalar.split():
                    if n in nota_frekans:
                        element_tipi = nota_to_el.get(n, "C")
                        s = ses_uret(nota_frekans[n], 0.25, enstruman=element_tipi)
                        s.play()
                        pygame.time.delay(200)
                pygame.time.delay(100)

    threading.Thread(target=cal, daemon=True).start()
def nota_dinlet_thread():
   
    sifreli_icerik = text_sifreli.get("1.0", tk.END).strip()
    if not sifreli_icerik:
        return

    def cal():
        satirlar = sifreli_icerik.split("\n")
        for satir in satirlar:
            if "|" in satir:
                _, notalar = satir.split("|")
                nota_listesi = notalar.split()
                for n in nota_listesi:
                    if n in nota_frekans:
                        s = ses_uret(nota_frekans[n], 0.2)
                        s.play()
                        pygame.time.delay(250) # Ntalar arası bekle
                pygame.time.delay(100) # arfler arası 

    threading.Thread(target=cal, daemon=True).start()


harf_koku = {
    "A": "Vanilin", "B": "Mentol", "C": "Limonen", "D": "Geraniol",
    "E": "Eugenol", "F": "Cinnamaldehit", "G": "Anetol", "H": "Carvon",
    "I": "Thymol", "J": "Camphor", "K": "Citral", "L": "Methyl Salicylate",
    "M": "Terpineol", "N": "Isoeugenol", "O": "Furfural", "P": "Borneol",
    "Q": "Safranal", "R": "Myrcene", "S": "Linalool", "T": "Caryophyllene",
    "U": "Humulene", "V": "Guaiacol", "W": "Curcumin", "X": "Nerol",
    "Y": "Farnesol", "Z": "Bisabolol", "?": "Piperonal", "!": "Capsaicin",
    " ": "Boşluk"
}

koku_formul = {
    "Vanilin": "C8H8O3", "Mentol": "C10H20O", "Limonen": "C10H6",
    "Geraniol": "C10H18O", "Eugenol": "C10H12O3",
    "Cinnamaldehit": "C9H8O", "Anetol": "C10H12O",
    "Carvon": "C10H14O", "Thymol": "C10H15O",
    "Camphor": "C10H16O", "Citral": "C10H17O",
    "Methyl Salicylate": "C8H8O2", "Terpineol": "C10H18O3",
    "Isoeugenol": "C10H12O2", "Furfural": "C5H4O2",
    "Borneol": "C10H19O", "Safranal": "C9H13O",
    "Myrcene": "C10H16", "Linalool": "C5H18O",
    "Caryophyllene": "C15H24", "Humulene": "C8H24",
    "Guaiacol": "C7H8O2", "Curcumin": "C21H20O6",
    "Nerol": "C3H48O", "Farnesol": "C15H26O",
    "Bisabolol": "C6H6O4", "Piperonal": "C8H6O3",
    "Capsaicin": "C18H27NO3", "Boşluk": "X1"
}

element_nota = {"C": "Do", "H": "Re", "O": "Mi", "N": "Fa", "X": " "}

def atom_to_nota(atom, sayi):
    nota = element_nota.get(atom, "")
    return [nota] * (sayi if sayi > 0 else 1)


top = tk.Tk()
top.title("Koku & Müzik Kriptografi")
top.geometry("1000x650")

try:
    bg = Image.open("C:/Users/sulta/OneDrive/Desktop/koku.webp")
    bg = bg.resize((1000, 650))
    bg = bg.filter(ImageFilter.GaussianBlur(3))
    bg_photo = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(top, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    top.configure(bg="#d8d7d7")


main_panel = tk.Frame(top, bg="white", padx=30, pady=20)
main_panel.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(main_panel, text="Koku-Müzik Şifreleme", font=("Garamond", 24, "bold"), bg="white", fg="#4A2C2C").pack()
tk.Label(main_panel, text="Moleküllerden Melodilere Güvenli Mesajlar", font=("Garamond", 11), bg="white", fg="#888").pack(pady=(0, 20))

BOX_WIDTH, BOX_HEIGHT = 40, 6


tk.Label(main_panel, text="Şifrelenecek Mesaj:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w")
entry_sifrele = tk.Entry(main_panel, font=("Segoe UI", 12), width=BOX_WIDTH + 8, bd=1, relief="solid")
entry_sifrele.pack(pady=(5, 15), ipady=5)


container = tk.Frame(main_panel, bg="white")
container.pack()


left_box = tk.Frame(container, bg="white")
left_box.grid(row=0, column=0, padx=15)
tk.Label(left_box, text="Oluşan Notalar", font=("Segoe UI", 9, "bold"), bg="white", fg="#555").pack(anchor="w")
text_sifreli = tk.Text(left_box, height=BOX_HEIGHT, width=BOX_WIDTH, font=("Consolas", 10), bg="#fdfdfd")
text_sifreli.pack()

right_box = tk.Frame(container, bg="white")
right_box.grid(row=0, column=1, padx=15)
tk.Label(right_box, text="Çözülecek Notalar", font=("Segoe UI", 9, "bold"), bg="white", fg="#555").pack(anchor="w")
text_coz = tk.Text(right_box, height=BOX_HEIGHT, width=BOX_WIDTH, font=("Consolas", 10), bg="#fdfdfd")
text_coz.pack()


tk.Label(main_panel, text="Çözülen Metin:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(15, 0))
text_cozulmus = tk.Text(main_panel, height=2, width=BOX_WIDTH + 8, font=("Segoe UI", 12, "bold"), bg="#f2f3f2", bd=0)
text_cozulmus.pack(pady=5)


def sifrele():
    metin = entry_sifrele.get()
    sifreli_metin = []
    for harf in metin:
        harf_upper = harf.upper()
        if harf_upper in harf_koku:
            koku = harf_koku[harf_upper]
            formul = koku_formul[koku]
            atomlar = re.findall(r'([A-Z])(\d*)', formul)
            notalar = []
            for atom, sayi in atomlar:
                sayi = int(sayi) if sayi else 1
                notalar.extend(atom_to_nota(atom, sayi))
            harf_tipi = "L" if harf.islower() else "U"
            sifreli_metin.append(f"{harf_tipi}|{' '.join(notalar)}")
    text_sifreli.delete("1.0", tk.END)
    text_sifreli.insert(tk.END, "\n".join(sifreli_metin))

def coz():
    sifreli_metin = text_coz.get("1.0", tk.END).strip()
    nota_element = {v.lower(): k for k, v in element_nota.items()}
    satirlar = sifreli_metin.split("\n")
    sonuc = []
    for satir in satirlar:
        if "|" not in satir: continue
        harf_tipi, nota_kisim = satir.split("|", 1)
        notalar = nota_kisim.split()
        elementler = [nota_element.get(n.lower(), "?") for n in notalar]
        if " " in elementler: continue
        sayim = Counter(elementler)
        formul = "".join(f"{el}{sayim[el] if sayim[el] > 1 else ''}" for el in sorted(sayim))
        koku = next((k for k, v in koku_formul.items() if v == formul), " ")
        harf = next((h for h, v in harf_koku.items() if v == koku), " ")
        if harf_tipi == "L": harf = harf.lower()
        sonuc.append(harf)
    text_cozulmus.delete("1.0", tk.END)
    text_cozulmus.insert(tk.END, "".join(sonuc))

def temizle():
    entry_sifrele.delete(0, tk.END)
    text_sifreli.delete("1.0", tk.END)
    text_coz.delete("1.0", tk.END)
    text_cozulmus.delete("1.0", tk.END)


btn_frame = tk.Frame(main_panel, bg="white")
btn_frame.pack(pady=15)

btn_opt = {"font": ("Segoe UI", 9, "bold"), "width": 14, "bd": 1, "cursor": "hand2"}

tk.Button(btn_frame, text="ŞİFRELE", command=sifrele, bg="#4A2C2C", fg="white", **btn_opt).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="DINLET ", command=nota_dinlet_thread, bg="#7FA37C", fg="white", **btn_opt).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="ÇÖZ", command=coz, bg="#6B8EAD", fg="white", **btn_opt).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="TEMİZLE", command=temizle, bg="#dcdcdc", fg="black", **btn_opt).grid(row=0, column=3, padx=5)

top.mainloop()