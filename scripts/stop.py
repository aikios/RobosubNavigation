import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

print("Stopping the sub")
navigator.init()

navigator.set_pwm_channel_value(PwmChannel.Ch1, 0)