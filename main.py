
import requests
from bs4 import BeautifulSoup
import smtplib

user_price=4000.00#SET YOUR TARGET PRICE HERE


def send_mail(price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="*******",password="******")#YOUR BOT EMAIL ID AND PASSWORD
        connection.sendmail(from_addr="*******",#YOUR BOT EMAIL ID AND PASSWORD
                            to_addrs="********",#YOUR PERSONAL EMAIL ID
                            msg=f"subject: LOW PRICE ALERT!\nThe Price is Now {price}",)

URL = "https://www.amazon.in/dp/B084DWH53T?pf_rd_r=2G6B7F505H8F2PJNB840&pf_rd_p=07f4cd28-387a-4e6f-a233-28a4e86529c3"
#THE URL IS THE LINK OF THE PRODUCT IN THE AMAZON WEBSITE
response = requests.get(URL, headers= {"User-Agent":"Defined"})
data = response.text

soup = BeautifulSoup(data,"html.parser")

price = soup.select(selector="#mbc-price-1")   #THIS WILL GIVE US THE PRICE AS A LIST, BUT THERE'LL BE ONLY ONE ELEMENT, SO USE INDEX 0.


price_string = price[0].getText()

cost=price_string.split() #THIS ALSO GIVES US A LIST
print(cost[1])
list_of_digits = cost[1].split(",")

final_price = float("".join(list_of_digits))

if final_price <= user_price:
    send_mail(final_price)