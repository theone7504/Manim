from manim import *

class TransformationsOnExpGraph(Scene):
    def construct(self):
        # Create the axes with equal scaling for x and y
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"color": BLUE},
            x_length=7,
            y_length=7,
        ).add_coordinates()
        
        title = MathTex("f(x) = e^x").to_edge(UP).to_edge(LEFT)
        
        # List of transformations with corresponding functions and labels
        transformations = [
            (lambda x: np.exp(2 * x), MathTex("f(cx) = e^{2x}"), Text("at c=2"), ORANGE),
            (lambda x: np.exp(0.5 * x), MathTex("f(cx) = e^{0.5x}"), Text("at c=0.5"), PURPLE),
            (lambda x: 2 * np.exp(x), MathTex("cf(x) = 2e^x"), Text("at c=2"), GREEN),
            (lambda x: 0.5 * np.exp(x), MathTex("cf(x) = \\frac{1}{2}e^x"), Text("at c=0.5"), RED),
            (lambda x: -np.exp(x), MathTex("cf(x) = -e^x"), Text("at c=-1"), MAROON),
            (lambda x: np.exp(-x), MathTex("f(cx) = e^{-x}"), Text("at c=-1"), PINK)
        ]

        # Adding title and axes to the scene
        self.play(Write(title, run_time=3))
        self.play(Create(axes, run_time=3))
        self.wait(2)
        
        for func, formula, c, color in transformations:
            graph = axes.plot(func, color=color)
            graph_label = formula.next_to(title, DOWN).set_color(color).shift(RIGHT*1)
            graph_label_2 = c.next_to(formula, DOWN, buff=0.5).set_color(color)
            
            # Animate the graph and formula
            self.play(Write(graph_label, run_time=2))
            self.play(Write(graph_label_2, run_time=2))
            self.play(Create(graph, run_time=4))
            
            self.wait(3)
            
            # Clear the graph and labels for the next transformation but keep the title
            self.play(FadeOut(graph, run_time=2), FadeOut(graph_label, run_time=2), FadeOut(graph_label_2, run_time=2))
        
        self.wait(2)
