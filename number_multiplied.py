from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        dot1 = Dot(np.array([-3,0,0]))
        dot2 = Dot(np.array([-1,0,0]))
        dot3 = Dot(np.array([0,0,0]))
        dot4 = Dot(np.array([2,0,0]))
        dot5 = Dot(np.array([4.7,0,0]))

        text0 = TextMobject("0")
        text0.next_to(dot1,DOWN)

        text1 = TextMobject("1")
        text1.next_to(dot2,DOWN)

        text2 = TextMobject("x").scale(1.4)
        text2.next_to(dot3,DOWN)

        text3 = TextMobject("y").scale(1.2)
        text3.next_to(dot4,DOWN)

        #x垂线
        line0 = Line(np.array([0,0,0]),np.array([0,2,0]))
        #x轴
        line1 = Line(np.array([-3,0,0]),np.array([6,0,0]),color=WHITE)
        #斜轴
        line2 = Line(np.array([-3,0,0]),np.array([6,4,0]),color= WHITE)
        #1所在的垂线
        line3 = Line(np.array([-1,0,0]),np.array([-1,1,0]))

        #y的斜线

        line4 = Line(np.array([-1.4,1,0]),np.array([4,-0.6,0]),color=BLUE)

        #交x
        line5 = line4.copy()

        text4 = TextMobject("xy")
        text4.next_to(dot5,DOWN)

        self.add(line1)
        self.wait(1)

        self.play(Write(text0))

        self.play(Write(text2))
        self.play(Write(text3))

        self.add(dot2,dot3,dot4)
        self.wait(1)

        self.play(Write(text1))
        self.add(dot1)
        self.wait(1)

        self.add(line2)
        self.wait(1)

        self.add(line3)
        self.wait(1)
        self.add(line0)
        self.play(Write(line0))
        self.wait(1)
        self.play(Write(line4))
        self.wait(1)
        self.play(ApplyMethod(line5.shift,np.array([1,0.5,0])),run_time=0.8)
        self.add(dot5)
        self.wait(1)
        self.play(Write(text4))
        self.wait(3)

