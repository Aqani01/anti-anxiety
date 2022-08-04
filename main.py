def on_button_pressed_a():
    basic.show_string("you can do this")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("stop overthinking")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Breath")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("start counting")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)


basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.SMALL_HEART)
basic.show_icon(IconNames.HEART)
