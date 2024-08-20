import pyodbc
import matplotlib.pyplot as plt
from datetime import datetime

conn = pyodbc.connect(        # SQL Server bağlantısı
    'DRIVER={SQL Server};'
    r'SERVER=your_server_name;'  # Sunucu adınızı buraya girin
    'DATABASE=your_database_name;'  # Veritabanı isminizi buraya girin
    'Trusted_Connection=yes;'  # # Eğer SQL Server Authentication kullanıyorsanız bu satırı değiştirin
    # 'UID=your_username;'  # SQL Server kullanıcı adınızı buraya girin (gerekliyse)
    # 'PWD=your_password;'  # SQL Server şifrenizi buraya girin (gerekliyse)
)
# Eğer Windows Authentication kullanıyorsanız yukarıdaki yorum satırlarını geçin

cursor = conn.cursor()  # SQL sorgusu ile veriyi çekme
cursor.execute("SELECT product_name, price, date FROM product_prices")

product_names = [] # Veriyi saklamak için listeler oluşturma
prices = []
dates = []

for row in cursor.fetchall():              # Veriyi çekme ve listelere ekleme
    product_names.append(row[0])
    prices.append(row[1])
    dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

conn.close()

unique_products = set(product_names) # Farklı ürünler için farklı çizgiler çizme
plt.figure(figsize=(10,6))

for product in unique_products:
    product_dates = [dates[i] for i in range(len(dates)) if product_names[i] == product]
    product_prices = [prices[i] for i in range(len(prices)) if product_names[i] == product]
    plt.plot(product_dates, product_prices, label=product)

plt.xlabel('Tarih')
plt.ylabel('Fiyat (TL)')
plt.title('Ürünlere Göre Zaman İçinde Fiyat Değişimleri')
plt.legend(title="Ürünler")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
