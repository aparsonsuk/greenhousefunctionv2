def Status():
    basic.show_string("Temp:")
    basic.show_number(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C))
    basic.pause(1000)
    basic.show_string("Soil:")
    basic.show_number(kitronik_smart_greenhouse.read_io_pin(kitronik_smart_greenhouse.PinType.ANALOG,
            kitronik_smart_greenhouse.IOPins.P1))
    basic.pause(1000)
    basic.show_string("humid:")
    basic.show_number(kitronik_smart_greenhouse.humidity())
    basic.pause(1000)

def on_button_pressed_a():
    zipStick.set_color(kitronik_smart_greenhouse.colors(ZipLedColors.PURPLE))
    zipStick.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    zipStick.clear()
    zipStick.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Status()
input.on_button_pressed(Button.B, on_button_pressed_b)

def WaterPlants():
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(True))
    basic.pause(1000)
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(False))
    basic.pause(2000)
soilHue = 0
humidHue = 0
tempHue = 0
zipStick: kitronik_smart_greenhouse.greenhouseZIPLEDs = None
zipLEDs = kitronik_smart_greenhouse.create_greenhouse_zip_display(8)
statusLEDs = zipLEDs.status_leds_range()
zipStick = zipLEDs.zip_stick_range()

def on_forever():
    global tempHue, humidHue, soilHue
    tempHue = Math.map(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C),
        0,
        40,
        210,
        0)
    humidHue = Math.map(kitronik_smart_greenhouse.humidity(), 0, 100, 35, 150)
    soilHue = Math.map(kitronik_smart_greenhouse.read_io_pin(kitronik_smart_greenhouse.PinType.ANALOG,
            kitronik_smart_greenhouse.IOPins.P1),
        0,
        1023,
        35,
        150)
    statusLEDs.set_zip_led_color(0, tempHue)
    statusLEDs.set_zip_led_color(1, humidHue)
    statusLEDs.set_zip_led_color(2, soilHue)
    statusLEDs.show()
    if kitronik_smart_greenhouse.read_io_pin(kitronik_smart_greenhouse.PinType.ANALOG,
    kitronik_smart_greenhouse.IOPins.P1) <= 400:
        basic.show_icon(IconNames.SAD)
        for index in range(2):
            WaterPlants()
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
