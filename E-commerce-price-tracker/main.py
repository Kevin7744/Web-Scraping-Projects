from bs4 import BeautifulSoup
import requests
import pprint

# parse the hmtl page
page=requests.get("http://localhost:8000/shop-cart/products.html")
soup=BeautifulSoup(page.content, "html.parser")

# retrieve all the products
# def retrieve_all_product_price():
#     all_products = soup.find_all('li', class_='span4')
#     product_one = all_products[0]
#     product_one_price = product_one.find("strong")
#     print(product_one_price.get_text())
#     print(product_one_price.get_text().strip().strip('$'))

# Fake price comparator
def lazy_comaprator():
    all_products = soup.find_all('li', class_='span4')
    products = {}
    for product in all_products:
        products[product.find("p").get_text().strip()] = product.find("strong").get_text().strip().strip("$")
    sort = sorted([(v, k) for k, v in products.items()])
    pprint.pprint(sort)

if __name__ == '__main__':
    # retrieve_all_product_price()
    lazy_comaprator()

