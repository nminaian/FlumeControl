"""Inspired by the plotting implementation in `boilerdaq`, with placeholders."""

from dataclasses import dataclass
from typing import Deque

import pyqtgraph

pyqtgraph.setConfigOptions(antialias=True)
DELAY = 2
HISTORY_LENGTH = 600


@dataclass
class Result:
    name: str
    unit: str
    history: Deque[float]


class Plotter:
    """A plotter."""

    window = pyqtgraph.GraphicsWindow()  # type: ignore

    def __init__(
        self,
        title: str,
        results: list[Result],
        row: int = 0,
        col: int = 0,
    ):
        self.all_results: list[Result] = []
        self.all_curves: list[pyqtgraph.PlotCurveItem] = []
        self.all_histories: list[Deque[float]] = []
        self.time: list[int] = [-i * DELAY for i in range(HISTORY_LENGTH)]
        self.time.reverse()
        self.add(title, results, row, col)

    def add(self, title: str, results: list[Result], row: int, col: int):
        """Plot results to a new pane in the plot window.

        Attributes
        ----------
            title: The title of an additional plot.
            results: The results to plot.
            row: The window row to place an additional plot.
            col: The window column to place an additional plot.
        """

        plot = self.window.addPlot(row, col)
        plot.addLegend()
        plot.setLabel("left", units=results[0].unit)
        plot.setLabel("bottom", units="s")
        plot.setTitle(title)
        self.all_results.extend(results)
        histories = [result.history for result in results]
        self.all_histories.extend(histories)
        names = [result.name for result in results]
        for i, (history, name) in enumerate(zip(histories, names, strict=True)):
            curve = plot.plot(self.time, history, pen=pyqtgraph.intColor(i), name=name)
            self.all_curves.append(curve)

    def update(self):
        """Update plots."""
        for curve, history in zip(self.all_curves, self.all_histories, strict=True):
            curve.setData(self.time, history)
