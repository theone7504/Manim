from manim import *

class matrixTest(Scene):
    def construct(self):
        A = np.array([[-1, 5], [7, 11]])
        B = np.array([[2, 3], [-8, 0]])
        C = np.dot(A, B)

        matrixA = Matrix(A)
        matrixB = Matrix(B)
        matrixC = Matrix(C)
        
        matrixA.height = 2.5
        matrixB.height = 2.5
        matrixA.set_color(PURPLE)
        matrixB.set_color(RED)
        
        cross = Tex("*", color=WHITE, font_size=200)
        Equals = Tex("=", color=WHITE, font_size=100)
        
        self.play(Write(matrixA))
        self.play(matrixA.animate.to_corner(UP).to_edge(LEFT))
        cross.next_to(matrixA, RIGHT)
        self.play(Write(cross))
        self.play(Write(matrixB))
        self.play(matrixB.animate.next_to(cross, RIGHT))
        Equals.next_to(matrixB, RIGHT)
        self.play(Write(Equals))
        matrixC.next_to(Equals)
        self.play(Write(matrixC))
        
        C_elements = VGroup(*matrixC.get_entries())
        A_rows = matrixA.get_rows()
        B_columns = matrixB.get_columns()

        for r, c, ans in zip(
            [A_rows[0], A_rows[0], A_rows[1], A_rows[1]],
            [B_columns[0], B_columns[1], B_columns[0], B_columns[1]],
            C_elements,
        ):
            _bOpen = Tex("[", color=WHITE, font_size=100)
            _bClose = Tex("]", color=WHITE, font_size=100)
            _bOpen1 = Tex("[", color=WHITE, font_size=200)
            _bClose1 = Tex("]", color=WHITE, font_size=200)
            _Dot = Tex(".", color=WHITE, font_size=200)
            _r = r.copy().set_color(BLUE)
            _c = c.copy().set_color(YELLOW)

            _bOpen.next_to(matrixA, DOWN * 3)
            self.play(Write(_bOpen))
            self.play(_r.animate.next_to(_bOpen))
            _bClose.next_to(_r, RIGHT)
            self.play(Write(_bClose))
            _Dot.next_to(_bClose, RIGHT)
            self.play(Write(_Dot))
            _bOpen1.next_to(_Dot, RIGHT)
            self.play(Write(_bOpen1))
            self.play(_c.animate.next_to(_bOpen1))
            _bClose1.next_to(_c, RIGHT)
            self.play(Write(_bClose1))
            
            g = VGroup(_bOpen, _r, _bClose, _Dot, _bOpen1, _c, _bClose1)
            ans.font_size = 60
            ans.set_color(PURE_GREEN)
            self.play(Transform(g, ans))

        self.wait()
