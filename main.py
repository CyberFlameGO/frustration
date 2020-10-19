fails = 0

def on_pin_pressed_p0():
    global fails
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.pause(1000)
    fails += 1
    basic.show_number(fails)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global fails
    fails = 0
    basic.show_leds("""
        # # # . #
        # . # . #
        # . # . #
        # . # # #
        # . . . .
        """)
    basic.pause(1000)
    basic.show_number(fails)
input.on_button_pressed(Button.A, on_button_pressed_a)
