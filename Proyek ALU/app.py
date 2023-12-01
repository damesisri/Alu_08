from flask import Flask, render_template, request
from greedy_algorithm import greedy_algorithm

app = Flask(__name__)

places = [
    "RS HKBP Balige",
    "Pelabuhan Penyebrangan Balige",
    "Gereja Katolik Balige",
    "Telkom Balige"
]

distance_matrix = [
    [0, 1.2, 1, 1.2],
    [1.2, 0, 0.6, 1.4],
    [1, 0.6, 0, 1.2],
    [1.2, 1.5, 1.2, 0]
]

@app.route('/')
def index():
    return render_template('index.html', places=places)

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    start_index = int(request.form['start_place'])
    end_index = int(request.form['end_place'])

    result_path = greedy_algorithm(distance_matrix, start_index)

    # Hindari rute yang kembali ke titik awal
    if result_path[-1] == start_index:
        result_path.pop()  # Hapus titik terakhir jika sama dengan titik awal

    # Perhitungan total distance dengan jarak terpendek
    total_distance = sum(distance_matrix[result_path[i]][result_path[i + 1]] for i in range(len(result_path) - 1))

    # Tambahkan jarak dari titik terakhir ke titik akhir
    total_distance += distance_matrix[result_path[-1]][end_index]

    route_description = f"Route from {places[start_index]} to {places[end_index]}"

    return render_template('index.html', places=places, result_path=result_path,
                           route_description=route_description, total_distance=total_distance)

if __name__ == '__main__':
    app.run(debug=True)