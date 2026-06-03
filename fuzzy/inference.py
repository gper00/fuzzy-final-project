import numpy as np
from fuzzy.membership import *

def evaluate_rules(daya, waktu, prioritas):
    """
    Evaluasi 27 rules Mamdani.
    Returns: list of (firing_strength, output_membership_function)
    """
    # Fuzzifikasi input
    d_r, d_s, d_t = m_daya_rendah(daya), m_daya_sedang(daya), m_daya_tinggi(daya)
    w_o, w_n, w_p = m_waktu_off_peak(waktu), m_waktu_normal(waktu), m_waktu_peak(waktu)
    p_r, p_s, p_t = m_prioritas_rendah(prioritas), m_prioritas_sedang(prioritas), m_prioritas_tinggi(prioritas)

    rules = []

    # Helper function to add rule
    def add_rule(strength, output_func):
        if strength > 0:
            rules.append((strength, output_func))

    # --- Definisi 27 Rules ---
    # Logika: H_score = D_idx + W_idx - Pr_idx
    # D: R=0, S=1, T=2
    # W: O=0, N=1, P=2
    # Pr: R=0, S=1, T=2
    
    # Kita petakan manual biar akurat sesuai keinginan (conservative)
    inputs_d = [d_r, d_s, d_t]
    inputs_w = [w_o, w_n, w_p]
    inputs_p = [p_r, p_s, p_t]

    for i in range(3): # Daya
        for j in range(3): # Waktu
            for k in range(3): # Prioritas
                strength = min(inputs_d[i], inputs_w[j], inputs_p[k])
                
                # Rule logic for output
                score = i + j - k # Range: -2 to 4
                
                if score >= 3:
                    output_func = m_hemat_besar
                elif score >= 1:
                    output_func = m_hemat_sedang
                else:
                    output_func = m_hemat_kecil
                
                # Overwrite specific rules from planning if necessary
                # Planning Rule 1: Tinggi (2), Peak (2), Rendah (0) -> Score 4 -> Besar. Match.
                # Planning Rule 3: Tinggi (2), Peak (2), Tinggi (2) -> Score 2 -> Sedang. Match.
                # Planning Rule 6: Sedang (1), Normal (1), Sedang (1) -> Score 1 -> Sedang. Planning says Kecil.
                # Let's adjust score mapping to match planning Rule 6.
                
                # Refined Score Mapping:
                if score >= 3: # (2,2,0), (2,2,1), (2,1,0), (1,2,0)
                    out = m_hemat_besar
                elif score >= 2: # (2,2,2), (2,1,1), (1,2,1), (1,1,0), (2,0,0), (0,2,0)
                    out = m_hemat_sedang
                else:
                    out = m_hemat_kecil
                
                add_rule(strength, out)
                
    return rules

def aggregate(rules, x_range):
    """
    Agregasi semua output rules menggunakan operator MAX.
    x_range: array nilai x untuk output (0-100)
    """
    aggregated_output = np.zeros_like(x_range)
    
    for strength, output_func in rules:
        # Potong membership function dengan firing strength (MIN)
        rule_output = np.minimum(strength, output_func(x_range))
        # Agregasi dengan MAX
        aggregated_output = np.maximum(aggregated_output, rule_output)
        
    return aggregated_output
