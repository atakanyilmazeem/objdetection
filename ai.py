from keras.models import load_model
from PIL import Image, ImageOps 
import numpy as np # kutuphaneler dahil ediliyor

def imagine(path): # path adında deger alan imagine fonksiyonu tanımlanıyor.
    np.set_printoptions(suppress=True) 
    model = load_model("keras_Model.h5", compile=False) # egittimiz yapay zeka modelini dahil ediyoruz
    class_names = open("labels.txt", "r").readlines() # yapay zekanın verecegi cıktıgıyı etiketlemek icin metin dosyası kullanıyoruz.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(path).convert("RGB") # fonksiyona verilen path degerinde yer alan fotografi aciyor
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  # fotograf boyutlandırması
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1 
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction) #fotograf uzerinde bir takim islemler 
    class_name = class_names[index] # sınıf adını getir
    confidence_score = prediction[0][index] #tahmin oranını getir
    print("Class:", class_name[2:], end="")
    print("Score:", confidence_score) # tahmini ve sınıfı yazdır

    return class_name[2:],confidence_score #tahmini ve sınıfı geri gonder