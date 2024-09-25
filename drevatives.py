from manim import *

class Derivatives(Scene):
    def construct(self):
        # Create axes with labels
        axes = (
            Axes(
                x_range=[0, 10, 1],
                x_length=9,
                y_range=[0, 20, 5],
                y_length=6,
                axis_config={"include_numbers": True, "include_tip": False}
            ).to_edge(DL).set_color(GREY)
        )
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Define the function
        func = axes.plot(
            lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0, 10], color=BLUE
        )
        
        # Value trackers
        x = ValueTracker(7)
        dx = ValueTracker(2)
        
        # Secant line group
        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="dy",
                secant_line_color=GREEN,
                secant_line_length=8,
            )
        )
        
        # Dots
        dot1 = always_redraw(
            lambda: Dot(color=RED).scale(0.7).move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot(color=RED).scale(0.7).move_to(axes.c2p(x.get_value() + dx.get_value(), func.underlying_function(x.get_value() + dx.get_value())))
        )

        # Add elements to the scene with animations
        self.play(FadeIn(axes), Write(axis_labels))
        self.play(Create(func))
        self.play(Create(VGroup(dot1, dot2, secant)))
        
        # Animate dx decreasing
        self.play(dx.animate.set_value(0.001), run_time=10, rate_func=smooth)
        self.wait(2)
        
        # Animate x moving to 0.5
        self.play(x.animate.set_value(0.5), run_time=5, rate_func=smooth)
        self.wait(2)
        
        # Animate dx increasing back
        self.play(dx.animate.set_value(2), run_time=5, rate_func=smooth)
        self.wait(2)
        
        # Animate x moving to 8
        self.play(x.animate.set_value(8), run_time=5, rate_func=smooth)
        self.wait(5)
        
        # Fade out everything at the end
        self.play(FadeOut(VGroup(axes, axis_labels, func, dot1, dot2, secant)))
        self.wait(2)

