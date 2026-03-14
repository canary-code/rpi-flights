from FlightRadar24 import FlightRadar24API
import sys
import math

try:
    import unicornhathd as unicorn
    print("16x16 unicornhathd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.clear()

this = sys.modules[__name__]
this.bounds = []
this.flights = []
this.sightings = []
this.my_airports = []
this.home_color = [117,210,71]
this.away_color = [252,76,2]
this.landing_color = [67,89,255]

def setup(latitude, longitude, radius, airports, home_color, away_color, landing_color):
    unicorn.clear()

    this.fr_api = FlightRadar24API()
    this.bounds = this.fr_api.get_bounds_by_point(latitude, longitude, radius)

    this.my_airports = airports
    this.home_color = home_color
    this.away_color = away_color
    this.landing_color = landing_color

    unicorn.rotation(-90)
    unicorn.clear()
    unicorn.brightness(0.2)

    print("Setup complete.")

def update():
    this.flights = None
    this.flights = this.fr_api.get_flights(bounds = this.bounds)
    this.flights.sort(key=lambda x: x.altitude, reverse=True)
    print(f"Found {len(this.flights)} flights")

def draw():
    unicorn.clear()

    x = 0
    quantized_speed = 600/16
    quantized_altitude = 35000/16

    for f in this.flights:
        if f.destination_airport_iata == "" or f.altitude < 10:
            continue

        q_alt = math.ceil(int(f.altitude / quantized_altitude))
        print(f"Flight {f.callsign} at {f.altitude} ft, spot #{q_alt}")

        if x >= 15:
            break
            x = 0
        else:
            x = x+1
        if f.origin_airport_iata in this.my_airports:
            color = this.home_color
        elif f.destination_airport_iata in this.my_airports:
            color = this.landing_color
        else:
            color = this.away_color

        max_y = math.ceil(int(f.ground_speed / quantized_speed))
        if max_y > 15: max_y = 15
        if max_y < 1: max_y = 1

        for y in range(0, 15):
            if y >= max_y:
                unicorn.set_pixel(x, y, 0, 0, 0)
            else:
                unicorn.set_pixel(x, y, *color)

    unicorn.show()

def shutdown():
    unicorn.clear()
    unicorn.off()
    sys.exit()

