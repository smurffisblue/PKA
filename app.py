from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

pesan_default = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Bermain puzzle",
    "Minum coklat panas",
    "Bermain dengan Garry",
    "Uang uang uang uang",
    "Menangkap ubur-ubur",
    "Beri aku resep rahasia",
    "Aku siap aku siap",
    "Ini adalah hari kebalikan"
]

@app.route('/puja_kerang_ajaib', methods=['GET', 'POST'])
def puja_kerang_ajaib():
    if request.method == 'GET':
        nama = request.args.get('nama')
        pesan = f"{nama}, {random.choice(pesan_default)}" if nama else random.choice(pesan_default)
        return jsonify({"pesan": pesan})

    elif request.method == 'POST':
        try:
            data = request.get_json()  # Mengambil data JSON dari body request

            if data and 'nama' in data:
                nama = data['nama']
                pesan = f"Selamat datang, {nama}, Anda berhasil masuk ke Puja Kerang Ajaib"
                return jsonify({"pesan": pesan})
            else:
                return jsonify({"error": "Parameter 'nama' tidak ditemukan dalam data JSON"}), 400
        except Exception as e:
            return jsonify({"error": f"Terjadi kesalahan: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)