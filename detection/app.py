from flask import Flask, request, jsonify, render_template
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_coordinates', methods=['POST'])
def receive_coordinates():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Lakukan pemrosesan data sesuai kebutuhan di sini

    message = 'Data berhasil diterima: Latitude {}, Longitude {}'.format(latitude, longitude)
    print(message)  # Cetak pesan ke terminal

    return jsonify({'message': 'Data berhasil diterima dan diproses'})

if __name__ == '__main__':
    app.run()
    webbrowser.open_new_tab('http://127.0.0.1:5000')
