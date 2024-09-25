from manim import *

class RandomFunctionGraph(Scene):
    def construct(self):
       
        axes = Axes(
            x_range=[-10, 10, 0.5],
            y_range=[-10, 10, 0.5],
            axis_config={"color": BLUE}
        ).shift(DOWN * 1).shift(LEFT*2)

        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

    
        def random_function(x):
            return 0.1 * x**3 - x**2 + 2 * x + 1

      
        graph = axes.plot(random_function, color=GREEN)

        
        input_value = 8
        output_value = random_function(input_value)
        input_dot = Dot(axes.c2p(input_value, 0), color=RED)
        output_dot = Dot(axes.c2p(input_value, output_value), color=YELLOW)

        input_line = DashedLine(axes.c2p(input_value, 0), axes.c2p(input_value, output_value), color=RED)
        output_line = DashedLine(axes.c2p(0, output_value), axes.c2p(input_value, output_value), color=YELLOW)

        input_label = MathTex(f"x = {input_value}").next_to(input_dot, DOWN)
        output_label = MathTex(f"f(x) = {output_value:.2f}").next_to(output_dot, RIGHT)

        function_text = MathTex("f(x) = y = 0.1x^3 - x^2 + 2x + 1").to_edge(UP)


        self.play(Create(axes), Write(labels))
        self.play(Write(function_text))
        self.play(Create(graph), run_time=2)
        self.play(Create(input_dot), Write(input_label))
        self.play(Create(output_dot), Write(output_label))
        self.play(Create(input_line), Create(output_line))
        self.wait(2)
