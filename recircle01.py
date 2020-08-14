from big_ol_pile_of_manim_imports import *

class Shapes(MovingCameraScene,Scene):
    def construct(self):


        #             蓝        黄          红        紫         橙
        colors = ['#30A9DE','#EFDC05','#E53A40','#2BDE73','#f2317f','#fff1b9']
        circle01 = Circle(radius=0.3,fill_color=colors[0],fill_opacity=1).set_stroke(colors[0],2)
        circle10 = Circle(radius=0.3,fill_color=colors[0],fill_opacity=1).set_stroke(colors[0],2).next_to(circle01,UP)

        #第一层
        group14 = VGroup(circle10,circle01)
        self.play(FadeInFromLarge(group14))

        text = [
            TextMobject(r'$2 = 1\times 2$').shift(3.3*DOWN),
            TextMobject(r'$2+4=2\times 3$').shift(3.3*DOWN),
            TextMobject(r'$2+4+6=3\times 4$').shift(3.3 * DOWN),
            TextMobject(r'$2+4+6+8=4\times 5$').shift(3.3* DOWN),
            TextMobject(r'$2+4+6+8+10=5\times 6$').shift(3.3*DOWN),
            TextMobject(r'$2+4+6+\cdot \cdot \cdot +2n = n(n+1)$').shift(3.3 * DOWN)
        ]

        text01 = [
            TextMobject(r'偶数求和').shift(2.5*DOWN).set_color(colors[5], 10),
            TextMobject(r'n=1').shift(2.7*DOWN).set_color(colors[5],3),
            TextMobject(r'n=2').shift(2.7 * DOWN).set_color(colors[5],3),
            TextMobject(r'n=3').shift(2.7 * DOWN).set_color(colors[5],3),
            TextMobject(r'n=4').shift(2.7 * DOWN).set_color(colors[5],3),
            TextMobject(r'n=5').shift(2.7 * DOWN).set_color(colors[5],3),
            TextMobject(r'n=n').shift(2.7 * DOWN).set_color(colors[5], 3)

        ]
        self.play(Write(text01[0]))
        self.wait(1.5)



        #第二层
        circle02 = Circle(radius=0.3, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle10,UP)
        circle03 = Circle(radius=0.3, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle10,RIGHT)
        circle04 = Circle(radius=0.3, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle10,UR)
        circle11 = Circle(radius=0.3, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle01,RIGHT)
        group01 = VGroup(circle02,circle03,circle04,circle11)
        self.play(FadeIn(group01))
        group15 = VGroup(group14,group01)
        self.play(ApplyMethod(
            group15.shift,0.5* DL,
        ),run_time=1.2)


        #第三层
        group02 = group01.copy().next_to(circle01,UR).set_color(colors[2])
        circle04 = group02[0].copy().shift(0.85*LEFT)
        circle05 = group02[1].copy().shift(1.7 * DOWN)

        group03 = VGroup(group02,circle04,circle05)
        self.play(FadeIn(group03))
        group16 = VGroup(group15,group03)
        self.play(ApplyMethod(
            group16.shift, 0.3 * DL,
        ), run_time=1.2)



        #第四层
        group04 = group03.copy().next_to(circle01,UR).set_color(colors[3])
        circle06 = group02[0].copy().shift(0.85 * LEFT+0.85 * UP).set_color(colors[3])
        circle07 = group02[1].copy().shift(1.7 * DOWN +0.85*RIGHT).set_color(colors[3])
        circle13 = group02[2].copy().shift(1.7 * DOWN + 0.85*RIGHT).set_color(colors[3])
        group05 = VGroup(group04,circle06,circle07,circle13)
        self.play(FadeIn(group05))
        group07 = VGroup(circle01,group01,group03,group05,circle10)

        self.play(ApplyMethod(group07.shift,0.3 * DOWN + 0.4 * LEFT))


        #第五层
        group06 = group05.copy().next_to(circle01, UR).set_color(colors[4])
        circle08 = group02[0].copy().shift(0.85 * LEFT + 1.7 * UP).set_color(colors[4])
        circle09 = group02[1].copy().shift(1.7 * DOWN + 1.7 * RIGHT).set_color(colors[4])

        group08 = VGroup(group06,circle08,circle09)
        self.play(FadeIn(group08))
        group13 = VGroup(group08,group07)
        group17 = VGroup(group13,group07)
        self.play(ApplyMethod(group17.shift, 0.1 * UP + 0.4 * LEFT),run_time=1.2)
        self.play(FadeOut(text01[0]))

        braces01 = Brace(group14, LEFT)
        brText01 = braces01.get_text('2')
        braces02 = Brace(circle01, DOWN)
        brText02 = braces02.get_text('1')
        self.play(Write(text01[1]))
        self.play(
            GrowFromCenter(braces01),
            Write(brText01),
            GrowFromCenter(braces02),
            Write(brText02)
        )
        group09 = VGroup(braces01,brText01,braces02,brText02)
        self.play(Write(text[0]))
        self.wait(2)
        self.play(FadeOut(group09))
        group18 = VGroup(text[0],text01[1])
        self.play(FadeOut(group18))


        braces03 = Brace(group01, LEFT)
        brText03 = braces03.get_text('3')
        braces04 = Brace(group01, DOWN)
        brText04 = braces04.get_text('2')
        self.play(Write(text01[2]))
        self.play(
            GrowFromCenter(braces03),
            Write(brText03),
            GrowFromCenter(braces04),
            Write(brText04)
        )
        group10 = VGroup(braces03, brText03, braces04, brText04)
        self.play(Write(text[1]))
        self.wait(2)
        self.play(FadeOut(group10))
        group19 = VGroup(text[1],text01[2])
        self.play(FadeOut(group19))


        braces05 = Brace(group03, LEFT)
        brText05 = braces05.get_text('4')
        braces06 = Brace(group03, DOWN)
        brText06 = braces06.get_text('3')
        self.play(Write(text01[3]))
        self.play(
            GrowFromCenter(braces05),
            Write(brText05),
            GrowFromCenter(braces06),
            Write(brText06)
        )
        group11 = VGroup(braces05, brText05, braces06, brText06)
        self.play(Write(text[2]))
        self.wait(2)
        self.play(FadeOut(group11))
        group20 = VGroup(text[2],text01[3])
        self.play(FadeOut(group20))


        braces07 = Brace(group07, LEFT)
        brText07 = braces07.get_text('5')
        braces08 = Brace(group07, DOWN)
        brText08 = braces08.get_text('4')
        self.play(Write(text01[4]))
        self.play(
            GrowFromCenter(braces07),
            Write(brText07),
            GrowFromCenter(braces08),
            Write(brText08)
        )
        group12 = VGroup(braces07, brText07, braces08, brText08)

        self.play(Write(text[3]))
        self.wait(2)
        self.play(FadeOut(group12))
        group21 = VGroup(text[3],text01[4])
        self.play(FadeOut(group21))

        braces09 = Brace(group13, LEFT)
        brText09 = braces09.get_text('6')
        braces10 = Brace(group13, DOWN)
        brText10 = braces10.get_text('5')
        self.play(Write(text01[5]))
        self.play(
            GrowFromCenter(braces09),
            Write(brText09),
            GrowFromCenter(braces10),
            Write(brText10)
        )
        #group14 = VGroup(braces09, brText09, braces10, brText10)
        self.play(Write(text[4]))
        self.wait(2)
        group22 = VGroup(text[4],text01[5])
        self.play(FadeOut(group22))
        self.wait(2)

        group23 = VGroup(text[5],text01[6])
        self.play(Transform(group22,group23))
        self.wait(4)
