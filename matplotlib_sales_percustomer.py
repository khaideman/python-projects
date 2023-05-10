import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file Excel
df = pd.read_csv('transaction_dataset.csv')

# Menghitung total penjualan per kota dan customer name
grouped = df.groupby(['City', 'Customer Name'])['Sales'].sum().reset_index()

# Mencari customer name dengan total penjualan terbanyak per kota
idx = grouped.groupby(['City'])['Sales'].transform(max) == grouped['Sales']
result = grouped[idx].reset_index(drop=True)

# Mengurutkan data berdasarkan kolom 'Sales' dari nilai terbesar ke terkecil
result = result.sort_values(by=['Sales'], ascending=False)

# Menampilkan hasil
print(result[['City', 'Customer Name', 'Sales']])

# Menampilkan grafik batang horizontal
plt.barh(result['City'], result['Sales'])
plt.title('Total Sales per City by Top Customer Name')
plt.xlabel('Total Sales')
plt.ylabel('City')
plt.show()
