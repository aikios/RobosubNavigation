import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import time

FREQUENCY = 50 # 50-400 Hz; higher values increase precision but decrease allowable latency

MIN_PULSE_MICROSEC = 1100
MED_PULSE_MICROSEC = 1500
MAX_PULSE_MICROSEC = 1900

print("Initializing navigator...")
navigator.init()
navigator.set_pwm_freq_hz(FREQUENCY)

def set_duty_cycle(channel, value):
    """
    Sets PWM channel to value between -1 to 1.
    """
    msec = MED_PULSE_MICROSEC + value * (MAX_PULSE_MICROSEC - MIN_PULSE_MICROSEC) / 2
    navigator.set_pwm_channel_value(channel, int(4095 * msec / (1 / FREQUENCY * 1e6)))

def enable():
    navigator.pwm_enable(True)
def disable():
    navigator.pwm_enable(False)

set_duty_cycle(PwmChannel.Ch1, 0)
enable()

for i in range(4):
    print(f"Starting iteration {i+1}")
    set_duty_cycle(PwmChannel.Ch1, 0.2)
    time.sleep(1)
    set_duty_cycle(PwmChannel.Ch1, 0)
    time.sleep(1)
    set_duty_cycle(PwmChannel.Ch1, -0.2)
    time.sleep(1)

set_duty_cycle(PwmChannel.Ch1, 0)
disable()
