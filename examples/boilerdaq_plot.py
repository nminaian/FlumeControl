"""Inspired by the plotting implementation in `boilerdaq`, with placeholders."""

from dataclasses import dataclass
from typing import Deque, List

import pyqtgraph

pyqtgraph.setConfigOptions(antialias=True)
DELAY = 2
HISTORY_LENGTH = 600


@dataclass
class Result:
    name: str
    unit: str
    history: Deque


class Plotter:
    """A plotter."""

    window = pyqtgraph.GraphicsWindow()

    def __init__(
        self,
        title: str,
        results: List[Result],
        row: int = 0,
        col: int = 0,
    ):
        self.all_results: List[Result] = []
        self.all_curves: List[pyqtgraph.PlotCurveItem] = []
        self.all_histories: List[Deque] = []
        self.time: List[int] = []
        for i in range(0, HISTORY_LENGTH):
            self.time.append(-i * DELAY)
        self.time.reverse()
        self.add(title, results, row, col)

    def add(self, title: str, results: List[Result], row: int, col: int):
        """Plot results to a new pane in the plot window.

        Parameters
        ----------
        title: str
            The title of an additional plot.
        results: List[Result]
            The results to plot.
        row: int = 0
            The window row to place an additional plot.
        col: int = 0
            The window column to place an additional plot.
        """

        i = 0
        plot = self.window.addPlot(row, col)
        plot.addLegend()
        plot.setLabel("left", units=results[0].unit)
        plot.setLabel("bottom", units="s")
        plot.setTitle(title)
        self.all_results.extend(results)
        histories = [result.history for result in results]
        self.all_histories.extend(histories)
        names = [result.name for result in results]
        for history, name in zip(histories, names):
            curve = plot.plot(self.time, history, pen=pyqtgraph.intColor(i), name=name)
            self.all_curves.append(curve)
            i += 1

    def update(self):
        """Update plots."""
        for curve, history in zip(self.all_curves, self.all_histories):
            curve.setData(self.time, history)
