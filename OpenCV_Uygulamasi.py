from tkinter import* 
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image  
import cv2
import numpy 

window =Tk 
kernel1 = ''
kernel2 = ''
uyari = ""
resized= numpy.ndarray 

def gorselsec ():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    url = str(window.filename)
    try:
        img = cv2.imread(url, cv2.IMREAD_UNCHANGED)

        width = 500
        height = 500 
        size = (width, height)
        global resized
        resized = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
        cv2.imshow("Orijinal Gorsel", resized)
    except:
        print("Hata Oluştu. Farklı bir görsel seçin.")
    
def agirlikOrtalama():
    kb1=int(kernel1.get().strip())
    kb2=int(kernel2.get().strip())
    global resized
    try:
        filtreleme = cv2.blur(resized,(kb1, kb2))
        cv2.imshow("Agirlik Ortalama Filtresi",filtreleme)
    except:
        print("Farklı Bir Kernel Değeri Giriniz.")

def Gaussian():
    kb1=int(kernel1.get().strip())
    kb2=int(kernel2.get().strip()) 
    global resized
    try:
        gauss = cv2.GaussianBlur(resized,(kb1, kb2),0)
        cv2.imshow("Gaussian Filtresi",gauss)
    except:
        print("Farklı Bir Kernel Değeri Giriniz.")

def Medyan():
    kb1=int(kernel1.get().strip())
    global resized
    try:
        medianfiltre = cv2.medianBlur(resized,kb1)
        cv2.imshow("Medyan Filtresi",medianfiltre)
    except:
        print("Farklı Bir Kernel Değeri Giriniz.")

def ikiTarafli (): 
    kb1=int(kernel1.get().strip())
    global resized 
    try:
        tarafli= cv2.bilateralFilter(resized, kb1, 100,100)
        cv2.imshow("Iki Tarafli Filtre",tarafli)
    except:
        print("Farklı Bir Kernel Değeri Giriniz.")


def girissayfasi():  ##kulanıcın karışalacağı ana pencere ekran 
    global window
    window=Tk(className=' PYTHON UYGULAMASI') ##pencere başlığı
    window.geometry("1000x480") ##boyutu
    window.configure(bg='#8b658b')##pencere rengi 
    window.resizable(width=FALSE, height=FALSE) ##pecrenin boyutu kullanıcı tarafından değiştirilemez
    Label(window, text="FİLTRE DENEME UYGULAMASI",bg='white',font=("Courier", 20) ).place(x=300, y=10) 
  
    #görsel seçme butonu
    gorselSecBtn= Button(text = "Resim Seç", command=gorselsec, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white',width=33,height=4)
    gorselSecBtn.place(x=80, y=80)
    uyari2 = Label(window, text="Gorsel Seçimi\nYapmadan Filtre Uygulanamaz!",bg='#8b658b',font=("Courier", 9)).place(x=90, y= 155) 

    #kernel seçimi
    kernelB = Label(window, text="Kernel Boyutunu Giriniz",bg='#f8f8ff',font=("Courier", 12)).place(x=80, y= 200) 
    uyari = Label(window, text="KERNEL BOYUTUNU BOŞ BIRAKMAYINIZ!",bg='#8b658b',font=("Courier", 9)).place(x=80, y= 265) 
    global kernel1
    kernel1= Entry(window,font=("Courier", 14))
    kernel1.place(x=120, y=235,width=60) 
    global kernel2
    kernel2= Entry(window,font=("Courier", 14))
    kernel2.place(x=190, y=235,width=60) 

    #yumuşatma filtreleri seçimi
    gorselSecBtn= Button(text = "Ağrılık Ortalama Filtreleme", command=agirlikOrtalama, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white',width=20,height=4)
    gorselSecBtn.place(x=450, y=80)

    gorselSecBtn= Button(text = "Gaussian Filtreleme", command=Gaussian, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white',width=20,height=4)
    gorselSecBtn.place(x=690, y=80)

    gorselSecBtn= Button(text = "Medyan Filtreleme", command=Medyan, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white',width=20,height=4)
    gorselSecBtn.place(x=450, y=200)

    gorselSecBtn= Button(text = "İki Taraflı Filtreleme", command=ikiTarafli, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white',width=20,height=4)
    gorselSecBtn.place(x=690, y=200)

    uyari1 = Label(window, text="Uygulamak İstediğiniz \n Filtreye Tıklayıp Görüntüleyin.",bg='#f8f8ff',font=("Courier", 11)).place(x=480, y=320) ##kullanıcıdan kernel alma label
    
    ##çıkış butonu 
    kapatbtn= Button(text = "KAPAT", command=window.quit, bg='#cdc1c5',activebackground = '#8b0a50', activeforeground = 'white', width=33,height=2)
    kapatbtn.place(x=80, y=320) 

    window.mainloop()

girissayfasi()