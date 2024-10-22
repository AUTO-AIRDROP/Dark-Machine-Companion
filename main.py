import requests
import json
import time

# Fungsi untuk membaca seluruh token dan query dari file auth.txt
def read_auth_data(file_path):
    auth_list = []
    with open(file_path, 'r') as file:
        for line in file:
            token, query = line.strip().split(' ', 1)  # Memisahkan token dan query
            auth_list.append((token, query))  # Menyimpan sebagai tuple
    return auth_list

url = "https://companion.darkmachinegame.com/api/idle-generator/charge"

# Loop yang akan terus berjalan sampai dihentikan dengan Ctrl + C
while True:
    # Membaca semua pasangan token dan query dari auth.txt
    auth_data_list = read_auth_data('auth.txt')
    no=1
    # Loop melalui setiap pasangan token dan query
    for token, query in auth_data_list:
        # Membuat payload untuk setiap token
        payload = json.dumps({
            "token": token
        })

        # Membuat header untuk setiap query
        headers = {
            'authorization': "tma "+ query,
            'Content-Type': 'application/json'
        }

        try:
            # Mengirim permintaan POST ke API
            response = requests.request("POST", url, headers=headers, data=payload)

            # Menampilkan hasil response untuk setiap pasangan
            print(f"No {no} ==> {response.status_code}")
            no +=1
        except Exception as e:
            # Menampilkan error jika terjadi masalah
            print(f"Error for token {token}: {e}")

        # Anda bisa menambahkan delay jika diperlukan untuk menghindari spam terlalu cepat
        time.sleep(2)  # Delay 2 detik antar request (bisa diatur sesuai kebutuhan)

    # Menambahkan delay sebelum mengulang dari awal lagi (opsional)
    print("Selesai memproses semua token, ulangi dari awal...")
    time.sleep(10)  # Delay 10 detik sebelum mengulang (bisa disesuaikan)
