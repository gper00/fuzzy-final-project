import numpy as np

def centroid(x_range, aggregated_output):
    """
    Hitung nilai crisp menggunakan metode Centroid (Center of Area).
    CoA = sum(x * mu(x)) / sum(mu(x))
    """
    sum_mu = np.sum(aggregated_output)
    if sum_mu == 0:
        return 0 # Default jika tidak ada rule yang aktif
    
    return np.sum(x_range * aggregated_output) / sum_mu
