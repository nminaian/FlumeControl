"""Inspired by the PID implementation in `boilerdaq`, with placeholders."""

from typing import Tuple

from simple_pid import PID


class VFD:
    """A VFD."""

    def __init__(self):
        pass

    def write(self, value):
        """Write a value to the VFD."""
        pass


class Sensor:
    """A sensor."""

    def __init__(self):
        pass

    def get(self) -> float:
        """Get a sensor reading."""
        return float()


class Controller:
    """A PID controller."""

    def __init__(
        self,
        vfd: VFD,
        feedback_sensor: Sensor,
        setpoint: float,
        gains: Tuple[float, float, float],
        output_limits: Tuple[float, float],
    ):
        self.vfd = vfd
        self.feedback_sensor = feedback_sensor
        self.feedback_value = self.feedback_sensor.get()
        self.pid = PID(*gains, setpoint, output_limits=output_limits)

    def update(self):
        """Update the PID controller."""

        control_value = self.pid(self.feedback_value)
        print(f"{self.feedback_value} {control_value}")
        self.vfd.write(control_value)
