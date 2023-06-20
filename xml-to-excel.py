from datetime import date
import xml.etree.ElementTree as ET
import pandas as pd

# XML dosyasını analiz etmek için fonksiyon
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    products = []

    for product_elem in root.findall('urun'):
        product = {}
        product['urun_adi'] = product_elem.find('urun_adi').text.strip()

        resimler_elem = product_elem.find('resimler')
        resim_urls = resimler_elem.findall('*')
        for i, resim_url in enumerate(resim_urls, start=1):
            product[f'resim_{i}'] = resim_url.text.strip()

        products.append(product)

    return products

#excel dosyasını adlandırmak için 
today=date.today()
editedDay = today.strftime("%d-%m-%Y")

# XML dosyasının adını ve çıktı Excel dosyasının adını belirtin
xml_file = 'rich_xml-18.06.2023.xml'
output_excel = 'rich-urunler-{}.xlsx'.format(editedDay)

# XML dosyasını analiz et ve verileri al
products = parse_xml(xml_file)

# Verileri Excel dosyasına yaz
df = pd.DataFrame(products)
df.to_excel(output_excel, index=False)
print("İşlem tamamlandı")
