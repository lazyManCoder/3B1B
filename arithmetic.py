from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
    def set_circle(self,n,color,m):
        dic = VGroup()
        for i in range(n):
            circle = Circle(radius=0.1,fill_color=color,fill_opacity=0.8).shift(i*0.3*UP+m*RIGHT).set_stroke(color,3).shift(LEFT+0.8 * UP)
            dic.add(circle)
        return dic

    def appear(self,brac,brat):
        self.play(
            GrowFromCenter(brac),
            Write(brat),
        )

    def construct(self):
        colors = ['#45d9fd', '#2BDE73', '#ee2560', '#ffd900', '#FF5A09', '#fdc4b6', '#8134af', '#41D3BD']
        text = [
            TextMobject('1').shift(LEFT),
            TextMobject(r'2').shift(0.7* LEFT),
            TextMobject(r'3').shift(0.4 * LEFT),
            TextMobject('4').shift(0.1 * LEFT),
                TextMobject('5').shift(0.2 * RIGHT),
            TextMobject('6').shift(0.5 * RIGHT),
            TextMobject('7').shift(0.8 * RIGHT),
            TextMobject('8').shift(1.1 * RIGHT),
            TextMobject('1+2+3+4+5+6+7+8'),
            TextMobject('1+2+3+4+5+6+7+8=36'),
            TextMobject(r'$9+9+\cdot \cdot \cdot +9=72$'),
            TextMobject('8+7+6+5+4+3+2+1'),
            TextMobject('1+2+3+4+5+6+7+8=?'),
        ]
        cir = VGroup()
        num = VGroup()
        text01 = TextMobject('怎样求下面的等差数列之和').shift((UP))
        group02 = VGroup(text01,text[-1])
        self.play(FadeIn(group02))
        self.wait()
        self.play(FadeOut(group02))
        for j in range(1,9):
            b01 = self.set_circle(j, colors[5], (j-1)*0.3)
            cir.add(b01)
            num.add(text[j-1])
            self.play(*[ FadeIn(i) for i in b01],FadeIn(text[j-1].scale(0.6).shift(0.5 * UP)),run_time=1.5)
        self.play(FadeOut(num))
        self.play(FadeIn(text[-5].scale(0.6).shift(0.4 * UP)))
        self.wait()
        cir01 = cir.copy().set_color(colors[0])
        self.play(
            ApplyMethod(cir01.shift,3.3 * DOWN),
        )
        self.play(cir01.rotate, -PI, run_time=2)
        self.play(Write(text[-2].scale(0.6)))
        self.wait()

        self.play(ApplyMethod(cir01.shift, 3.6 * UP))

        group01 = VGroup(text[-5], text[-2])
        group03 = VGroup(cir,cir01)
        braces01 = Brace(group03, LEFT)
        brText01 = braces01.get_text('9').scale(0.6)

        braces03 = Brace(group01, 0.5 * DOWN)
        brText03 = braces03.get_text('8个9进行相加').scale(0.8)
        self.appear(braces03,brText03)
        self.appear(braces01,brText01)
        group04 = VGroup(braces01,brText01,braces03,brText03)
        self.play(Transform(group01,text[-3].scale(0.6)))
        self.play(FadeOut(group04))
        self.play(WiggleOutThenIn(group03),WiggleOutThenIn(text[-3]),run_time=2)
        self.play(FadeIn(text[-4].shift(0.4 * DOWN).scale(0.6)))
        self.play(WiggleOutThenIn(text[-4]),WiggleOutThenIn(cir),run_time=2)
        self.wait(2)





