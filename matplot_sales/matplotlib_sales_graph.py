import pandas as pd
import matplotlib.pyplot as plt

# Bella Febriana

# fungsi nomor satu
def function_satu():
    # Membaca data dari file Excel
    df = pd.read_csv('transaction_dataset.csv')

    # Menghitung total penjualan per kota dan customer name
    grouped = df.groupby(['City', 'Customer Name'])['Sales'].sum().reset_index()

    # Mencari customer name dengan total penjualan terbanyak per kota
    idx = grouped.groupby(['City'])['Sales'].transform(max) == grouped['Sales']
    result = grouped[idx].reset_index(drop=True)

    # Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
    result = result.sort_values(by=['Sales'], ascending=False)

    # Menampilkan hasil dalam bentuk tabel
    print(result[['City', 'Customer Name', 'Sales']])

    # Menampilkan grafik batang horizontal
    plt.barh(result['City'], result['Sales'])
    plt.title('Total Sales per City by Top Customer Name')
    plt.xlabel('Total Sales')
    plt.ylabel('City')
    plt.show()


# fungsi nomor dua
def function_dua():
    # Membaca data dari file Excel
    df = pd.read_csv('transaction_dataset.csv')

    # Menghitung total penjualan per state dan customer name
    grouped = df.groupby(['State', 'Customer Name'])['Sales'].sum().reset_index()

    # Mencari customer name dengan total penjualan terbanyak per state
    idx = grouped.groupby(['State'])['Sales'].transform(max) == grouped['Sales']
    result = grouped[idx].reset_index(drop=True)

    # Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
    result = result.sort_values(by=['Sales'], ascending=False)

    # Menampilkan hasil
    print(result[['State', 'Customer Name', 'Sales']])

    # Menampilkan grafik batang horizontal
    plt.barh(result['State'], result['Sales'])
    plt.title('Total Sales per State by Top Customer Name')
    plt.xlabel('Total Sales')
    plt.ylabel('State')
    plt.show()

#fungsi nomor tiga
def function_tiga():
    # Membaca data dari file CSV
    df = pd.read_csv('transaction_dataset.csv')

    # Menghitung total penjualan per kategori dan product name
    grouped = df.groupby(['Category', 'Product Name'])['Sales'].sum().reset_index()

    # Mencari product name dengan total penjualan terbanyak per kategori
    idx = grouped.groupby(['Category'])['Sales'].transform(max) == grouped['Sales']
    result = grouped[idx].reset_index(drop=True)

    # Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
    result = result.sort_values(by=['Sales'], ascending=False)

    # Menampilkan hasil
    print(result[['Category', 'Product Name', 'Sales']])

    # Menampilkan grafik batang horizontal
    plt.barh(result['Product Name'], result['Sales'])
    plt.title('Total Sales per Product Name by Category')
    plt.xlabel('Total Sales')
    plt.ylabel('Product Name')
    plt.show()

#fungsi nomor empat
def function_empat():
    # Membaca data dari file Excel
    df = pd.read_csv('transaction_dataset.csv')

    # Menghitung total penjualan per segment dan customer name
    grouped = df.groupby(['Segment', 'Customer Name'])['Sales'].sum().reset_index()

    # Mencari customer name dengan total penjualan terbanyak per segment
    idx = grouped.groupby(['Segment'])['Sales'].transform(max) == grouped['Sales']
    result = grouped[idx].reset_index(drop=True)

    # Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
    result = result.sort_values(by=['Sales'], ascending=False)

    # Menampilkan hasil
    print(result[['Segment', 'Customer Name', 'Sales']])

    # Menampilkan grafik batang horizontal
    plt.barh(result['Segment'], result['Sales'])
    plt.title('Total Sales per Segment by Top Customer Name')
    plt.xlabel('Total Sales')
    plt.ylabel('Segment')
    plt.show()

#fungsi nomor lima
def function_lima():
    # Membaca data dari file Excel
    df = pd.read_csv('transaction_dataset.csv')

    # Menghitung total penjualan per Ship Mode
    grouped = df.groupby(['Ship Mode'])['Sales'].sum().reset_index()

    # Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
    result = grouped.sort_values(by=['Sales'], ascending=False).reset_index(drop=True)

    # Menampilkan hasil
    print(result[['Ship Mode', 'Sales']])

    # Menampilkan grafik batang horizontal
    plt.barh(result['Ship Mode'], result['Sales'])
    plt.title('Total Sales per Ship Mode')
    plt.xlabel('Total Sales')
    plt.ylabel('Ship Mode')
    plt.show()

while True:
    print("Pilih fungsi yang ingin dijalankan:")
    print("1. Fungsi Satu")
    print("2. Fungsi Dua")
    print("3. Fungsi Tiga")
    print("4. Fungsi Empat")
    print("5. Fungsi Lima")
    print("0. Keluar")

    choice = int(input("Masukkan pilihan Anda: "))

    if choice == 1:
        function_satu()
    elif choice == 2:
        function_dua()
    elif choice == 3:
        function_tiga()
    elif choice == 4:
        function_empat()
    elif choice == 5:
        function_lima()
    elif choice == 0:
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka antara 1-5 atau 0 untuk keluar.")