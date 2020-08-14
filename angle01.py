from big_ol_pile_of_manim_imports import *

class Shapes(MovingCameraScene,Scene):
    def construct(self):
        # for i in range(160):
        #     n = 160
        #     i = 0.5 * i
        #     # x轴上的变化
        #     y = Line(np.array([-n, i, 0]), np.array([n, i, 0]))
        #     y.set_stroke(WHITE, 0.5)
        #     x1 = Line(np.array([-n, -i, 0]), np.array([n, -i, 0]))
        #     x1.set_stroke(WHITE, 0.5)
        #     x = Line(np.array([i, -n, 0]), np.array([i, n, 0]))
        #     x.set_stroke(WHITE, 0.5)
        #     y1 = Line(np.array([-i, -n, 0]), np.array([-i, n, 0]))
        #     y1.set_stroke(WHITE, 0.5)
        #     self.add(x, x1, y, y1)
        # dot = Dot(np.array([0, 0, 0]))
        # self.play(Write(dot))
        #            蓝色         绿色       红色       黄色         橙色       肉色        紫色       草绿       粉色
        colors = ['#45d9fd', '#2BDE73', '#ee2560', '#ffd900', '#FF5A09', '#fdc4b6', '#8134af', '#41D3BD','#FF307F','#fff568']

        rect01 = Square(side_length=2)
        rect02 = rect01.copy()
        rect03 =  rect01.copy()


        self.play(Write(rect01))
        self.play(
            ApplyMethod(rect02.shift,2 * LEFT),
            ApplyMethod(rect03.shift, 2 * RIGHT),
            run_time=1.5
        )
        line01 = Line(np.array([-3,1,0]),np.array([-1,-1,0]))
        line02 = Line(np.array([-3, 1, 0]), np.array([1, -1, 0]))
        line03 = Line(np.array([-3, 1, 0]), np.array([3, -1, 0]))
        group01 = VGroup(line01,line02,line03)
        self.play(Write(group01))


        arc01 = Arc(radius=0.3, arc_center=np.array([-1, -1, 0]), start_angle=135 * DEGREES, angle=45 * DEGREES).set_stroke(colors[7], 3)
        sign01 = TextMobject(r'$\alpha $').next_to(arc01,LEFT).scale(0.6).set_color(colors[0]).shift(0.05 * UP+0.2 * RIGHT)
        group02 = VGroup(arc01,sign01)
        self.play(Write(group02))



        arc02 = Arc(radius=0.3, arc_center=np.array([1, -1, 0]), start_angle=150 * DEGREES, angle=26.6 * DEGREES).set_stroke(colors[5], 3)
        sign02 = TextMobject(r'$\beta  $').next_to(arc02,LEFT).scale(0.6).set_color(colors[3])
        group03 = VGroup(arc02,sign02)
        self.play(Write(group03))

        arc03 = Arc(radius=0.3, arc_center=np.array([3, -1, 0]), start_angle=165 * DEGREES, angle=18.4* DEGREES).set_stroke(colors[5], 3)
        sign03 = TextMobject(r'$\gamma $').next_to(arc03,LEFT).scale(0.6).set_color(colors[2])
        group04 = VGroup(arc03, sign03)
        self.play(Write(group04))

        #省略文字没有进行书写

        sign18 =TextMobject(r'$\alpha  + \beta  + \gamma  = ? $').shift(1.5* UP).set_color(colors[9])
        sign19 = TextMobject('三个相同的正方形并排放置').shift(2.5 * UP).set_color(colors[9])
        self.play(Write(sign19))
        self.play(Write(sign18))
        group13 = VGroup(sign18,sign19)

        self.wait(3)
        self.play(FadeOut(group13))
        group05 = VGroup(rect01,rect02,rect03)
        group06 = group05.copy()
        self.play(ApplyMethod(
            group06.shift,2 * UP
        ))

        line04 = Line(np.array([-3,1,0]),np.array([1,3,0]))
        line05 = Line(np.array([1,3,0]),np.array([3,-1,0]))
        self.play(Write(line04))
        self.play(Write(line05))

        triangle01 = Polygon(np.array([-3,1,0]),np.array([-3,3,0]),np.array([1,3,0]),fill_color=colors[0],fill_opacity=0.8).set_stroke(WHITE,1)
        triangle02 = Polygon(np.array([1, 3, 0]), np.array([3, 3, 0]), np.array([3, -1, 0]),fill_color=colors[0],fill_opacity=0.8).set_stroke(WHITE, 1)
        triangle03 = Polygon(np.array([-3, 1, 0]), np.array([-3, -1, 0]), np.array([1, -1, 0]),fill_color=colors[0],fill_opacity=0.8).set_stroke(WHITE, 1)
        group09 = VGroup(triangle01,triangle02,triangle03)
        self.play(
            FadeIn(group09),
        )

        #留下一个抖动的特效



        arc04 = Arc(radius=0.3, arc_center=np.array([3, -1, 0]), start_angle=90 * DEGREES,angle=26.6 * DEGREES).set_stroke(colors[2], 3)
        sign04 = TextMobject(r'$\beta  $').next_to(arc04, UP).scale(0.6).set_color(colors[3]).shift(0.1 * LEFT)
        group07 = VGroup(arc04, sign04)
        self.play(Write(group07))

        arc05 = Arc(radius=0.3, arc_center=np.array([1, 3, 0]), start_angle=-150 * DEGREES,angle=-26.6 * DEGREES).set_stroke(colors[5], 3)
        sign05 = TextMobject(r'$\beta  $').next_to(arc05, LEFT).scale(0.6).set_color(colors[3]).shift(0.1 * DOWN)
        group08 = VGroup(arc05, sign05)
        self.play(Write(group08))

        sign06 = TextMobject(r'=').rotate(PI/1.5).shift(LEFT + 2 * UP)
        sign07 = TextMobject(r'=').rotate(PI/4).shift(2 * RIGHT + UP)
        self.play(Write(sign06))
        self.play(Write(sign07))

        rect04 = Square(side_length=0.2).set_stroke(WHITE,3).shift(0.9* RIGHT+2.9*UP).rotate(26.6*DEGREES, about_point=np.array([1, 3, 0]))
        self.play(Write(rect04))

        self.play(FadeOut(group09))

        triangle04 = Polygon(np.array([-3,1,0]),np.array([-3,-1,0]),np.array([-1,-1,0]),fill_color=colors[2],fill_opacity=0.8).set_stroke(WHITE,1)
        self.play(FadeIn(triangle04))

        sign08 = TextMobject(r'=').shift(3 * LEFT)
        sign09 = TextMobject(r'=').rotate(PI/2).shift(2 * LEFT + DOWN)
        rect05 = Square(side_length=0.2).set_stroke(WHITE,3).shift(0.9* DOWN+2.9*LEFT)
        group10 = VGroup(sign08,sign09)
        self.play(Write(group10))
        self.play(Write(rect05))


        triangle05 = Polygon(np.array([-3,1,0]),np.array([1,3,0]),np.array([3,-1,0]),fill_color=colors[2],fill_opacity=0.8).set_stroke(WHITE,1)
        self.play(FadeIn(triangle05))

        arc06 = Arc(radius=0.3, arc_center=np.array([3, -1, 0]), start_angle=116.6 * DEGREES,angle=45 * DEGREES).set_stroke(colors[7], 3)
        sign10 = TextMobject(r'$\alpha $').next_to(arc06, LEFT).scale(0.6).shift(0.3 * UP+ 0.2 * RIGHT).set_color(colors[0])
        group11 = VGroup(arc06, sign10)
        self.play(Write(group11))


        group12 = VGroup(triangle05,triangle04)
        self.play(FadeOut(group12))
        self.play(Write(group11))

        sign11 = sign01.copy().scale(2.5)
        sign12 = sign02.copy().scale(2.5)
        sign13 = sign03.copy().scale(2.5)
        sign14 = TextMobject(r'+').scale(1.5)
        sign15 = TextMobject(r'+').scale(1.5)
        sign16 = TextMobject(r'=').scale(1.5)
        sign17 = TextMobject(r'$90^{ \circ  }  $').scale(1.5)
        self.play(
            ApplyMethod(sign11.shift,1.5 * DOWN+0.5 * LEFT),
            ApplyMethod(sign12.shift,1.5 * DOWN+0.8 * LEFT),
            ApplyMethod(sign13.shift,1.4 * DOWN+1.4 * LEFT),
            ApplyMethod(sign14.shift, 2.2 * DOWN + 1.2 * LEFT),
            ApplyMethod(sign15.shift, 2.2 * DOWN + 0.2 * RIGHT),
            ApplyMethod(sign16.shift, 2.2 * DOWN + 1.7 * RIGHT),
            ApplyMethod(sign17.shift, 2.2 * DOWN + 2.6 * RIGHT),
        )
        self.wait(3)


