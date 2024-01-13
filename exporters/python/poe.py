import requests
import json
import time
from prometheus_client import start_http_server, Gauge

def get_peoples_on_space(astros_on_space_url: str):
    """
    Get the number of people on space
    curl -GET curl -GET http://api.open-notify.org/astros.json | jq .
    docker build -t gmaas2/poe:1.0
    docker run -d -p 8899:8899 --name poe-exporter gmaas2/poe:1.0
    """
    try:
        response = requests.get(astros_on_space_url)
        data = response.json()
        print(data)
        return data['number']
    except Exception as error:
        print('Error on get astros.')
        raise error
    

def update_peoples_on_space_metric(astros_on_space_url: str):
    """
    Update the number of peoples on space metric
    """ 
    try:
        number_of_peoples_on_space_metric = Gauge('astros_on_space', 'Number of peopels on space')
        while True:
            number_of_people_on_space = get_peoples_on_space(astros_on_space_url)
            number_of_peoples_on_space_metric.set(number_of_people_on_space)
            print(f'Number of people/astros on space in this moment: {number_of_people_on_space}.')
            time.sleep(10)
    except Exception as error:
        print('Error on update metric.')
        raise error

    
def exporter_http_server_init():
    """
    Init Prometheus http server
    """ 
    try:
        start_http_server(8899)
        print('HTTP Server initialited on port 8889')
        return True
    except Exception as error:
        print('Error on export http endpoint metrics')
        raise error
    
def main():
    ASTROS_ON_SPACE_URL = "http://api.open-notify.org/astros.json"
    exporter_http_server_init()
    update_peoples_on_space_metric(ASTROS_ON_SPACE_URL)

if __name__ == '__main__':
    main()