from manim import *

class GeometricSolution(Scene):
    def construct(self):
        equation = MathTex("x^2", "+", "26x", "=", "27")
        equation.set_color_by_tex("x^2", BLUE)
        equation.set_color_by_tex("26x", GREEN)
        equation.set_color_by_tex("27", RED)
        self.play(Write(equation), run_time=2)
        self.play(equation.animate.to_edge(UP), run_time=1.5)

        Blue = Square(1, fill_color=BLUE, fill_opacity=1)
        blue_label = MathTex("x")
        self.play(DrawBorderThenFill(Blue))
        self.play(Blue.animate.shift(2 * LEFT + UP))
        blue_label.next_to(Blue, UP)
        self.play(Write(blue_label))

        plus_sign = MathTex("+")
        plus_sign.next_to(Blue, RIGHT, buff=0.5)
        self.play(Write(plus_sign))

        Green = Rectangle(width=1, height=0.5, fill_color=GREEN, fill_opacity=1, stroke_color=WHITE)
        green_label_width = MathTex("26")
        green_label_height = MathTex("x")
        self.play(DrawBorderThenFill(Green))
        self.play(Green.animate.next_to(plus_sign, RIGHT))
        green_label_width.next_to(Green, UP)
        green_label_height.next_to(Green, RIGHT)
        self.play(Write(green_label_height), Write(green_label_width))

        equal = MathTex("=")
        equal.next_to(green_label_height, RIGHT)
        self.play(Write(equal))

        Red = Square(1.5, fill_color=RED, fill_opacity=1)
        red_label = MathTex("27")
        self.play(DrawBorderThenFill(Red))
        self.play(Red.animate.next_to(equal, RIGHT))
        red_label.move_to(Red)
        self.play(Write(red_label))

        self.wait(2)



        #this script is yet to be finished