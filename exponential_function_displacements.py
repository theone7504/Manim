from manim import *

class ExponentialFunctionDisplacements(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 10, 1],
            x_length=8,
            y_length=6,
            tips=False,
            axis_config={"color": GREY_A, "include_numbers": True},
        ).to_edge(DOWN)

        # Labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)

        # Original function: f(x) = e^x
        original_graph = axes.plot(lambda x: np.exp(x), color=BLUE_C, x_range=[-4, 4])

        # Labels
        original_label = axes.get_graph_label(
            original_graph, label="f(x) = e^{x}", x_val=1, direction=UR, buff=0.5
        )

        # Formula text on top
        formula_text = MathTex("f(x) = e^{x}").to_edge(UP)

        # Display the axes and the original graph
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(original_graph), Write(original_label), Write(formula_text))
        self.wait(2)

        # Define transformations with their corresponding formulas
        transformations = [
            {
                "function": lambda x: np.exp(x) + 2,
                "formula": "f(x) = e^{x} + 2",
                "label": "Shift Up by 2",
                "color": YELLOW_C,
            },
            {
                "function": lambda x: np.exp(x) - 2,
                "formula": "f(x) = e^{x} - 2",
                "label": "Shift Down by 2",
                "color": GREEN_C,
            },
            {
                "function": lambda x: np.exp(x + 2),
                "formula": "f(x) = e^{x + 2}",
                "label": "Shift Left by 2",
                "color": MAROON_C,
            },
            {
                "function": lambda x: np.exp(x - 2),
                "formula": "f(x) = e^{x - 2}",
                "label": "Shift Right by 2",
                "color": PURPLE_C,
            },
        ]

        # Animation loop for each transformation
        for transform in transformations:
            # Create new graph
            new_graph = axes.plot(
                transform["function"], color=transform["color"], x_range=[-4, 4]
            )

            # Create new label for the graph
            new_label = axes.get_graph_label(
                new_graph,
                label=transform["formula"],
                x_val=1,
                direction=UR,
                buff=0.5,
                color=transform["color"],
            )

            # Update formula text on top
            new_formula_text = MathTex(transform["formula"]).to_edge(UP)

            # Transition to the new graph
            self.play(
                Transform(original_graph, new_graph),
                Transform(original_label, new_label),
                Transform(formula_text, new_formula_text),
            )
            self.wait(2)

        self.wait()

