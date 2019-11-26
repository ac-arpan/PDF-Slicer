from flask import *
import pdfcropper
from werkzeug import secure_filename
import os

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = "C:\\Users\\DELL\\Desktop\\WEB_DEV\\Pdf Cropper"
@app.route('/')
def upload():
        
    return render_template('file_upload.html')

@app.route('/success',methods=["GET","POST"])
def success():
    global start
    global end
    global f
        
    start = int(request.form['start'])
    end = int(request.form['end'])
    f = request.files['file']
    
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        
    global file 
    file = f.filename
        
    return render_template('success.html',start = start,end=end,name=file)


@app.route('/convert',methods=["GET","POST"])
def cropper():
    
    pdfcropper.cropper(start,end,file)
    
    return render_template('download.html')

@app.route('/download')
def download():
    filename = file.split(".")[0] + " cropped.pdf"
    return send_file(filename,as_attachment = True)
    
    
if __name__ == '__main__' :
    app.run(host='127.0.0.1',port=8000)