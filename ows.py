import pyowm
own=pyowm=OWM('079e2ccc90467ae079a158c3c9d3d609')
observation=own.weather_at_zip_code('77081','US')
print(observation)