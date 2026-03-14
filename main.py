#!/usr/bin/python

import sys
import os
import time
import json

import overhead

def load_config(filepath):
    """Loads a JSON config file with error handling."""
    if not os.path.exists(filepath):
        print(f"Error: Config file not found at {filepath}")
        return {}
    
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        return {}


def main_loop():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    sleep = config['sleep']
    latitude = config['location']['latitude']
    longitude = config['location']['longitude']
    radius = config['location']['radius']
    airports = config['airports']
    home_color = config['colors']['home']
    away_color = config['colors']['away']
    landing_color = config['colors']['landing']

    overhead.setup(latitude, longitude, radius, airports, home_color, away_color, landing_color)

    while 1:
        overhead.update()
        overhead.draw()
        time.sleep(sleep)


if __name__ == '__main__':
    try:
        config = load_config('config.json')
        main_loop()
    except KeyboardInterrupt:
        overhead.shutdown()
        sys.exit(0)

    overhead.shutdown()
