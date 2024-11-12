import pandas as pd

# Przykładowe dane
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": ["a", "b", "c", "d", "e"]})

x_test = pd.DataFrame({"A": [2, 4], "B": ["b", "d"]})

# Pusta lista do przechowywania indeksów wierszy do usunięcia
indexes_to_remove = []

# Sprawdź każdy wiersz w df
for idx, row in df.iterrows():
    # Jeśli wiersz znajduje się w x_test, zapisz jego indeks
    if any((x_test == row).all(axis=1)):
        indexes_to_remove.append(idx)

# Usuń wiersze z df
df_cleaned = df.drop(indexes_to_remove)

print(df_cleaned)
