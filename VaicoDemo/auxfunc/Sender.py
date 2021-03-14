"""
Functions for cast and make an HTTP request to AWS API to store predictions

JCA
Vaico
"""
import base64
import json
from time import strftime, localtime
import pickle
import requests
from requests.exceptions import HTTPError
from sys import getsizeof

import cv2 as cv


SERVER = {
    "prod":{
        "api": 'https://1x06civnj2.execute-api.us-east-2.amazonaws.com/DummyStage/newdata/fromstream',
        'key': 'TmEpgrNEOC8KS8FNYKB6zmKnqagJmMC2mW0F6ky0'
        },
    'dev':{
        'key':'SbdzW13c8E8mLkf9NEkk14a2o3hh5nN04hXo7spM',
        'api': ' https://j8wmps8gr0.execute-api.us-east-2.amazonaws.com/testing/newdata/fromstream'
        }
}

class Sender:
    def __init__(self,observer, sender, place='local-test', stage='dev'):
        self.API_ENDPOINT = SERVER[stage]['api']
        self.API_KEY = SERVER[stage]['key']
        print('Sender API {}'.format(self.API_ENDPOINT))
        self.observer = observer
        self.place = place
        self.sender = sender

    def pack_data(self, obs_data):
        """Add data, modify and encode data, to set ready to send"""
        obs_data['frame'] = self.im2json(obs_data['frame'])
        json_data = json.dumps(obs_data)
        print('Package size: {} Kilobyte'.format(getsizeof(json_data) / 1000))
        return json_data

    def send_request(self, model, im):
        """Send general request to server"""
        print(f'Sending request from: {self.observer}')
        date = strftime("%Y-%m-%d_%H:%M:%S", localtime()) # No cambiar formato de la fecha

        payload = {
            'task': 'predict-cloud',
            'place': self.place,
            'observer': self.observer,
            'date': date,
            'frame': im,
            'model': model,
            'sender': self.sender
        }

        json_data = self.pack_data(payload)
        headers = {"x-api-key": self.API_KEY}

        try:
            url = '{}/{}'.format(self.API_ENDPOINT, '')
            print('Wating server response...')
            response = requests.post(url, data=json_data, headers=headers, timeout=6000)  # data-> body in http request
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error occurred: {}'.format(http_err))
            raise HTTPError(http_err)
        except Exception as err:
            print('Other error occurred: {}'.format(err))  # Python 3.6
            raise Exception(err)
        else:
            print('Successfully sent package')
            return response

    def im2json(self, im):
        """Encode image to send"""
        _, imdata = cv.imencode('.JPG', im)
        im_str = base64.b64encode(imdata).decode('ascii')
        return im_str

