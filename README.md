# flights

## Hardware
I run this on a Raspberry Pi 3 with a Pimoroni Unicorn Hat HD. I haven't tested it on other hardware. The Unicorn Hat HD was discontinued, but you may be able to find old stock or buy used on eBay. 

## Install

From your RPI terminal:

```
git clone https://github.com/canary-code/rpi-flights.git
cd rpi-flights
pip install -r requirements.txt
```

## Configuration

Edit the `config.json` file to set the latitude, longitude, and radius (in meters) for observations. The default is the White House.

Set your local airport codes in `airports`.

The `colors` have 3 settings: `home` (taking off from a local airport), `away` (neither taking off nor landing at a local airport), and `landing` (landing at a local airport).

## Running

Run the app with `python main.py`.






