# Mengimport fungsi dan konstanta dari modul_sensor
import modul_sensor

# 1. Struktur Data Utama
log_kebun = []

# 2. Fungsi Validasi Input menggunakan try-except dan while True
def input_sensor():
    while True:
        try:
            suhu = float(input("Masukkan Suhu Udara (0-100 C): "))
            kelembaban = float(input("Masukkan Kelembaban Tanah (0-100 %): "))
            
            # Validasi rentang rasional
            if 0 <= suhu <= 100 and 0 <= kelembaban <= 100:
                return (suhu, kelembaban)
            else:
                print("Input di luar rentang rasional! Silakan coba lagi (0-100).\n")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka saja.\n")

# 3. Menu Interaktif
while True:
    print(f"\n=== SISTEM MONITORING IOT - {modul_sensor.LOKASI[0]} ===")
    print("[1] Rekam Data")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        print("\n--- Menu 1: Rekam Data ---")
        data_baru = input_sensor()
        log_kebun.append(data_baru)
        print("Data berhasil direkam!")
        
    elif pilihan == "2":
        print("\n--- Menu 2: Analisis Tren (3 Terakhir) ---")
        if not log_kebun:
            print("Belum ada data yang direkam. Silakan pilih menu 1 terlebih dahulu.")
            continue
            
        # Menggunakan Slicing untuk mengambil maksimal 3 data terakhir
        data_slice = log_kebun[-3:]
        
        # Cetak ketiga data tersebut menggunakan perulangan for
        print("3 Data Terakhir:")
        for idx, data in enumerate(data_slice, 1):
            print(f"   Data ke-{idx} -> Suhu: {data[0]} C, Kelembaban: {data[1]}%")
            
        # Panggil fungsi dari modul untuk menghitung rata-rata dan status
        rata_s, rata_l = modul_sensor.hitung_tren(data_slice)
        status = modul_sensor.evaluasi_irigasi(rata_s, rata_l, modul_sensor.AMBANG_KRITIS)
        
        print(f"\nRata-rata Suhu       : {rata_s:.2f} C")
        print(f"Rata-rata Kelembaban : {rata_l:.2f}%")
        print(f"Status Sistem        : {status}")
        
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan sistem ini. Program selesai.")
        break
    else:
        print("Pilihan menu tidak tersedia! Silakan ketik angka 1, 2, atau 3.")
