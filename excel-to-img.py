import os
import pandas as pd
import requests
from datetime import date
import unicodedata
import re

# Excel dosyasını oku
df = pd.read_excel("rich-urunler-20-06-2023.xlsx")

# Hedef klasörü oluştur (varsa üzerine yazmaz)
today = date.today()
editedDay = today.strftime("%d.%m.%Y")
folder = "rich-urun-resimleri-{}".format(editedDay)
if not os.path.exists(folder):
    os.makedirs(folder)

# Resim sütunlarının adlarını belirle
columnOfImg = ["resim_1", "resim_2", "resim_3", "resim_4", "resim_5", "resim_6", "resim_7"]

# Geçersiz karakterleri kaldıran ve Türkçe karakterleri düzenleyen işlev
def duzelt(element):
    element = re.sub(r'[<>:"/\\|?*]', '', element)  # Geçersiz karakterleri kaldır
    element = ''.join(c for c in unicodedata.normalize('NFD', element) if unicodedata.category(c) != 'Mn')  # Türkçe karakterleri düzenle
    return element
    
# Her bir resim sütunu için işlem yap
for col in columnOfImg:
    # Her bir hücredeki URL ve ürün adını kontrol et
    for index, row in df.iterrows():
        url = row[col]
        productName = row["urun_adi"]
        if pd.notnull(url) and pd.notnull(productName):  # URL ve ürün adı boş değilse
            response = requests.get(url)
            if response.status_code == 200:  # İstek başarılı ise
                # Resmi indir ve dosyaya kaydet
                folderName = f"{folder}/{duzelt(productName)}_{col}_{index}.jpg"
                with open(folderName, "wb") as file:
                    file.write(response.content)
                print(f"Resim {folderName} indirildi.")
            else:
                print(f"Hata: {col}_{index} resmi indirilemedi.")

print("Resimler indirildi...")
