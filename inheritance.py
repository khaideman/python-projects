class Kendaraan:
    def Kendaraan_info(self, nama, tahun):
        print('Class kendaraan')
        print('Nama:', nama, 'Tahun:', tahun)

class Mobil:
    def Mobil_info(self, Nama_Mobil, Alamat):
        print('Class mobil')
        print('Nama Mobil:', Nama_Mobil, 'Alamat:', Alamat)

class Sedan(Kendaraan, Mobil):
    def Sedan_info(self, Tipe, Nopol):
        print('Class sedan')
        print('Tipe:', Tipe, 'Nopol:', Nopol)

data_car = Sedan()

data_car.Kendaraan_info('Kalvin Haideman', 2015)
data_car.Mobil_info('Honda Vario 150', 'Sidoarjo')
data_car.Sedan_info(112233, 'W 1121 RR')