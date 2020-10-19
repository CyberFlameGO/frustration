let fails = 0
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    basic.pause(1000)
    fails += 1
    basic.showNumber(fails)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    fails = 0
    basic.showLeds(`
        # # # . #
        # . # . #
        # . # . #
        # . # # #
        # . . . .
        `)
    basic.pause(1000)
    basic.showNumber(fails)
})
