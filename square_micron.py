from big_ol_pile_of_manim_imports import *


class Difference(Scene):
    def construct(self):
        #建立一个对象
        rect = Polygon(np.array([-2,2,0]),np.array([-6,2,0]),np.array([-6,-2,0]),np.array([-2,-2,0]))

        # 描一个线
        line01 = Line(np.array([-6,2,0]),np.array([-2,2,0]),stroke_color='#FFFFF0',stroke_width=5,background_stroke_width=5)
        line02 = Line(np.array([-6,-2,0]),np.array([-6,2,0]))
        self.play(FadeIn(rect))
        # self.add(line01)
        
        text01 = TextMobject('a').next_to(line01,UP)
        text02 = TextMobject('a').next_to(line02,LEFT)
        self.play(Write(text01))
        self.play(Write(line01),run_time=1)

        rect1 = Polygon(np.array([-2,2,0]),np.array([-6,2,0]),np.array([-6,-2,0]),np.array([-2,-2,0]),fill_color='#2BDE73',fill_opacity=1.0)


        label=TextMobject("$ a^{2} $")
        label2 = TextMobject("$ = $")

        # label2 = TextMobject("面积一 = ")
        label.bg=SurroundingRectangle(label,color='#2BDE73',fill_opacity=0.8)
        label_group = VGroup(label.bg,label).shift(1.6 * UP + 3 * RIGHT)
        label2 = label2.shift(1.6 * UP + 2.2 * RIGHT)


        #第二个矩形
        small_rect = Polygon(np.array([-3,-2,0]),np.array([-2,-2,0]),np.array([-2,-1,0]),np.array([-3,-1,0]))
        sline01 = Line(np.array([-2,-1,0]),np.array([-2,-2,0]),color=YELLOW)
        sline02 = Line(np.array([-2,-2,0]),np.array([-3,-2,0]),color=YELLOW)
        b01 = TextMobject('b').next_to(sline01,RIGHT)
        b02 = TextMobject('b').next_to(sline02,DOWN)
    

        sline03 = Line(np.array([-2,2,0]),np.array([-2,-1,0]),color=GREEN)
        sline04 = Line(np.array([-6,-2,0]),np.array([-3,-2,0]),color=GREEN)
        a_b01 = TextMobject('a-b').next_to(sline03,RIGHT)
        a_b02 = TextMobject('a-b').next_to(sline04,DOWN)
        a_b02.set_color(PINK)
        

        #创建一个矩形背景为棕色从中间向外面显示
        small_bg = Polygon(np.array([-3,-2,0]),np.array([-2,-2,0]),np.array([-2,-1,0]),np.array([-3,-1,0]),fill_color='#3b9a9c',fill_opacity=1)


        #组合起来进行缩小
        group01 = VGroup(rect,small_bg)
        b03 = TextMobject("$ b^{2} $").shift(0.7 * UP + 3 * RIGHT)
        b04 = TextMobject("$  =  $").shift(0.7 * UP + 2.2 * RIGHT)
    
        group02 = VGroup(b03,b04)



        # 画剩余的部分
        big_rect01 = Polygon(np.array([-6,2,0]),np.array([-2,2,0]),np.array([-2,-1,0]),np.array([-3,-1,0]),np.array([-3,-2,0]),np.array([-6,-2,0]),fill_color='#3b9a9c',fill_opacity=1)
        big_rect02 = Polygon(np.array([-6,2,0]),np.array([-2,2,0]),np.array([-2,-1,0]),np.array([-3,-1,0]),np.array([-3,-2,0]),np.array([-6,-2,0]),fill_color='#3b9a9c',fill_opacity=0.3)

        #公式部分
        #b05 = TextMobject("$ A r e a   $").shift(0.8 * RIGHT + 0.4 * DOWN)
        b06 = TextMobject("$  =  $").shift(2.2 * RIGHT + 0.4 * DOWN)
        #b07 = TextMobject("$ A r e a_{1} - A r e a_{2}  $").shift(4 * RIGHT + 0.4 * DOWN)
        b08 = TextMobject("$ =  a^{2} -  b^{2}  $").shift(1 * DOWN + 3.05 * RIGHT)
        


        #旋转部分
        cut_rect = Polygon(np.array([-6,-1,0]),np.array([-3,-1,0]),np.array([-3,-2,0]),np.array([-6,-2,0]),fill_color='#fef4a9',fill_opacity=0.5)
        # cut_rect.set_color('#FF82AB')
        cut_rect01 = Polygon(np.array([-6,-1,0]),np.array([-3,-1,0]),np.array([-3,-2,0]),np.array([-6,-2,0]),fill_color='#fef4a9',fill_opacity=1)
        cut_rect.rotate(PI/2)
        bubg = Polygon(np.array([-6,-1,0]),np.array([-3,-1,0]),np.array([-3,-2,0]),np.array([-6,-2,0]),fill_color=BLACK,fill_opacity=1)

        xline01 = Line(np.array([-4,0,0]),np.array([-5,0,0]),color='#EAEAEA')
        xline02 = Line(np.array([-5,0,0]),np.array([-5,-3,0]),color='#EAEAEA')
        x01 = TextMobject('b')
        x01.set_color(GREEN)
        x02 = TextMobject('a-b')
        x02.set_color(YELLOW)
        x02.rotate(PI/2)

        x01.next_to(xline01,UP)
        x02.next_to(xline02,LEFT)

        #移到右边
        group03 = VGroup(cut_rect,xline01,xline02,x01,x02)

        #整合上面的a 和 b,在group中怎样将
        z_line = Line(np.array([-6,2,0]),np.array([-1,2,0]),color=WHITE)
        z01 = TextMobject("a + b")
        z01 = z01.next_to(z_line,UP)
        z_line01 = Line(np.array([-6,2,0]),np.array([-6,-1,0]),color=GREEN)
        z02 = TextMobject("a - b")
        z02.set_color(GREEN)
        z02.rotate(PI/2)
        z02.shift(6.5 * LEFT)
        z03 = TextMobject(" = (a+b)(a-b)").shift(1.8 * DOWN + 3.5 * RIGHT)

        #创造一个矩形
        inn = Polygon(np.array([-6,2,0]),np.array([-1,2,0]),np.array([-1,-1,0]),np.array([-6,-1,0]),fill_color='#004d61',fill_opacity=0.5,color=WHITE)
        gt = TextMobject('=')
        gt.shift(3 * DOWN)





        self.play(Write(line02))
        self.add(text02)

        self.play(
                rect1.shift,1.6 * UP + 7 * RIGHT,
                rect1.scale,0.2,
                run_time=1,

        )

        self.play(FadeIn(label_group))
        self.play(FadeIn(label2))
        self.wait(1)
        self.add(small_rect)
        self.play(Write(sline01))
        self.add(b01)

        self.play(Write(sline02))
        self.add(b02)

        self.play(Write(sline03))
        self.add(a_b01)

        self.play(Write(sline04))
        self.add(a_b02)
        self.play(GrowFromCenter(small_bg),run_time=2)
        self.wait(1)


        self.play(
                group01.shift,0.72 * UP + 7 * RIGHT,
                group01.scale,0.2,
                run_time=1,

        )
        self.add(group02)


        self.play(FadeIn(big_rect01),run_time=1)
        self.play(FadeIn(big_rect02),run_time=1)
        self.play(
            big_rect02.shift,3 * DOWN + 3 * RIGHT,
            big_rect02.scale,0.3,
            run_time = 1,
        )

        #self.play(Write(b05))
        self.play(Write(b06))
        #self.play(Write(b07))
        self.play(Write(b08))


        self.play(Write(bubg))
        self.play(
                Transform(cut_rect01,cut_rect),
                run_time=1,

        )


        #移动旋转的块
        self.play(Write(xline01))
        self.play(Write(x01))
        self.play(Write(xline02))
        self.play(Write(x02))
        self.play(
            ApplyMethod(x01.move_to,
             np.array([-2
             ,2,0])
            ),
             ApplyMethod(x02.move_to,
             np.array([-2
             ,2,0])
            ),
             ApplyMethod(xline01.move_to,
             np.array([-2
             ,2,0])
            ),
             ApplyMethod(xline02.move_to,
             np.array([-2
             ,2,0])
            ),
             ApplyMethod(cut_rect01.shift,
             3 * RIGHT + 2 * UP
            ),
             ApplyMethod(a_b01.move_to,
             np.array([-3
             ,1,0])
            ),
             ApplyMethod(
                group03.shift,3 * RIGHT + 2 * UP,
            ),            
            run_time=2
        )


        self.play(FadeOut(x01))
        self.play(FadeOut(text01))
        self.play(Write(z_line))
        self.play(Write(z01))
        self.play(FadeOut(text02))
        self.play(FadeOut(x02))
        self.play(Write(z_line01))
        self.play(Write(z02))
        self.play(GrowFromCenter(inn),run_time=1)
        self.wait(1)
        self.add(gt)
        self.play(
            inn.shift,5 * RIGHT + 3.4 * DOWN,
            inn.scale,0.35,
            run_time = 2
        )
        self.play(Write(z03))
        self.wait(2)
















