# Proje Adı
xml To excel & excel To img

## Proje Açıklaması

Bir işletme, çalıştığı firma tarafından sağlanan ürünlerle ilgili bilgilere ihtiyaç duyuyor. Ancak firma, bu bilgileri XML formatında sunuyor.

İşletme XML dosyasındaki diğer bilgilerle ilgilenmek zorunda kalmadan, yalnızca ürünlerin resimlerine erişim sağlamak istiyor. 

Bu istekler doğrultusunda bu işletme için oluşturduğum projeyle sadece ürün adı ve resim etiketlerine odaklanarak istenilen verilere erişmeye imkan sunuyor.

## Proje Özellikleri

- XML dosyasını proje klasörüne .xml dosyası olarak kaydeden ve belirtilen etiketlere göre bir Excel dosyası oluşturan `xml-to-excel.py` scripti.
- Excel dosyasında yer alan resim URL'lerini otomatik olarak ziyaret ederek resimleri indiren ve kaydeden `excel-to-img.py` scripti.
- İndirilen resimlerin kaydedildiği klasördeki başarılı ve başarısız indirme işlemlerini konsola yazdıran mekanizma.

## Kurulum

1. Örnek Proje klasörünü bilgisayarınıza indirin.
2. İstediğiniz bir editörde proje klasörünü açtıktan sonra uygulamayı kullanmaya/test etmeye hazırsınız.

## Kullanım

1. XML dosyasını proje klasörüne `.xml` uzantısıyla kaydedin.
2. `xml-to-excel.py` scriptini çalıştırın ve script içindeki "xml_file" adlı değişkene işlenmesini istediğiniz XML dosyasının adını girin.
3. Script, XML dosyasında belirttiğiniz etiketlere göre bir Excel dosyası oluşturacaktır. (Bu işlem sonrasında artık istediğiniz veriler oluşturulan excel tablosuna kaydedilmiş olacak.)
4. `excel-to-img.py` scriptini çalıştırın ve "df" adlı değişkene oluşturulan Excel dosyasının adını girin.
5. Script, Excel dosyasındaki resim URL'lerini otomatik olarak ziyaret ederek resimleri indirecek ve kaydedecektir.
6. İndirilen resimler proje klasöründe belirtilen klasöre kaydedilecek ve indirme durumunu konsola yazdırılacaktır.

