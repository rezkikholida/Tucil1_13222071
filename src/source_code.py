import numpy as np
import tkinter as tk
import time

def isSafe(queen_matrix, color_matrix, row, column):
    n = len(color_matrix)
    list_color, count_color = cek_warna(queen_matrix, color_matrix, n)

    # cek warna
    warna = color_matrix[row][column]
    if warna in list_color:
        indeks = list_color.index(warna)
        if count_color[indeks] == 1:
            return 1

    # cek apakah pada baris tersebut ada queen
    for i in range(n):
        if queen_matrix[row][i] == 1:
            return 0
        
    # cek apakah pada kolom tersebut ada queen
    for j in range(n):
        if queen_matrix[j][column] == 1:
            return 0
        
    # cek diagonal
        # kiri atas
        if row > 0 and column > 0:
            if queen_matrix[row-1][column-1] == 1:
                return 0
        # kanan atas
        if row > 0 and column < n-2:
            if queen_matrix[row-1][column+1] == 1:
                return 0
        # kiri bawah
        if row < n-2 and column > 0:
            if queen_matrix[row+1][column-1] == 1:
                return 0
        # kanan bawah
        if row < n-2 and column < n-2:
            if queen_matrix[row+1][column+1] == 1:
                return 0
    
    # lolos semua pengecekan
    return 1

def cek_warna(queen_matrix, color_matrix, n):
    list_color = []
    count_color = []

    for i in range(n):
        for j in range(n):
            if queen_matrix[i][j] == 1:
                warna = color_matrix[i][j]
                if warna not in list_color:
                    list_color.append(warna)
                    count_color.append(1)
                else:
                    indeks = list_color.index(warna)
                    count_color[indeks] += 1

    return list_color, count_color

def simpan_txt():
    with open("solusi.txt", "w") as f:
        for i in range(n):
            row_output = ""
            for j in range(n):
                if queen_matrix[i][j] == 1:
                    row_output += "#"
                else:
                    row_output += color_matrix[i][j]
            f.write(row_output + "\n")

    print("Solusi berhasil disimpan sebagai solusi.txt")

# ================================== NAMA FILE ===============================================
with open("input5.txt", "r") as f:
    lines = [list(line.strip()) for line in f]

color_matrix = np.array(lines)
n = len(color_matrix)
queen_matrix = np.zeros((n, n), dtype=int)
row = 0
column = 0
queen_true = 0

# Initial case, pada baris pertama, ada semua queen
for i in range(n):
    queen_matrix[0][i] = 1

# GUI
# mapping warna
color_map = {
    "A": "#96BEFF",  # biru muda
    "B": "#B3DFA0",  # hijau muda
    "C": "#FF7B60",  # coral
    "D": "#BBA3E2",  # ungu muda
    "E": "#E6F388",  # lime
    "F": "#DFDFDF",  # abu terang
    "G": "#FFC992",  # peach
    "H": "#FFAEC9",  # pink
    "I": "#B97A57",  # coklat
    
    "J": "#00BFFF",  # deep sky blue
    "K": "#32CD32",  # lime green
    "L": "#FF1493",  # deep pink
    "M": "#FFD700",  # gold
    "N": "#8A2BE2",  # blue violet
    "O": "#FF4500",  # orange red
    "P": "#20B2AA",  # light sea green
    "Q": "#DC143C",  # crimson
    "R": "#708090",  # slate gray
    
    "S": "#00CED1",  # dark turquoise
    "T": "#ADFF2F",  # green yellow
    "U": "#FF69B4",  # hot pink
    "V": "#1E90FF",  # dodger blue
    "W": "#FF8C00",  # dark orange
    "X": "#9932CC",  # dark orchid
    "Y": "#3CB371",  # medium sea green
    "Z": "#CD5C5C"   # indian red
}

# buat window
root = tk.Tk()
root.title("N Queens")

# buat grid
for i in range(n):
    for j in range(n):
        letter = color_matrix[i][j]
        color = color_map.get(letter, "white")

        if queen_matrix[i][j] == 1:
            text_symbol = "♛"
        else:
            text_symbol = ""

        cell = tk.Label(
            root,
            text=text_symbol,
            fg="black",
            bg=color,
            width=5,
            height=2,
            font=("Segoe UI Symbol", 20),
            highlightthickness=1,
            highlightbackground="black"
        )
        cell.grid(row=i, column=j)
root.mainloop()

# Variabel yang dibutuhkan
waktu_pencarian = 0
banyak_kasus = 0

# Fungsi Utama
start = time.perf_counter()

# Cek 
# cek violation
while queen_true < n:
    if not isSafe(queen_matrix, color_matrix, row, column):
        banyak_kasus += 1
        queen_matrix[row][column] = 0
        if row <= n-2:
            row += 1
        else:
            row = 0
            if column <= n-2: 
                column += 1
            else:
                break
        queen_matrix[row][column] = 1
    else:
        queen_true += 1
        banyak_kasus += 1
        if row <= n-2:
            row += 1
        else:
            row = 0
            if column <= n-2: 
                column += 1
            else:
                break

end = time.perf_counter()

waktu_pencarian = (end - start) * 1000  # jadi milisecond

# Output
for i in range(n):
    row_output = ""
    for j in range(n):
        if queen_matrix[i][j] == 0:
            row_output += color_matrix[i][j]
        else:
            row_output += "#"
    print(row_output)

print(f"Waktu pencarian: {waktu_pencarian} ms")
print(f"Banyak kasus yang ditinjau: {banyak_kasus} kasus")
simpan = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak)")

if simpan.lower() == "ya":
    simpan_txt()
