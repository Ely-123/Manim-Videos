from manim import *


# Escena que muestra la primera parte del video
class Scen0(Scene):
    def construct(self):
        variables = (
            VGroup(MathTex("A"), MathTex("R"), MathTex("r"), MathTex("d"))
            .arrange_submobjects()
            .shift(UP)
        )

        f1 = MathTex("4").scale(1.3)
        f2 = MathTex("4=1+1+1+1").scale(1.3).next_to(f1, DOWN).shift([0, 2, 0])
        f3 = MathTex("4=2+1+1").scale(1.3).next_to(f2, DOWN)
        f4 = MathTex("4=2+2").scale(1.3).next_to(f3, DOWN)
        f5 = MathTex("4=3+1").scale(1.3).next_to(f4, DOWN)
        f6 = MathTex("4=4").scale(1.3).next_to(f5, DOWN)
        f7 = MathTex("p(4)=5").scale(1.3)
        f8 = MathTex("p(n)=?").scale(1.3).next_to(f7, DOWN)

        self.play(Write(f1))
        self.wait(2)
        self.play(Uncreate(f1))
        self.play(Write(f2))
        self.play(Write(f3))
        self.play(Write(f4))
        self.play(Write(f5))
        self.play(Write(f6))
        # se eliminan las particionwe
        self.play(
            Uncreate(f6),
            Uncreate(f5),
            Uncreate(f4),
            Uncreate(f3),
            Uncreate(f2),
            Uncreate(f1),
        )
        self.wait(1)
        self.play(Write(f7))
        self.wait(5)
        self.play(Write(f8))

        self.wait(5)