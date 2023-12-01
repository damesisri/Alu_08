#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Greedy Algorithm
def greedy_algorithm(distance_matrix, start_node):
    num_nodes = len(distance_matrix)
    visited_nodes = set()
    current_node = start_node
    path = [current_node]

    while len(visited_nodes) < num_nodes:
        next_node = min(
            (node for node in range(num_nodes) if node not in visited_nodes),
            key=lambda x: distance_matrix[current_node][x]
        )
        visited_nodes.add(next_node)
        path.append(next_node)
        current_node = next_node

    return path


# Matriks jarak
distance_matrix = [
    [0, 1.2, 1, 1.2],
    [1.2, 0, 0.6, 1.4],
    [1, 0.6, 0, 1.2],
    [1.2, 1.5, 1.2, 0]
]

# Daftar tempat
places = [
    "RS HKBP Balige",
    "Pelabuhan Penyebrangan Balige",
    "Gereja Katolik Balige",
    "Telkom Balige"
]

# Jalur antar tempat
routes = {
    "RS HKBP Balige": {
        "Pelabuhan Penyebrangan Balige": ["Arah Utara di Jl. Gereja menuju Jl. GHM. Siahaan", "Belok kiri ke Jl.Lintas Sumatera/Jl. Siborong-borong", "Dari Bundaran, ambil keluar ke-2 menuju Jl. D.I Panjaitan", "Teruskan ke Jl. Siliwangi", "Belok kanan ke Jl. Bukit Barisan"],
        "Gereja Katolik Balige": ["Jl. Gereja, Jl. Lintas Sumatera -> Jl. Patuan Nagari", "Jl. Gereja -> Jl. Lintas Sumatera"],
        "Telkom Balige": ["Ambil arah utara di Jl. Gereja menuju Jl. GHM. Siahaan", "Belok kanan ke Jl. GHM. Siahaan", "Belok kiri"]
    },
    "Pelabuhan Penyebrangan Balige": {
        "RS HKBP Balige": ["Arah Utara di Jl. Gereja menuju Jl. GHM. Siahaan", "Belok kiri ke Jl.Lintas Sumatera/Jl. Siborong-borong", "Dari Bundaran, ambil keluar ke-2 menuju Jl. D.I Panjaitan", "Teruskan ke Jl. Siliwangi", "Belok kanan ke Jl. Bukit Barisan"],
        "Gereja Katolik Balige": ["Ambil arah selatan di Jl. Bukit Barisan menuju Jl. Siliwangi", "Belok kanan ke Jl. Siliwangi", "Belok kiri ke Jl. Dr. T.D Pardede", "Belok kanan ke Jl. Lintas Sumatera/ Jl. Patuan Nagari/ Jl. Siborong-borong-Parapat/ Jl. Sm Raja"],
        "Telkom Balige": ["Ambil arah selatan di Jl. Bukit Barisan menuju Jl. Siliwangi", "Belok kiri ke Jl.Siliwangi", " Teruskan ke Jl. D.I Panjaitan", "Di bundaran, ambil jalan keluar pertama menuju Jl. Lintas Sumatera/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Belok kanan ke Jl. Gereja", "Belok kiri ke Jl. GHM. Siahaan"]
    },
    "Gereja Katolik Balige": {
        "RS HKBP Balige": ["Jl. Gereja, Jl. Lintas Sumatera -> Jl. Patuan Nagari", "Jl. Gereja -> Jl. Lintas Sumatera"],
        "Pelabuhan Penyebrangan Balige": ["Ambil arah selatan di Jl. Bukit Barisan menuju Jl. Siliwangi", "Belok kanan ke Jl. Siliwangi", "Belok kiri ke Jl. Dr. T.D Pardede", "Belok kanan ke Jl. Lintas Sumatera/ Jl. Patuan Nagari/ Jl. Siborong-borong-Parapat/ Jl. Sm Raja"],
        "Telkom Balige": ["Ambil arah barat daya menuju Jl. GHM. Siahaan", "Belok kanan ke Jl. Gereja", "Belok kiri ke Jl. Lintas Sumatera/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Di bundaran, ambil jalan keluar pertama menuju Jl. Lintas Sumatera/Jl. Patuan Nagari/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Belok kiri ke Jl. Tnadang Buhit"]
    },
    "Telkom Balige": {
        "RS HKBP Balige": ["Ambil arah utara di Jl. Gereja menuju Jl. GHM. Siahaan", "Belok kanan ke Jl. GHM. Siahaan", "Belok kiri"],
        "Pelabuhan Penyebrangan Balige": ["Ambil arah selatan di Jl. Bukit Barisan menuju Jl. Siliwangi", "Belok kiri ke Jl.Siliwangi", " Teruskan ke Jl. D.I Panjaitan", "Di bundaran, ambil jalan keluar pertama menuju Jl. Lintas Sumatera/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Belok kanan ke Jl. Gereja", "Belok kiri ke Jl. GHM. Siahaan"],
        "Gereja Katolik Balige": ["Ambil arah barat daya menuju Jl. GHM. Siahaan", "Belok kanan ke Jl. Gereja", "Belok kiri ke Jl. Lintas Sumatera/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Di bundaran, ambil jalan keluar pertama menuju Jl. Lintas Sumatera/Jl. Patuan Nagari/Jl. Siborong Borong - Parapat/Jl. Sm Raja", "Belok kiri ke Jl. Tnadang Buhit"]
    }
}

# Menambahkan jarak khusus ke matriks jarak (misalnya, RS HKBP Balige ke Telkom Balige)
special_distance_RS_to_Telkom = 1.5
special_distance_Telkom_to_RS = 1.2
RS_index = places.index("RS HKBP Balige")
Telkom_index = places.index("Telkom Balige")
distance_matrix[RS_index][Telkom_index] = special_distance_RS_to_Telkom
distance_matrix[Telkom_index][RS_index] = special_distance_Telkom_to_RS

# Menentukan jalur awal (misalnya, RS HKBP Balige ke Pelabuhan Penyebrangan Balige)
start_place = "RS HKBP Balige"
end_place = "Pelabuhan Penyebrangan Balige"
start_index = places.index(start_place)
end_index = places.index(end_place)

result_path = greedy_algorithm(distance_matrix, start_index)
print("Jalur terpendek:", result_path)

# Menemukan jalur spesifik antara tempat awal dan akhir
route_description = routes[start_place][end_place]
print("Rute terpendek:", route_description)


# In[ ]:




