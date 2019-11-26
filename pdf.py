import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def img2pdf(filepath):
    
    name = filepath + '.pdf'
    raw_file = os.listdir(filepath)
    
    ''' get img file'''
    img_list = []
    for i in raw_file:
        end = i.split('.')[-1]
        if end in ['jpg','jpeg','png']:
            img_list.append(filepath+'/'+i)
    img_list.sort()

    ''' write to file '''
    x = canvas.Canvas(name)
    for img in img_list:
        img_r = ImageReader(img)
        img_size = img_r.getSize()
        x.setPageSize(img_size)
        x.drawImage(img,0,0)
        x.showPage()
    
    x.save()
    return True

if __name__ == '__main__':
        
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print('loading...')
        if img2pdf(path):
            print('{} ok.'.format(path))
    else:
        print('Use python {} dir'.format(sys.argv[0]))



