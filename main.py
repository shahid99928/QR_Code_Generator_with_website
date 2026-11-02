from flask import Flask,render_template,request 
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def generateQR():
    data = request.form.get('link', '').strip()
    if not data:
        return render_template(
            'index.html',
            error='Please enter a link to generate a QR code: ',
            link=data,
        ), 400

    memory = BytesIO()
    image = qrcode.make(data)
    image.save(memory)
    memory.seek(0)
    
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html', data=base64_img, link=data)
if __name__ == '__main__':
    app.run(debug=True)