# 1. Variabel konstanta bertipe Tuple
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)  # (Suhu Max, Kelembaban Min)

# 2. Fungsi untuk menghitung rata-rata dari data yang sudah di-slice
def hitung_tren(data_slice):
    if not data_slice:
        return 0.0, 0.0
    
    total_suhu = 0
    total_lembab = 0
    
    for suhu, kelembaban in data_slice:
        total_suhu += suhu
        total_lembab += kelembaban
        
    rata_suhu = total_suhu / len(data_slice)
    rata_lembab = total_lembab / len(data_slice)
    
    return rata_suhu, rata_lembab

# 3. Fungsi untuk mengevaluasi status irigasi berdasarkan ambang batas
def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    suhu_max = tuple_kritis[0]
    lembab_min = tuple_kritis[1]
    
    if rata_suhu > suhu_max or rata_lembab < lembar_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."
