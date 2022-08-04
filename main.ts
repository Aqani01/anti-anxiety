input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("you can do this")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("stop overthinking")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("Breath")
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("start counting")
})
basic.showIcon(IconNames.Heart)
basic.showIcon(IconNames.SmallHeart)
basic.showIcon(IconNames.Heart)
