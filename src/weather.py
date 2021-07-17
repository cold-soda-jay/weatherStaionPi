from flask import Flask, render_template
app = Flask(__name__)
from utility import *
import os, time


ut = Utility()

@app.route('/')
def index():

    out_temp, weather_icon, out_humm, in_temp, in_humm = ut.load_weather()
    
    return render_template('index.html',
                            title = TITLE,
                            out_temp = out_temp,
                            in_temp =  in_temp,
                            out_humm = out_humm,
                            in_humm = in_humm,
                            weather_icon = weather_icon)





if __name__ == '__main__':
   app.run(host=HOST,port=PORT)
