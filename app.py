from flask import Flask, render_template, request, jsonify
from encryption_crypto_utils import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/encrypt_page')
def encrypt_page():
    return render_template('encrypt.html')

@app.route('/decrypt_page')
def decrypt_page():
    return render_template('decrypt.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    plaintext = data.get('input')
    key = data.get('key')
    print(f"user input: {plaintext}, key: {key}")
    result = encrypt(plaintext, key)
    return jsonify(result)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.get_json()
    ciphertext = data.get('input')
    key = data.get('key')
    iv = data.get('iv')
    print(f"user input: {ciphertext}, key: {key}, iv: {iv}")
    decrypted = decrypt(ciphertext, key, iv)
    return jsonify({"plaintext": decrypted})
if __name__ == '__main__':
    app.run(debug=True)
