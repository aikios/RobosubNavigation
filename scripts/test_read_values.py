import bluerobotics_navigator as navigator
from bluerobotics_navigator import UserLed
clanker_attributes=[0]*7
navigator.init()

navigator.set_led(UserLed.Led1, True)

clanker_attributes[0] = navigator.read_pressure()
clanker_attributes[1] = navigator.read_temp()
#clanker_attributes[2] = navigator.read_mag()
clanker_attributes[3] = navigator.self_test()
#clanker_attributes[4] = navigator.read_gyro()
#clanker_attributes[5] = navigator.read_adc_all().channel
clanker_attributes[6] = navigator.read_accel()


i = 0;
while(i<len(clanker_attributes)):
	print(clanker_attributes[i])
	i+=1;

navigator.set_led(UserLed.Led1, False)
