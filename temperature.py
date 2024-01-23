import Adafruit_DHT
import requests
import time

# ThingSpeak API endpoint and API key
THINGSPEAK_API_ENDPOINT = "https://api.thingspeak.com/update"
THINGSPEAK_API_KEY = ""

# DHT22 sensor settings
DHT_SENSOR_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 4  # Replace with the actual GPIO pin connected to the sensor

def read_dht22_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, DHT_PIN)
    return humidity, temperature

def send_to_thingspeak(api_key, field1, field2):
    payload = {'api_key': api_key, 'field1': field1, 'field2': field2}
    response = requests.post(THINGSPEAK_API_ENDPOINT, params=payload)
    return response.status_code

def main():
    try:
        while True:
            humidity, temperature = read_dht22_sensor()

            if humidity is not None and temperature is not None:
                print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
                status_code = send_to_thingspeak(THINGSPEAK_API_KEY, temperature, humidity)

                if status_code == 200:
                    print("Data sent to ThingSpeak successfully!")
                else:
                    print(f"Failed to send data. Status code: {status_code}")

            else:
                print("Failed to retrieve data from DHT22 sensor.")

            time.sleep(300)  # Delay for 5 mins before reading and sending data again

    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
