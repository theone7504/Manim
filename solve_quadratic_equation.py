from manim import *

class SolveQuadraticEquation(Scene):
    def construct(self):
        # Title
        title = Text("Solving the equation:", font_size=36)
        equation = MathTex("x^2 + 26x = 27", font_size=36)
        equation.next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(equation))
        self.wait(1)
        self.play(VGroup(title, equation).animate.to_edge(UP))

        # Step 1: Rewrite the equation in standard form
        step1 = Text("Step 1: Rewrite the equation in standard form", font_size=28)
        step1.shift(2 * UP)
        self.play(Write(step1))

        eq1 = MathTex("x^2 + 26x - 27 = 0", font_size=36)
        eq1.next_to(step1, DOWN, buff=0.5)
        self.play(Write(eq1))
        self.wait(2)

        # Step 2: Factor the quadratic equation
        self.play(FadeOut(step1))
        step2 = Text("Step 2: Factor the quadratic equation", font_size=28)
        step2.shift(2 * UP)
        self.play(Write(step2))

        eq2 = MathTex("(x + 27)(x - 1) = 0", font_size=36)
        eq2.next_to(step2, DOWN, buff=0.5)
        self.play(Transform(eq1, eq2))
        self.wait(2)

        # Step 3: Set each factor to zero
        self.play(FadeOut(step2))
        step3 = Text("Step 3: Set each factor to zero", font_size=28)
        step3.shift(2 * UP)
        self.play(Write(step3))

        eq3 = MathTex("x + 27 = 0 \\quad \\text{or} \\quad x - 1 = 0", font_size=36)
        eq3.next_to(step3, DOWN, buff=0.5)
        self.play(Transform(eq1, eq3))
        self.wait(2)

        # Step 4: Solve each equation
        self.play(FadeOut(step3))
        step4 = Text("Step 4: Solve each equation", font_size=28)
        step4.shift(2 * UP)
        self.play(Write(step4))

        eq4 = MathTex("x = -27 \\quad \\text{or} \\quad x = 1", font_size=36)
        eq4.next_to(step4, DOWN, buff=0.5)
        self.play(Transform(eq1, eq4))
        self.wait(2)

        # Final result
        self.play(FadeOut(step4), FadeOut(eq1))
        final_result = Text("The solutions are x = -27 and x = 1", font_size=36)
        final_result.shift(UP)
        self.play(Write(final_result))
        self.wait(2)

