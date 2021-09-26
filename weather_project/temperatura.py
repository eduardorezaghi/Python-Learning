from pyowm import OWM

chave_api = ''

def obtem_temperatura(local):
    climate_api = OWM(chave_api)
    local_observed = climate_api.weather_at_place(local)
    local_climate = local_observed.get_weather()
    temperatura = local_climate.get_temperature(unit='celsius')

    return temperatura
