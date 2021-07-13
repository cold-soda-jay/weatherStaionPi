import bs4
import requests
import re
from fake_useragent import UserAgent


try:
    import adafruit_dht as ada                                                                       
    import Adafruit_DHT
except:
    print("None Package: Adafruit_DHT")
from config import *



class Utility:

    location="2892794"

    def __init__(self):
        self.session = requests.Session()
        self.location = LOCATION

    
    def get_weather(self):
        try:
            response = self.session.get(f"https://www.weather.de/location/{LOCATION}")
            data = bs4.BeautifulSoup(response.text, "html.parser")
            today = data.select_one("#content > div:nth-child(1) > div > div.wn-box.wn-temperature")
            img_url = today.find("img").attrs["src"]
            temprature = today.text[:-2]
            humidity_text = data.select_one("#content > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(2) > div").text
            humidity = re.findall(r"\d.*\d", humidity_text)[0]
            return temprature, img_url, humidity
        except:
            return 'NaN', 'NaN', 'NaN'

    def get_weather_google(self):
        try:
            ua = UserAgent()
            
            header = {"User-Agent":ua.random,
                        "cookie": COOKIE,
                        "x-client-data": "CI+2yQEIpLbJAQjEtskBCKmdygEIjuXKAQjQmssBCKCgywEIrfLLAQjc8ssBCO/yywEIs/jLAQie+csBCPX5ywEYjp7LARi68ssBGN/5ywE="}

            response = self.session.get(f"https://www.google.com/search?q=weather+{LOCATION}", headers=header)
            data = bs4.BeautifulSoup(response.text, "html.parser")
            temprature = data.select_one("#wob_tm").text
            img_url = data.select_one("#wob_tci").attrs["src"]
            humidity_text = data.select_one("#wob_hm").text
            humidity = re.findall(r"\d.*\d", humidity_text)[0]
            return temprature, img_url, humidity
        except:
            return 'NaN', 'NaN', 'NaN'

    def get_home(self):
        dht = ada.DHT11(PIN)
        try:
            #humidity,tempe_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
            tempe_c = dht.temperature
            humidity = dht.humidity
            return tempe_c, humidity
        except RuntimeError as error:
            print(error.args[0])
            return 'NaN', 'NaN'
    
    def geather_info(self):
        out_temp, weather_icon, out_humm = self.get_weather()
        in_temp, in_humm =  self.get_home()
        with open("data.txt", "a+") as f:
                f.write(f"\n{out_temp},{weather_icon},{out_humm},{in_temp}, {in_humm}")
        

    def load_weather(self):
        try:
            with open("data.txt", "r") as f:
                line = f.readlines()[-1]
                out_temp, weather_icon, out_humm, in_temp, in_humm = line.split(",")
        except :
            print("No such file!")
            line = "NaN,NaN,NaN,NaN,NaN"
        return line.split(",")
            


if __name__ == '__main__':
    ut = Utility()

    print(ut.get_weather())