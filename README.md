# Temperature Reader
https://thingspeak.com/channels/2410181

## Setup
1. Add Thinkspeak API Key to temperature.sh.
2. Add system service to run on device startup.
```bash
cp temperature.service /etc/systemd/system
```
3. Enable service
```bash
sudo systemctl daemon-reload
sudo systemctl enable temperature.service
```
