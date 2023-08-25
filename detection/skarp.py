import requests

def get_latest_location():
    url = "http://127.0.0.1:5000/receive_coordinates"  # Sesuaikan dengan URL server Flask Anda
    response = requests.post(url)
    data = response.json()

    if 'coords' in data:
        latitude = data['coords']['latitude']
        longitude = data['coords']['longitude']
        return latitude, longitude
    else:
        return None

if __name__ == "__main__":
    location = get_latest_location()
    if location:
        latitude, longitude = location
        print("Latitude:", latitude)
        print("Longitude:", longitude)
    else:
        print("Gagal mendapatkan data lokasi terbaru.")
