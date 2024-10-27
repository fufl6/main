#создай тут фоторедактор Easy Editor!
from random import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
app = QApplication([])
main_win = QWidget()
main_win.resize(700,400)
main_win.setWindowTitle('умни не замитка')
layout_main = QVBoxLayout
text = QTextEdit()
list1 = QListWidget()
list2 = QListWidget()
push1 = QPushButton('Лево')
push2 = QPushButton('Право')
push3 = QPushButton('Зеркало')
push4 = QPushButton('Резкость')
push5 = QPushButton('Ч/Б')
push6 = QPushButton('Пипка')
label1 = QLabel('пиктуре')
text = QListWidget()
line1 = QHBoxLayout()
line1.addWidget(push1)
line1.addWidget(push2)
line1.addWidget(push3)
line1.addWidget(push4)
line1.addWidget(push5)
line2 = QVBoxLayout()
line2.addWidget(push6)
line2.addWidget(text)
line3 = QVBoxLayout()
line3.addWidget(label1)
line3.addLayout(line1)
line4 = QHBoxLayout()
line4.addLayout(line2)
line4.addLayout(line3)
workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = list()
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def ShowFilenamesList():
    chooseWorkdir()
    extensions = ['png','jpg']
    filenames = os.listdir(workdir)
    result = filter(filenames,extensions)
    text.clear()
    for hohl in result:
        text.addItem(hohl)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None        
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        label1.hide()
        pixmapimage = QPixmap(path)
        w,h = label1.width(), label1.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        label1.setPixmap(pixmapimage)
        label1.show()
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path or os.path.isdir(path))):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_blr(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_mr(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_l(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_ri(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)


workimage = ImageProcessor()

def showChoosenImage():
    if text.currentRow() >= 0:
        filename = text.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)
text.currentRowChanged.connect(showChoosenImage)
push4.clicked.connect(workimage.do_blr)
push1.clicked.connect(workimage.do_l)
push2.clicked.connect(workimage.do_ri)
push3.clicked.connect(workimage.do_mr)
push5.clicked.connect(workimage.do_bw)
push6.clicked.connect(ShowFilenamesList)



main_win.setLayout(line4)
main_win.show()
app.exec()

