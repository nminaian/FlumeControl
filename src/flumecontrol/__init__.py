"""Flume Control PID."""

# sourcery skip: upper-camel-case-classes

__version__ = "0.0.0"


from simple_pid import PID  # type: ignore


class VFD:
    """A VFD."""

    def __init__(self):
        pass

    def write(self, value: float):
        """Write a value to the VFD."""


class Sensor:
    """A sensor."""

    def __init__(self):
        pass

    def get(self) -> float:
        """Get a sensor reading."""
        return float()


class Controller:
    """A PID controller."""

    def __init__(  # noqa: PLR0913
        self,
        vfd: VFD,
        feedback_sensor: Sensor,
        setpoint: float,
        gains: tuple[float, float, float],
        output_limits: tuple[float, float],
    ):
        self.vfd = vfd
        self.feedback_sensor = feedback_sensor
        self.feedback_value = self.feedback_sensor.get()
        self.pid = PID(*gains, setpoint, output_limits=output_limits)

    def update(self):
        """Update the PID controller."""

        control_value = self.pid(self.feedback_value)
        print(f"{self.feedback_value} {control_value}")
        if control_value is not None:
            self.vfd.write(control_value)
