function Status () {
    basic.showString("Temp:")
    basic.showNumber(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C))
    basic.pause(1000)
    basic.showString("Soil:")
    basic.showNumber(kitronik_smart_greenhouse.readIOPin(kitronik_smart_greenhouse.PinType.analog, kitronik_smart_greenhouse.IOPins.p1))
    basic.pause(1000)
    basic.showString("humid:")
    basic.showNumber(kitronik_smart_greenhouse.humidity())
    basic.pause(1000)
}
input.onButtonPressed(Button.A, function () {
    zipStick.setColor(kitronik_smart_greenhouse.colors(ZipLedColors.Purple))
    zipStick.show()
})
input.onButtonPressed(Button.AB, function () {
    zipStick.clear()
    zipStick.show()
})
input.onButtonPressed(Button.B, function () {
    Status()
})
function WaterPlants () {
    kitronik_smart_greenhouse.controlHighPowerPin(kitronik_smart_greenhouse.HighPowerPins.pin13, kitronik_smart_greenhouse.onOff(true))
    basic.pause(1000)
    kitronik_smart_greenhouse.controlHighPowerPin(kitronik_smart_greenhouse.HighPowerPins.pin13, kitronik_smart_greenhouse.onOff(false))
    basic.pause(2000)
}
let soilHue = 0
let humidHue = 0
let tempHue = 0
let zipStick: kitronik_smart_greenhouse.greenhouseZIPLEDs = null
let zipLEDs = kitronik_smart_greenhouse.createGreenhouseZIPDisplay(8)
let statusLEDs = zipLEDs.statusLedsRange()
zipStick = zipLEDs.zipStickRange()
basic.forever(function () {
    tempHue = Math.map(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C), 0, 40, 210, 0)
    humidHue = Math.map(kitronik_smart_greenhouse.humidity(), 0, 100, 35, 150)
    soilHue = Math.map(kitronik_smart_greenhouse.readIOPin(kitronik_smart_greenhouse.PinType.analog, kitronik_smart_greenhouse.IOPins.p1), 0, 1023, 35, 150)
    statusLEDs.setZipLedColor(0, tempHue)
    statusLEDs.setZipLedColor(1, humidHue)
    statusLEDs.setZipLedColor(2, soilHue)
    statusLEDs.show()
    if (kitronik_smart_greenhouse.readIOPin(kitronik_smart_greenhouse.PinType.analog, kitronik_smart_greenhouse.IOPins.p1) <= 400) {
        basic.showIcon(IconNames.Sad)
        for (let index = 0; index < 2; index++) {
            WaterPlants()
        }
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
