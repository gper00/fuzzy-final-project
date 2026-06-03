import numpy as np
from fuzzy.inference import evaluate_rules, aggregate
from fuzzy.defuzzification import centroid

def hitung_penghematan(daya, waktu, prioritas):
    """
    Fungsi utama untuk menghitung rekomendasi penghematan energi.
    Returns: 
        - crisp_output: Nilai persentase penghematan (0-100)
        - keputusan: String aksi konkret
        - aggregated_output: Array mu(x) untuk visualisasi
        - x_range: Array x untuk visualisasi
    """
    # 1. Definisi range output
    x_range = np.linspace(0, 100, 500)
    
    # 2. Evaluasi Rules
    rules = evaluate_rules(daya, waktu, prioritas)
    
    # 3. Agregasi
    aggregated_output = aggregate(rules, x_range)
    
    # 4. Defuzzifikasi
    crisp_output = centroid(x_range, aggregated_output)
    
    # 5. Terjemahkan ke Keputusan
    if crisp_output <= 30:
        keputusan = "✅ Konsumsi normal, tidak perlu tindakan"
    elif crisp_output <= 60:
        keputusan = "⚠️ Kurangi penggunaan perangkat prioritas rendah"
    else:
        keputusan = "🔴 Matikan segera perangkat non-esensial"
        
    return crisp_output, keputusan, aggregated_output, x_range
