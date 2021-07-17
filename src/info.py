from utility import *
import time
import os
from datetime import date


ut = Utility()
start = time.time() 
out_temp, weather_icon, out_humm = ut.get_weather()
#out_temp, weather_icon, out_humm = '16', 'https://www.weather.de/themes/weather/assets/images/icons/weather/04.svg', '93'
while True:
    today = date.today()
    day = today.strftime("%d-%m-%Y")
    try:
        os.system("sudo pkill -9 libgpiod_pulsei")
        now = time.time()
        
        if (now-start)/60 >= 60:
            out_temp, weather_icon, out_humm = ut.get_weather()
            #if out_temp == "NaN":
            #    out_temp, weather_icon, out_humm = '16', 'https://www.weather.de/themes/weather/assets/images/icons/weather/04.svg', '93'
            start = time.time()  
        in_temp, in_humm =  ut.get_home()
        #ut.geather_info()
        with open(f"../data/data_{day}.txt", "a+") as f:
                f.write(f"\n{out_temp},{weather_icon},{out_humm},{in_temp}, {in_humm}")
        print("Data gethered")
        time.sleep(WAIT_TIME)
    except:
        print("Error!")