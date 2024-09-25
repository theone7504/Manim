from manim import *
import pandas as pd
import numpy as np


class ScatterPlotAnimatedScene(Scene):

    def construct(self):
        # Download data and put in DataFrame
        data_url = "https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_normal.csv"
        df = pd.read_csv(data_url)

        # Perform linear regression to get the line of best fit
        x = df['x']
        y = df['y']
        coefficients = np.polyfit(x, y, 1)
        slope, intercept = coefficients

        # Define the line of best fit function
        def line_of_best_fit(x):
            return slope * x + intercept

        # Animate the creation of Axes
        ax = Axes(x_range=[0, 100, 5], y_range=[-20, 200, 10], axis_config={"include_numbers": True})
        self.play(Write(ax))

        self.wait()  # wait for 1 second

        # Animate the creation of dots
        dots = [Dot(ax.c2p(x_val, y_val), color=BLUE) for x_val, y_val in df.values]
        self.play(LaggedStart(*[Write(dot) for dot in dots], lag_ratio=.05))

        self.wait(1)  # wait for 1 second

        # Add the line of best fit
        line_start = ax.c2p(0, line_of_best_fit(0))
        line_end = ax.c2p(100, line_of_best_fit(100))
        line = Line(start=line_start, end=line_end, color=RED)
        self.play(Write(line))

        self.wait(8)  # wait for 8 second


