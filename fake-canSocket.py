import time
import random
import can

bus = can.Bus(
	interface="socketcan",
	channel="vcan0"
)

while True:
	temperature = random.randint(20,80)
	
	msg = can.Message(
		arbitration_id=0x456,
		data=[temperature],
		is_extended_id=False
	)
	
	bus.send(msg)
	time.sleep(1)
