from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf = PdfFileReader(open(file,'rb'))  # PdfFileReader object
    outPdf = PdfFileWriter()                     # PdfFileWriter object
    
    ostream = open(file.split(".")[0] + "cropped" + ".pdf",'wb')  #opening one file to write the extracted pdf
    
    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))
        
        outPdf.write(ostream)
        
        start += 1
        
    ostream.close()
    
#cropper(1,3,"sample.pdf")
    