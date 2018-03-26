# GPIO controlling
Position of GPIO pins : https://i.imgur.com/aIdC4EE.png
![alt text](https://i.imgur.com/aIdC4EE.png "GPIO")


## Make LED blink
Using GPIO_05 as an output.
- Connect LED with a resistor (~300 ohm)
`GPIO_05(signal)` --- `LED` --- `resistor` --- `GPIO_06(ground)`
- Run `LED_blink.py`

## Control LED via Firebase
- Create a Firebase project, get the ApiKey
- Upload this json as the database structure.
https://github.com/Wesely/RaspPython/blob/master/PyrebaseGPIO/GPIO_Database.json
- Connect `LED` with a `300 ohm resistor`, between `GPIO_05` and `GPIO_06`
- Run `LED_Firebase_control.py` on RaspberryPi. It will listen to Firebase streaming.
https://github.com/Wesely/RaspPython/blob/master/PyrebaseGPIO/LED_Firebase_control.py
- Goto `Firebase > database`, change the value of `GPIO_05`, the LED will be changed, too.
