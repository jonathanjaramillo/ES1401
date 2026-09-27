import time
from XRPLib.defaults import *


# Change these three numbers after doing Part 2 of the assignment.
MIN_DISTANCE = 5.0
MAX_DISTANCE = 200.0
MAX_JUMP = 25.0


def reliable_distance():
    """Read the sensor until three good readings have been collected."""
    accepted = []
    last_reading = None

    while len(accepted) < 3:
        reading = rangefinder.distance()  # centimeters

        # Rule 1: ignore readings that cannot be trusted.
        if reading == 0 or reading == rangefinder.MAX_VALUE:
            time.sleep(0.05)
            continue

        if reading < MIN_DISTANCE or reading > MAX_DISTANCE:
            time.sleep(0.05)
            continue

        # Rule 2: ignore a reading that is much different from the last one.
        # The first good reading has no previous reading to compare with.
        if last_reading is not None:
            if abs(reading - last_reading) > MAX_JUMP:
                continue

        # This reading passed both tests, so keep it.
        accepted.append(reading)
        last_reading = reading
        time.sleep(0.05)

    # Rule 3: average the three good readings.
    return (accepted[0] + accepted[1] + accepted[2]) / 3


# Keep reading and printing the filtered distance.
while True:
    distance = reliable_distance()
    print("Distance:", distance, "cm")
    time.sleep(0.1)
