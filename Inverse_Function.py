from manim import *

class InverseFunctions(Scene):
    def construct(self):
        # Create a SquareGrid to ensure equal scaling
        grid = NumberPlane(
            x_range=[-2, 4, 1],
            y_range=[-2, 4, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        ).scale(1.25)

        # Add labels to the axes
        grid_labels = grid.get_axis_labels(x_label="x", y_label="y")

        # Define the exponential function e^x
        exp_graph = grid.plot(lambda x: np.exp(x), color=YELLOW, x_range=[-2, 1.5])
        exp_label = MathTex("e^x").next_to(grid.c2p(1, np.exp(1)), UR)

        # Define the natural logarithm function ln(x)
        ln_graph = grid.plot(lambda x: np.log(x), color=GREEN, x_range=[0.1, 4])
        ln_label = MathTex("\\ln(x)").next_to(grid.c2p(np.exp(1), 1), UR)

        # Define the line y=x
        line_graph = grid.plot(lambda x: x, color=RED, x_range=[-2, 4])
        line_label = MathTex("y=x").next_to(grid.c2p(3, 3), UR)

        # Add graphs and labels to the scene
        self.play(Create(grid), Write(grid_labels))
        self.play(Create(exp_graph), Write(exp_label))
        self.play(Create(line_graph), Write(line_label))

        # Transform exponential graph to the logarithm graph, but keep the original
        ln_graph_copy = ln_graph.copy()
        self.play(Create(ln_graph_copy), Write(ln_label))

        # Highlight reflection
        reflection_arrow = Arrow(start=grid.c2p(1, np.exp(1)), end=grid.c2p(np.exp(1), 1), buff=0, color=PURPLE)
        self.play(Create(reflection_arrow))
        reflection_text = MathTex(r"(1, e)", r"\leftrightarrow", r"(e, 1)").to_edge(DOWN)
        self.play(Write(reflection_text))

        # Show reflection of a point
        point = Dot(grid.c2p(1, np.exp(1)), color=YELLOW)
        reflected_point = Dot(grid.c2p(np.exp(1), 1), color=GREEN)
        
        self.play(FadeIn(point), FadeIn(reflected_point))
        self.play(point.animate.move_to(grid.c2p(2, np.exp(2))), reflected_point.animate.move_to(grid.c2p(np.exp(2), 2)))

        # Show final graph with reflection text
        self.wait(2)
