from functools import reduce
import pandas as pd
import pprint

class Klasifikasi():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hipotesis = None

    def __init__(self, filename=None, class_attr=None):
        self.data = pd.read_csv(filename, sep=',', header=0)
        self.class_attr = class_attr

    def hitung_priori(self):
        # Perhitungan Priori
        nilai_kelas = list(set(self.data[self.class_attr]))
        data_kelas = list(self.data[self.class_attr])
        for kelas in nilai_kelas:
            self.priori[kelas] = data_kelas.count(kelas) / float(len(data_kelas))
        print("Nilai Priori: ", self.priori)

    def dapatkan_cp(self, atribut, tipe_atribut, nilai_kelas):
        # Perhitungan Probabilitas Kondisional
        data_atribut = list(self.data[atribut])
        data_kelas = list(self.data[self.class_attr])
        total = 1
        for i in range(len(data_atribut)):
            if data_kelas[i] == nilai_kelas and data_atribut[i] == tipe_atribut:
                total += 1
        return total / float(data_kelas.count(nilai_kelas))

    def hitung_probabilitas_kondisional(self, hipotesis):
        for kelas in self.priori:
            self.cp[kelas] = {}
            for atribut in hipotesis:
                self.cp[kelas].update({hipotesis[atribut]: self.dapatkan_cp(atribut, hipotesis[atribut], kelas)})
        print("\nProbabilitas Kondisional yang Dihasilkan:\n")
        pprint.pprint(self.cp)

    def klasifikasikan(self):
        # Klasifikasi dan Prediksi
        print("Hasil:")
        for kelas in self.cp:
            print(kelas, " ==> ", reduce(lambda x, y: x * y, self.cp[kelas].values()) * self.priori[kelas])

if __name__ == "__main__":
    klasifikasi = Klasifikasi(filename="kepuasan_dataset.csv", class_attr="Kelas")
    klasifikasi.hitung_priori()
    klasifikasi.hipotesis = {"Responsiveness": 'Tinggi', "Ketersediaan Sumber Daya": 'Rendah',
                             "Kualitas Pengajaran": 'Sedang', "Bimbingan dan Dukungan Akademis": 'Rendah'}

    klasifikasi.hitung_probabilitas_kondisional(klasifikasi.hipotesis)
    klasifikasi.klasifikasikan()
