from big_ol_pile_of_manim_imports import *
from numpy import *

class Homework(Scene):

    def setup(self):
        self.A = np.array([1, 0, 0])
        self.B = np.array([-1, 0, 0])
        self.C = np.array([-0.3, 1.3, 0])

        self.main_tri = Polygon(
            self.A, self.B, self.C,
            color=BLUE, fill_color=BLUE, fill_opacity=0.8
        )

        label_a = TexMobject("a").scale(0.7).next_to((self.B+self.C)/2, UL, buff=0.08)
        label_b = TexMobject("b").scale(0.7).next_to((self.A+self.C)/2, UR, buff=0.08)
        label_c = TexMobject("c").scale(0.7).next_to((self.B+self.A)/2, DOWN, buff=0.08)
        self.labels = VGroup(label_a, label_b, label_c)

        sq_a = Polygon(self.B, self.C, np.array([-1.6, 2, 0]), np.array([-2.3, 0.7, 0]), color=WHITE)
        sq_b = Polygon(self.C, self.A, np.array([2.3, 1.3, 0]), np.array([1, 2.6, 0]), color=WHITE)
        sq_c = Polygon(self.A, self.B, np.array([-1, -2, 0]), np.array([1, -2, 0]), color=WHITE)
        self.sq = VGroup(sq_a, sq_b, sq_c)

        tri_a = Polygon(self.A, np.array([1, -2, 0]), np.array([2.3, 1.3, 0]), color=RED, fill_color=RED, fill_opacity=0.8)
        tri_b = Polygon(self.B, np.array([-2.3, 0.7, 0]), np.array([-1, -2, 0]), color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        tri_c = Polygon(self.C, np.array([1, 2.6, 0]), np.array([-1.6, 2, 0]), color='#2BDE73', fill_color='#2BDE73', fill_opacity=0.8)
        self.tri = VGroup(tri_a, tri_b, tri_c)

        equation = TexMobject("S_{\\ } = S_{\\ } = S_{\\ } = S_{\\ }").to_corner(2 * DOWN, buff=1.1)
        tri_1 = self.main_tri.copy().set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][0], RIGHT+DOWN*3, buff=-0.08)
        tri_2 = tri_a.copy().rotate(PI/2).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][2], RIGHT+DOWN*3, buff=-0.08)
        tri_3 = tri_b.copy().rotate(PI/2, axis=IN).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][4], RIGHT+DOWN*3, buff=-0.08)
        tri_4 = tri_c.copy().rotate(PI/4, axis=IN).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][6], RIGHT+DOWN*3, buff=-0.08)
        self.equation = VGroup(equation, tri_1, tri_2, tri_3, tri_4)


    def construct(self):
        self.wait(0.5)
        self.play(ShowCreation(self.main_tri))
        self.play(FadeIn(self.labels))
        self.play(*[ShowCreation(i) for i in self.sq], run_time=1.5)
        self.play(*[ShowCreation(i) for i in self.tri], run_time=1.5)
        self.play(
            *[
                WiggleOutThenIn(i)
                for i in self.tri
            ], run_time=1.5
        )
        self.wait()
        self.play(
            FadeOut(self.sq),
            Rotating(self.tri[0], radians=PI/2, about_point=self.A),
            Rotating(self.tri[1], radians=PI/2, about_point=self.B),
            Rotating(self.tri[2], radians=PI/2, about_point=self.C),
            run_time=1.5
        )
        self.wait()
        self.play(
            self.main_tri.shift, UP,
            self.tri.shift, UP,
            self.labels.shift,UP,
        )


        self.play(
            WiggleOutThenIn(self.tri[0]),
            WiggleOutThenIn(self.main_tri)
        )
        self.play(
            FadeIn(self.equation[0][0][:3]),
            TransformFromCopy(self.main_tri, self.equation[1]),
            TransformFromCopy(self.tri[0], self.equation[2]),
            run_time=1.5
        )

        self.play(
            WiggleOutThenIn(self.tri[1]),
            WiggleOutThenIn(self.main_tri)
        )
        equation_copy_1 = self.equation[1].copy()
        equation_copy_2 = self.equation[1].copy()
        self.play(
            FadeIn(self.equation[0][0][3:5]),
            TransformFromCopy(self.main_tri, equation_copy_1),
            TransformFromCopy(self.tri[1], self.equation[3]),
            run_time=1.5
        )

        self.play(
            WiggleOutThenIn(self.tri[2]),
            WiggleOutThenIn(self.main_tri)
        )
        self.play(
            FadeIn(self.equation[0][0][5:]),
            TransformFromCopy(self.main_tri, equation_copy_2),
            TransformFromCopy(self.tri[2], self.equation[4]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(FadeOut(VGroup(self.equation[0][0][:2], self.equation[1], equation_copy_1, equation_copy_2)))
        self.equation[0][0][:2].set_opacity(0)
        self.equation[1].set_fill(opacity=0)
        self.equation.generate_target()


        #表达式的位置
        self.equation.target.scale(1.3).shift(0.2* DOWN+LEFT)
        self.play(MoveToTarget(self.equation))

        self.play(Write(self.equation[0][0][:2]))
        self.play(Write(self.equation[1]))
        self.wait(1.5)
