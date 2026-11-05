"""PCA Dimensionality Reducer"""

def mean_center(data):
    n = len(data)
    cols = len(data[0])
    means = [sum(row[j] for row in data) / n for j in range(cols)]
    return [[row[j] - means[j] for j in range(cols)] for row in data]

if __name__ == "__main__":
    print("[RUN] PCA Engine...")
    d = [[10, 20], [12, 22], [14, 24]]
    centered = mean_center(d)
    print(f"[OK] Zero-Centered Data Sample: {centered[0]}")
