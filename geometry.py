from big_ol_pile_of_manim_imports import * 

class Shapes(Scene):
   def construct(self):
        #创建三个矩形
        rect01 = Square(side_length=1).rotate(PI/3).shift(2.08 * UP + 1.85 * LEFT)
        rect02 = Square(side_length=1.99).shift(0.675 * LEFT + 0.36 * UP)
        rect03 = Square(side_length=1.7).rotate(PI/3).shift(2.57 *UP)
        
        #画一个小矩形
        rect04 = Square(side_length=0.2).rotate(PI/3).shift(1.12 * LEFT + 2.1 * UP)
        rect04.set_stroke(WHITE,1)
        group01 = VGroup(rect01,rect02,rect03,rect04)

        self.play(Write(group01))

        #标记符号
        sign01 = TextMobject('$a^{2}$').set_color('#30A9DE').shift(2.2 * UP + 1.9 * LEFT)
        sign02 = TextMobject('$b^{2}$').set_color('#EFDC05').shift(2.7 * UP )
        sign03 = TextMobject('$c^{2}$').set_color('#2BDE73').shift(0.5 *UP + 0.6 * LEFT)
        group02 = VGroup(sign01,sign02,sign03)
        self.play(Write(group02))
        self.wait()
        #画直线
        line01 = DashedLine(np.array([-2.51,1.9,0]),np.array([1.18,2.9,0]))
        line02 = DashedLine(np.array([-2.51,1.9,0]),np.array([0.35,1.36,0]))
        line03 = DashedLine(np.array([-1.63,-0.55,0]),np.array([-1.16,2.2,0]))
        line04 = DashedLine(np.array([-1.16,2.2,0]),np.array([-1.16,-0.57,0]))
        self.play(FadeOut(group02))
        self.play(Write(line01))
        self.play(Write(line02))
        self.play(Write(line03))
        self.play(Write(line04))

        #创建一个三角形
        rect05 = Polygon(np.array([0,0,0]),np.array([1,0,0]),np.array([0,1,0]),fill_color='#57D1C9',fill_opacity=0.6).rotate(PI/3).shift(1.57 * UP + 2.36 * LEFT)
        rect05.set_stroke(WHITE,1)


        self.play(GrowFromCenter(rect05))

        rect06 = rect05.copy()

        rect07 = Polygon(np.array([-2.485,1.88,0]),np.array([-1.68,1.36,0]),np.array([0.35,1.36,0]),fill_color='#57D1C9',fill_opacity=0.6)


        rect08 = rect07.copy()
        self.play(Transform(rect06,rect08),run_time=2)
        
        
        rect09 = Polygon(np.array([-1.68,1.36,0]),np.array([-1.16,2.2,0]),np.array([-1.63,-0.57,0]),fill_color='#57D1C9',fill_opacity=0.6)
        rect10 = rect09.copy()
        rect10.set_stroke(WHITE,1)
        #self.play(ApplyMethod(rect))
        self.play(
            FadeOut(rect06),
            Transform(rect08,rect10),
            )

        self.wait(1.2)

        rect11 = Polygon(np.array([-1.68,1.36,0]),np.array([-1.63,-0.57,0]),np.array([-1.16,1.36,0]),fill_color='#57D1C9',fill_opacity=0.6)
        rect11.set_stroke(WHITE,1)
        self.play(Transform(rect08,rect11),run_time=2)

        rect12 = Square(side_length=1,fill_color='#57D1C9',fill_opacity=0.8).rotate(PI/3).shift(2.08 * UP + 1.85 * LEFT)
        rect12.set_stroke(WHITE,1)
        rect13 = Polygon(np.array([-1.68,1.36,0]),np.array([-1.16,1.36,0]),np.array([-1.16,-0.62,0]),np.array([-1.68,-0.62,0]),fill_color='#57D1C9',fill_opacity=0.8)
        rect13.set_stroke(WHITE,1)
        self.play(
            FadeOut(rect08),
            GrowFromCenter(rect13),
            FadeOut(rect05),
            GrowFromCenter(rect12),
            )


        rect14 = Square(side_length=1.7,fill_color='#ED5485',fill_opacity=0.8).rotate(PI/3).shift(2.57 *UP)
        
        rect14.set_stroke(WHITE,1)
        self.play(GrowFromCenter(rect14))
        self.wait()

        rect15 = rect14.copy()
        rect16 = Polygon(np.array([-1.16,-0.62,0]),np.array([-1.16,1.36,0]),np.array([0.33,1.36,0]),np.array([0.33,-0.62,0]),fill_color='#ED5485',fill_opacity=0.8)
        rect16.set_stroke(WHITE,1)
        self.play(Transform(rect15,rect16),run_time=1.5)



        group03 = VGroup(line01,line02,line03,line04)
        self.play(FadeOut(group03),run_time=2)
        self.play(FadeOut(rect04))


        group04 = VGroup(rect02,rect15,rect13,rect16)
        group05 = VGroup(rect01,rect12)
        group06 = VGroup(rect03,rect14)

        self.play(
            ApplyMethod(group05.shift, LEFT + 0.2 * UP),
            ApplyMethod(group06.shift,RIGHT + 0.2 * UP),
            ApplyMethod(group04.shift,DOWN + 0.3 * LEFT),
        )
        self.wait()
        sign01.shift(0.3 * DOWN) 
        sign02.shift(0.8 * DOWN)
        #sign03.shift(0.4 * LEFT + 0.2 * UP)
        sign03.shift( 0.4 * UP + 0.3 * RIGHT)
        sign04 = TextMobject('+').shift(LEFT + 1.8 * UP)
        #shift(LEFT + 1.2 * UP)
        sign05 = TextMobject('=').shift(LEFT + 0.8 * UP)
        group07 = group05.copy()
        group08 = group06.copy()
        group09 = group04.copy()
        self.play(
             Transform(group07,sign01),
             Transform(group08,sign02),
             Transform(group09,sign03),
             Write(sign04),
             Write(sign05),
             run_time=2,
        )
        self.wait(2)
