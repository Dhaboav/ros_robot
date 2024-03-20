#!/usr/bin/env python3
import os
import json


class Model:
    def __init__(self) -> None:
        dir = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir, 'settings.json')
        with open(json_path) as json_file:
            json_data = json.load(json_file)

        self.front_camera = [
            json_data['widthCamera'],
            json_data['heightCamera'],
            json_data['frontCamera']['index'],
            json_data['frontCamera']['comPort'],
            json_data['frontCamera']['modelPath'],
            json_data['frontCamera']['labelPath'],
            json_data['frontCamera']['threshold']
        ]
        
        self.omni_camera = [
            json_data['widthCamera'],
            json_data['heightCamera'],
            json_data['omniCamera']['index'],
            json_data['omniCamera']['comPort'],
            json_data['omniCamera']['xCenter'],
            json_data['omniCamera']['yCenter'],
            json_data['omniCamera']['lowerColor'],
            json_data['omniCamera']['upperColor'],
            json_data['omniCamera']['kernelValue'],
            json_data['omniCamera']['erodeValue'],
            json_data['omniCamera']['dilasiValue']
        ]