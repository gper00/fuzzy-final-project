import numpy as np

def trimf(x, abc):
    """Triangular membership function with zero division handling."""
    assert len(abc) == 3, 'abc parameter must have 3 elements'
    a, b, c = abc
    
    # Left slope
    if a == b:
        term1 = np.where(x >= a, 1.0, 0.0)
    else:
        term1 = (x - a) / (b - a)
        
    # Right slope
    if b == c:
        term2 = np.where(x <= b, 1.0, 0.0)
    else:
        term2 = (c - x) / (c - b)
        
    return np.maximum(0, np.minimum(term1, term2))

def trapmf(x, abcd):
    """Trapezoidal membership function with zero division handling."""
    assert len(abcd) == 4, 'abcd parameter must have 4 elements'
    a, b, c, d = abcd
    
    # Left slope
    if a == b:
        term1 = np.where(x >= a, 1.0, 0.0)
    else:
        term1 = (x - a) / (b - a)
        
    # Right slope
    if c == d:
        term2 = np.where(x <= c, 1.0, 0.0)
    else:
        term2 = (d - x) / (d - c)
        
    return np.maximum(0, np.minimum(np.minimum(term1, 1.0), term2))

# --- Daya Aktif (0 - 2200 W) ---
def m_daya_rendah(x):
    return trapmf(x, [0, 0, 400, 800])

def m_daya_sedang(x):
    return trimf(x, [600, 1100, 1600])

def m_daya_tinggi(x):
    return trapmf(x, [1400, 2000, 2200, 2200])

# --- Jam Operasional (0 - 24 Jam) ---
# Optimized overlaps to remove dead zones at 6:00, 17:00, and 22:00
def m_waktu_off_peak(x):
    # Transition: Off-peak (0-8) and (20-24)
    p1 = trapmf(x, [0, 0, 5, 8])
    p2 = trapmf(x, [20, 22, 24, 24])
    return np.maximum(p1, p2)

def m_waktu_normal(x):
    # Transition: 5 to 19 (Peak at 12)
    return trimf(x, [5, 12, 19])

def m_waktu_peak(x):
    # Transition: 17 to 22 (Peak at 19.5)
    return trimf(x, [17, 19.5, 22])

# --- Prioritas Perangkat (1 - 10) ---
def m_prioritas_rendah(x):
    return trapmf(x, [1, 1, 2.5, 4])

def m_prioritas_sedang(x):
    return trimf(x, [3, 5, 7])

def m_prioritas_tinggi(x):
    return trapmf(x, [6, 8.5, 10, 10])

# --- Rekomendasi Penghematan (0 - 100 %) ---
def m_hemat_kecil(x):
    return trapmf(x, [0, 0, 15, 30])

def m_hemat_sedang(x):
    return trimf(x, [20, 40, 60])

def m_hemat_besar(x):
    return trapmf(x, [50, 75, 100, 100])
