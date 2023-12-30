
from bs4 import BeautifulSoup
import requests
import smtplib

PRODUCT_URL = "https://www.amazon.com/Monster-Headlight-Rechargeable-Batteries-Included/dp/B09K72PB6C/ref=sr_1_3_sspa?keywords=rc+car&qid=1703815145&sr=8-3-spons&ufe=app_do%3Aamzn1.fos.17d9e15d-4e43-4581-b373-0e5c1a776d5d&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
CURRENT_PRICE = 52.79

def get_price():

    web_page = requests.get(PRODUCT_URL)
    soup = BeautifulSoup(web_page.content, 'html.parser')

    price = soup.find(name="span", class_="a-price-whole").getText()
    priceCents = soup.find(name="span", class_="a-price-fraction").getText()

    return float(price + priceCents)

def send_email(price):

    from_address = "anthonyWoodPython15@gmail.com"
    to_address = "woodanthony15@gmail.com"
    password = "odln rggw jhdv yhnw"
    subject = "Price Drop on RC car ya dingus!"
    msg = f"HEY, YOU! The price of the product you want is now ${price}!\nGO AND BUY IT!\n{PRODUCT_URL}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, f"Subject: {subject}\n\n{msg}")
        server.quit()
        print("Email Sent Successfully")

    except Exception as e:
        print("Email Failed to Send with errror: ", e)
    


def main():
    
    price = get_price()
    print(price)

    if price < CURRENT_PRICE:
        send_email(price)
        


if __name__ == '__main__':
    main()