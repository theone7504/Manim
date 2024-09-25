from manim import *

class TransformationsOnXSquare(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 8, 2],
            axis_config={"color": BLUE},
        )

        # Original function y = x^2
        original_graph = axes.plot(lambda x: x**2, color=WHITE, x_range=[-4, 4])

        # Labels
        graph_label = axes.get_graph_label(original_graph, label="y = x^2")
        formula_text = MathTex("y = x^2").to_edge(UP)

        # Display the original graph
        self.play(Create(axes), Create(original_graph), Write(formula_text), Write(graph_label))
        self.wait(2)

        # Define the transformations
        transformations = [
            (lambda x: 2 * x**2, "y = 2x^2"),  # Vertical Stretch
            (lambda x: 0.5 * x**2, "y = \\frac{1}{2}x^2"),  # Vertical Shrink
            (lambda x: (x/2)**2, "y = \\left(\\frac{x}{2}\\right)^2"),  # Horizontal Stretch
            (lambda x: (2*x)**2, "y = (2x)^2"),  # Horizontal Shrink
            (lambda x: -x**2, "y = -x^2"),  # Reflection about x-axis
            (lambda x: (-x)**2, "y = (-x)^2"),  # Reflection about y-axis
        ]

        # Animate each transformation
        for transform, formula in transformations:
            # Create new graph and formula text
            new_graph = axes.plot(transform, color=YELLOW, x_range=[-4, 4])
            new_formula_text = MathTex(formula).to_edge(UP)

            # Transition to the new graph
            self.play(
                Transform(formula_text, new_formula_text),
                Transform(original_graph, new_graph),
            )
            self.wait(2)

        self.wait()

