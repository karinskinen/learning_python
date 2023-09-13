import requests
import pandas as pd


def get_api_data(variable_id):
    fingrid_api_base_url = 'https://api.fingrid.fi'
    headers = { "x-api-key" : "DCt4V2dyqx91RAXMieYFAaa1DFb7dGYb2XuCWjWN" }
    request_url = fingrid_api_base_url + '/v1/variable/event/json/' + variable_id
    result = requests.get(request_url, headers=headers)

    if result.status_code != 200:
        return []

    return result.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total = get_api_data('124')
    wind = get_api_data('75')

    total_value = total[0].get('value')
    production_wind_value = wind[0].get('value')

    print(total)

    print('total consumption value')

    print(total_value)
    print(production_wind_value)
    print('The percentage of consumption that could be covered by wind:')
    print(production_wind_value/total_value*100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

