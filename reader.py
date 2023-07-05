"""
Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

 <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
 <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
<zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.

Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".

Przykład działania:
python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
Z pliku in.csv:
drzwi,3,7,0
kanapka,12,5,1
pedzel,22,34,5
plakat,czerwony,8,kij
Ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0
"""
import csv
import sys


def modify_csv(input_file, output_file, changes):
    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    for change in changes:
        change_values = change.split(',')
        if len(change_values) == 3:
            try:
                column = int(change_values[0])
                row = int(change_values[1])
                value = change_values[2]
                if row < len(rows) and column < len(rows[row]):
                    rows[row][column] = value
                else:
                    print(f"błąd {change} - argumenty poza skalą.")
            except ValueError:
                print(f"błąd {change} - argumenty poza skalą.")

    print(f"From file {input_file}:")
    for row in rows:
        print(','.join(row))

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


if len(sys.argv) < 4:
    print("python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]

modify_csv(input_file, output_file, changes)
