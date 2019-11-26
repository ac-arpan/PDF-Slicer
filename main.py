from flask import *
import pdfcropper

app = Flask(__name__)


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
        
    global file 
    file = f.filename
        
    return render_template('success.html',start = start,end=end,name=file)


@app.route('/convert',methods=["GET","POST"])
def cropper():
    pdfcropper.cropper(start,end,file)
    
    return render_template('download.html')

@app.route('/download')
def download():
    filename = file.split(".")[0] + "cropped.pdf"
    return send_file(filename,as_attachment = True)
    
    
if __name__ == '__main__' :
    app.run(host='127.0.0.1',port=8000)