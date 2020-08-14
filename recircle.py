from big_ol_pile_of_manim_imports import *

class Shapes(MovingCameraScene,Scene):
    def construct(self):


        #               蓝      黄           红       紫         橙
        colors = ['#30A9DE','#EFDC05','#E53A40','#2BDE73','#f2317f']
        circle01 = Circle(radius=0.5,fill_color=colors[0],fill_opacity=1).set_stroke(colors[0],2)

        #第一层
        self.play(FadeInFromLarge(circle01))
        self.play(ApplyMethod(circle01.shift, DL))

        self.wait(1.5)
        #第二层
        circle02 = Circle(radius=0.5, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle01,UP)
        circle03 = Circle(radius=0.5, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle01,RIGHT)
        circle04 = Circle(radius=0.5, fill_color=colors[1], fill_opacity=1).set_stroke(colors[0], 2).next_to(circle01,UR)
        group01 = VGroup(circle02,circle03,circle04)
        self.play(FadeIn(group01))
        self.wait(2)
        #第三层

        group02 = group01.copy().next_to(circle01,UR).set_color(colors[2])
        circle04 = group02[0].copy().shift(1.25*LEFT)
        circle05 = group02[1].copy().shift(1.25 * DOWN)
        group03 = VGroup(group02,circle04,circle05)
        self.play(FadeIn(group03))
        self.wait(2)
        #第四层
        group04 = group03.copy().next_to(circle01,UR).set_color(colors[3])
        circle06 = group02[0].copy().shift(1.25 * LEFT+1.25 * UP).set_color(colors[3])
        circle07 = group02[1].copy().shift(1.25 * DOWN +1.25*RIGHT).set_color(colors[3])
        group05 = VGroup(group04,circle06,circle07)
        self.play(FadeIn(group05))
        group07 = VGroup(circle01,group01,group03,group05)
        self.play(ApplyMethod(group07.shift,DL))
        self.wait(2)

        #第五层
        group06 = group05.copy().next_to(circle01, UR).set_color(colors[4])
        circle08 = group02[0].copy().shift(1.25 * LEFT + 2.5 * UP).set_color(colors[4])
        circle09 = group02[1].copy().shift(1.25 * DOWN + 2.5 * RIGHT).set_color(colors[4])
        group08 = VGroup(group06,circle08,circle09)
        self.play(FadeIn(group08))
        group13 = VGroup(group08,group07)
        self.wait(2)

        braces01 = Brace(circle01, LEFT)
        brText01 = braces01.get_text('1')
        braces02 = Brace(circle01, DOWN)
        brText02 = braces02.get_text('1')
        self.play(
            GrowFromCenter(braces01),
            Write(brText01),
            GrowFromCenter(braces02),
            Write(brText02)
        )
        group09 = VGroup(braces01,brText01,braces02,brText02)
        self.wait(2)
        self.play(FadeOut(group09))


        braces03 = Brace(group01, LEFT)
        brText03 = braces03.get_text('2')
        braces04 = Brace(group01, DOWN)
        brText04 = braces04.get_text('2')
        self.play(
            GrowFromCenter(braces03),
            Write(brText03),
            GrowFromCenter(braces04),
            Write(brText04)
        )
        group10 = VGroup(braces03, brText03, braces04, brText04)
        self.wait(2)
        self.play(FadeOut(group10))


        braces05 = Brace(group03, LEFT)
        brText05 = braces05.get_text('3')
        braces06 = Brace(group03, DOWN)
        brText06 = braces06.get_text('3')
        self.play(
            GrowFromCenter(braces05),
            Write(brText05),
            GrowFromCenter(braces06),
            Write(brText06)
        )
        group11 = VGroup(braces05, brText05, braces06, brText06)
        self.wait(2)
        self.play(FadeOut(group11))

        braces07 = Brace(group07, LEFT)
        brText07 = braces07.get_text('4')
        braces08 = Brace(group07, DOWN)
        brText08 = braces08.get_text('4')
        self.play(
            GrowFromCenter(braces07),
            Write(brText07),
            GrowFromCenter(braces08),
            Write(brText08)
        )
        group12 = VGroup(braces07, brText07, braces08, brText08)
        self.wait(2)
        self.play(FadeOut(group12))

        braces09 = Brace(group13, LEFT)
        brText09 = braces09.get_text('5')
        braces10 = Brace(group13, DOWN)
        brText10 = braces10.get_text('5')
        self.play(
            GrowFromCenter(braces09),
            Write(brText09),
            GrowFromCenter(braces10),
            Write(brText10)
        )
        #group14 = VGroup(braces09, brText09, braces10, brText10)

        self.wait(4)
