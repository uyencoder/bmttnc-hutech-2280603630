from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted_text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted_text: {decrypted_text}"

#VIGENERE
@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        action = request.form['action']
        
        if action == 'encrypt':
            result = VigenereCipher(text, key, decrypt=False)
        elif action == 'decrypt':
            result = VigenereCipher(text, key, decrypt=True)
    
    return render_template('vigenere.html', result=result)



#main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)