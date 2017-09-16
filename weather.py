import pyowm
import re
owm = pyowm.OWM('d5ef4e775014720f649791b7c7bfb5af')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')


observation = owm.weather_at_place('Allahabad,in')
w = observation.get_weather()
a = str(w)
b = re.sub('[^A-Za-z0-9]', '', a)
c=b[b.find("s")+6:]



x = w.get_temperature('celsius')
y=str(x)
z = re.sub('[^0-9]', '', y)
d = 'The temperature is '+z[:2]+' degree celsius. And it looks like it will be, '+c+' today.'
temp = 'The temperature is '+z[:2]+' degree celsius.'
