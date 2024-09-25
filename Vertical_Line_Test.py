from manim import *

class VerticalLineTest(Scene):
    def construct(self):
        # Create axes with equal aspect ratio
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        ).scale(1.5)
        axes.set_aspect_ratio(1)  # Ensure the aspect ratio is 1:1
        
        # Introduce the title
        title = Text("The Vertical Line Test!", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Define and plot a non-function (circle)
        circle_relation = axes.plot_implicit_curve(
            lambda x, y: x**2 + y**2 - 1,
            color=YELLOW
        )
        circle_label = Text("A Circle: Not a Function!", font_size=24, color=YELLOW).next_to(axes, DOWN)
        
        # Draw the circle and add label
        self.play(Create(axes))
        self.play(Create(circle_relation), Write(circle_label))
        self.wait(1)

        # Define and draw bold vertical lines for the circle
        vertical_lines_circle = VGroup()
        for x in np.linspace(-1.5, 1.5, 5):
            line = axes.get_vertical_line(axes.c2p(x, 3), color=RED, stroke_width=8)
            line.add_updater(lambda m: m.put_start_and_end_on(
                axes.c2p(x, -3),
                axes.c2p(x, 3)
            ))
            vertical_lines_circle.add(line)
            self.play(Create(line))
            self.wait(0.5)
        
        # Emphasize that this is not a function
        self.play(
            circle_label.animate.set_color(RED),
            title.animate.set_color(RED)
        )
        self.play(Flash(circle_relation, color=RED), run_time=2)
        
        # Show two outputs for one input (vertical line at x=0)
        self.play(Indicate(vertical_lines_circle[2], color=RED, scale_factor=1.5))
        output_text = Text("Two outputs for one input? Not a function!", font_size=24, color=RED)
        output_text.next_to(circle_label, DOWN)
        self.play(Write(output_text))
        self.wait(2)
        
        # Transition to a proper function
        self.play(FadeOut(circle_relation, vertical_lines_circle, circle_label, output_text))
        self.play(title.animate.set_color(WHITE))
        
        # Define and plot a function (cubic curve)
        cubic_function = axes.plot(
            lambda x: x**3,
            color=GREEN
        )
        cubic_label = Text("A Function: y = x^3", font_size=24, color=GREEN).next_to(axes, DOWN)
        
        # Draw the cubic function and add label
        self.play(Create(cubic_function), Write(cubic_label))
        self.wait(1)

        # Define and draw bold vertical lines for the cubic function
        vertical_lines_function = VGroup()
        for x in np.linspace(-1.5, 1.5, 4):
            line = axes.get_vertical_line(axes.c2p(x, 3), color=GREEN, stroke_width=8)
            line.add_updater(lambda m: m.put_start_and_end_on(
                axes.c2p(x, -3),
                axes.c2p(x, 3)
            ))
            vertical_lines_function.add(line)
            self.play(Create(line))
            self.wait(0.5)
        
        # Emphasize that this is a function
        self.play(
            cubic_label.animate.set_color(GREEN),
            title.animate.set_color(GREEN)
        )
        self.play(Flash(cubic_function, color=GREEN), run_time=2)
        
        # Show one output for each input
        self.play(Indicate(vertical_lines_function[0], color=GREEN, scale_factor=1.5))
        output_text_function = Text("One output for each input: This is a function!", font_size=24, color=GREEN)
        output_text_function.next_to(cubic_label, DOWN)
        self.play(Write(output_text_function))
        self.wait(2)
        
        # End with a playful conclusion
        conclusion = Text(
            "Remember: A function passes the vertical line test!",
            font_size=28, color=WHITE
        ).next_to(output_text_function, DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(FadeOut(cubic_function, vertical_lines_function, cubic_label, output_text_function, conclusion, title, axes))

