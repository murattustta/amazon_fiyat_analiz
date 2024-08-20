import pyodbc
import matplotlib.pyplot as plt

# SQL Server bağlantısı
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=your_server_name;'  # Sunucu adınızı buraya girin
    'DATABASE=your_database_name;'  # Veritabanı isminizi buraya girin
    'Trusted_Connection=yes;'  # Eğer SQL Server Authentication kullanıyorsanız bu satırı değiştirin
    # 'UID=your_username;'  # SQL Server kullanıcı adınızı buraya girin (gerekliyse)
    # 'PWD=your_password;'  # SQL Server şifrenizi buraya girin (gerekliyse)
)
# Eğer Windows Authentication kullanıyorsanız yukarıdaki yorum satırlarını geçin

cursor = conn.cursor()
cursor.execute("SELECT product_name, date, price FROM product_prices ORDER BY product_name, date")

data = cursor.fetchall()   # Veriyi listeye çekme

percentage_changes = {}     # Ürün bazında yüzde değişim hesaplama
current_product = None
previous_price = None

for row in data:
    product_name, date, price = row

    if product_name != current_product:
        current_product = product_name
        previous_price = None
        percentage_changes[current_product] = {'dates': [], 'percentage_changes': []}

    if previous_price is not None:
        percentage_change = ((price - previous_price) / previous_price) * 100
        percentage_changes[current_product]['dates'].append(date)
        percentage_changes[current_product]['percentage_changes'].append(percentage_change)

    previous_price = price

conn.close()

plt.figure(figsize=(12, 8))  # Yüzdesel değişimleri çizgi grafiği ile görselleştirme

for product_name, values in percentage_changes.items():
    plt.plot(values['dates'], values['percentage_changes'], marker='o', label=product_name)

plt.xlabel('Tarih')
plt.ylabel('% Değişim')
plt.title('Ürünlerin Günlük Fiyat Değişimleri')
plt.xticks(rotation=45)
plt.legend(title="Ürünler")
plt.grid(True)
plt.tight_layout()
plt.show()
