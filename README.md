# Amazon TR Ürün Fiyat Takip Projesi

## Proje Hakkında

Bu proje, Amazon Türkiye'deki ürünlerin fiyatlarını günlük olarak takip etmek
ve  MS SQL Server veritabanında saklamak için geliştirilmiştir. 
Projede `pyodbc`, `requests`, `matplotlib` ve `BeautifulSoup` gibi Python kütüphaneleri kullanılmıştır. 
Toplanan verileri veri tabanına kaydedip üzerinde görselleştirme ve analiz işlemleri gerçekleştirilebilir.

**Veritabanı ve Sunucu Bilgilerini Güncelleyin:**

   Kullandığınız MS SQL Server veritabanı ve sunucu bilgilerini aşağıdaki kod bloklarında belirtilen yerlere girin:

   - `your_server_name` kısmına kendi sunucu adınızı girin.
   - `your_database_name` kısmına kendi veritabanı isminizi girin.
   - `your_user_agent` kısmına kendi User-Agent bilginizi girin.
   - `your_product_url` kısmına kendi çekmek istediğiniz Amazon TR URL bilgisini girin.
## Kullanılan Teknolojiler ve Araçlar

- **Veritabanı:** Microsoft SQL Server
- **Kimlik Doğrulama:** Windows Authentication
- **Python Kütüphaneleri:**
  - `pyodbc` (Veritabanı bağlantısı için)
  - `requests` (HTTP istekleri için)
  - `BeautifulSoup` (Web scraping için)
  - `datetime` (Tarih ve saat işlemleri için)
  - `matplotlib` (Veri görselleştirme için)

## Gerekli Kütüphanelerin Yüklenmesi

Projenin çalışması için gerekli Python kütüphanelerini terminale aşağıdaki gibi yazarak komutla yükleyebilirsiniz:

```bash
pip install pyodbc requests beautifulsoup4 matplotlib


