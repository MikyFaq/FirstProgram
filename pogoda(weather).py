#Weather v.1
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

#Use 'openweathermap' for get your API key
owm = OWM('Your API')
mgr = owm.weather_manager()
place = input("В каком городе/стране?(which city/country?):")
#Get info about weather
observation = mgr.weather_at_place(place)
w = observation.weather
#About temperature
temp = w.temperature('celsius')["temp"]
#print
print ("В городе(in city) " + place + " сейчас(right now) " + w.detailed_status )
print ("Температура сейчас(temperature now):" + str(temp))
input()