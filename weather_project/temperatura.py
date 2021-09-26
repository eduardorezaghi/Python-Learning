from pyowm import OWM

chave_api = '9d23aeb1c193dbd4fd958ef184504a1e'

def obtem_temperatura(local):
    climate_api = OWM(chave_api)
    local_observed = climate_api.weather_at_place(local)
    local_climate = local_observed.get_weather()
    temperatura = local_climate.get_temperature(unit='celsius')

    return temperatura