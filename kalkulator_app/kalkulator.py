class Calculator:
    def __init__(self):
        self.result = 0

    def tambah(self, num1, num2):
        self.result = num1 + num2

    def kurang(self, num1, num2):
        self.result = num1 - num2

    def kali(self, num1, num2):
        self.result = num1 * num2

    def bagi(self, num1, num2):
        if num2 == 0:
            raise ValueError("Tidak dapat melakukan pembagian dengan nol")
        self.result = num1 / num2

    def clear(self):
        self.result = 0


calculator = Calculator()

while True:
    print("Menu calculator:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Bersihkan")
    print("6. Keluar")

    choice = input("Masukkan pilihan (1/2/3/4/5/6): ")

    if choice == '1':
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        calculator.tambah(num1, num2)
        print("Hasil: ", calculator.result)

    elif choice == '2':
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        calculator.kurang(num1, num2)
        print("Hasil: ", calculator.result)

    elif choice == '3':
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        calculator.kali(num1, num2)
        print("Hasil: ", calculator.result)

    elif choice == '4':
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        try:
            calculator.bagi(num1, num2)
            print("Hasil: ", calculator.result)
        except ValueError as e:
            print("Error: ", e)

    elif choice == '5':
        calculator.clear()
        print("Hasil: ", calculator.result)

    elif choice == '6':
        break

    else:
        print("Pilihan tidak valid")