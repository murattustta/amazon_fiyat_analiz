import requests
from bs4 import BeautifulSoup
import pyodbc
from datetime import datetime

# SQL Server bağlantısı için gerekli bilgileri girin
# Kendi sunucu adınızı ve veritabanı adınızı buraya girin
server = r'your_server_name'  # SQL Server sunucu adı
database = 'your_database_name'  # Bağlanmak istediğiniz veritabanı

# Windows Authentication kullanarak SQL Server'a bağlanma
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Ürün verilerini ekleme fonksiyonu
def save_to_db(product_id, product_name, price):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
    INSERT INTO product_prices (product_id, product_name, price, date)
    VALUES (?, ?, ?, ?)
    ''', (product_id, product_name, price, date))
    conn.commit()

def get_page_content(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"HTTP Hatası: {e}")
        return None

def parse_product_price(soup):
    price = soup.select_one('span.a-price-whole')
    if price:
        clean_price = price.get_text().strip().replace('.', '').replace(',', '')
        return int(clean_price)
    return None

def fetch_and_save_products():
    # Buradaki URL'leri ve ürün adlarını kendi izlemek istediğiniz ürünlerin URL'leri ile değiştirin
    products = {
        1: {'url': 'your_product_url_1', 'alias': 'Product 1'},
        2: {'url': 'your_product_url_2', 'alias': 'Product 2'},
        3: {'url': 'your_product_url_3', 'alias': 'Product 3'},
        4: {'url': 'your_product_url_4', 'alias': 'Product 4'},
        5: {'url': 'your_product_url_5', 'alias': 'Product 5'}
    }

    # Kendi User-Agent bilginizi buraya girin
    headers = {
        "User-Agent": "your_user_agent"  # Kendi User-Agent bilginizi buraya girin
    }

    for product_id, product_info in products.items():
        content = get_page_content(product_info['url'], headers)
        if content:
            soup = BeautifulSoup(content, 'html.parser')

            product_title = product_info['alias']
            product_price = parse_product_price(soup)

            if product_title and product_price is not None:
                save_to_db(product_id, product_title, product_price)
                print(f"Veri kaydedildi: {product_title}, {product_price} TL")
            else:
                print("Ürün adı veya fiyatı bulunamadı.")
        else:
            print(f"Sayfa içeriği alınamadı: {product_info['url']}")

fetch_and_save_products()

conn.close()
