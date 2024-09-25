from manim import *
import numpy as np
import math

class RiemannIntegral(Scene):
    def construct(self):
        # Setup axes
        ax = Axes(
            x_range=[-2, 6, 1],
            y_range=[0, 2, 0.5],
            axis_config={"include_tip": False, "numbers_to_exclude": [-2, 6]}
        ).add_coordinates()

        self.play(Create(ax))
        
        def get_riemann_rects(graph, dx=0.2):
            return ax.get_riemann_rectangles(
                graph, x_range=[0, 5], dx=dx, input_sample_type="right"
            )

        
        graph1 = ax.plot(lambda x: 0.1 * (x - 2) ** 2 + 1, color=BLUE)
        self.play(Create(graph1))
        
        label1 = MathTex(r"(x-2)^2+1").to_edge(UP).scale(1.3)
        self.play(FadeIn(label1))
        
        rects = VGroup()
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = get_riemann_rects(graph1, dx)
            rects.add(rect)
        
        self.play(Create(rects[0]))
        for i in range(1, len(rects)):
            self.play(Transform(rects[0], rects[i]), run_time=0.5)
        self.wait(1)

        
        graph2 = ax.plot(lambda x: (-1 * (x - 3) ** 3 + 3 * (x - 3) + 3) / 15, color=GREEN)
        self.play(Transform(graph1, graph2))
        
        label2 = MathTex(r"-(x-3)^3 + 3(x-3) + 3").to_edge(UP).scale(1.3)
        self.play(Transform(label1, label2))
        
        rects2 = VGroup()
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = get_riemann_rects(graph2, dx)
            rects2.add(rect)
        
        self.play(Transform(rects[0], rects2[0]))
        for i in range(1, len(rects2)):
            self.play(Transform(rects[0], rects2[i]), run_time=0.5)
        self.wait(1)

        graph3 = ax.plot(lambda x: (math.sin(x / 1.5) + 1) / 2, color=RED)
        self.play(Transform(graph1, graph3))
        
        label3 = MathTex(r"\sin(\frac{x}{1.5})+1").to_edge(UP).scale(1.3)
        self.play(Transform(label1, label3))
        
        rects3 = VGroup()
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = get_riemann_rects(graph3, dx)
            rects3.add(rect)
        
        self.play(Transform(rects[0], rects3[0]))
        for i in range(1, len(rects3)):
            self.play(Transform(rects[0], rects3[i]), run_time=0.5)
        self.wait(1)

        graph4 = ax.plot(lambda x: x / 10 + 1, color=ORANGE)
        self.play(Transform(graph1, graph4))
        
        label4 = MathTex(r"\frac{x}{10}+1").to_edge(UP).scale(1.3)
        self.play(Transform(label1, label4))
        
        rects4 = VGroup()
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = get_riemann_rects(graph4, dx)
            rects4.add(rect)
        
        self.play(Transform(rects[0], rects4[0]))
        for i in range(1, len(rects4)):
            self.play(Transform(rects[0], rects4[i]), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(rects[0]), FadeOut(label1), FadeOut(graph1), FadeOut(ax))
