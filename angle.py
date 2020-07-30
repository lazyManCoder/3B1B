from big_ol_pile_of_manim_imports import *


class Shapes(Scene):
	def construct(self):
		#三角形
		angle01 = Polygon(np.array([0,0,0]),np.array([1.7,0,0]),np.array([0,1,0]),fill_color='#8134af',fill_opacity=0.8).rotate(PI/2).rotate(PI/1.5).shift(LEFT).scale(1.5)
		#小矩形
		rect01 = Square(side_length=0.2).rotate(PI/6).shift(1.43 * UP + 0.55 * RIGHT)
		rect01.set_stroke(WHITE,1)
		self.play(Write(angle01))
		self.play(Write(rect01))
		group01 = VGroup(angle01,rect01)

		sign01 = TextMobject('a').next_to(angle01,RIGHT)
		sign02 = TextMobject('b').next_to(angle01,LEFT)
		sign03 = TextMobject('c').next_to(angle01,DOWN)
		self.play(Write(sign01))
		self.play(Write(sign02))
		self.play(Write(sign03))
		group02 = VGroup(sign01,sign02,sign03)


		self.wait(1.5)
		angle01 = group01.scale(2)
		sign04 = TextMobject('a x c').next_to(angle01,RIGHT)
		sign05 = TextMobject('b x c').next_to(angle01,0.3 *LEFT)
		sign06 = TextMobject('c x c').next_to(angle01,DOWN)
		
		group03 = VGroup(sign04,sign05,sign06)

		group04 = VGroup(angle01,group03)

		self.play(
			FadeOut(group02),
			Write(group04),
			run_time=3,
			)

		sign07 = TextMobject('ac').shift(2.2 * RIGHT + 1.3 * UP)
		sign08 = TextMobject('bc').shift(1.7 * LEFT + 1.3 * UP)
		sign09 = TextMobject('$c^{2}$').next_to(angle01,DOWN)
		group05 = VGroup(sign07,sign08,sign09)
		self.play(Transform(group03,group05))

		#画一个三角形
		angle02 = Polygon(np.array([-0.21,0.98,0]),np.array([0.381,0.98,0]),np.array([0.381,-0.038,0]),fill_color=BLUE,fill_opacity=0.8).scale(2.5).shift(0.5 * UP + 1.98 * RIGHT)
		#小矩形
		rect02 = Square(side_length=0.2).shift(2.7 * RIGHT + 2.12 * UP)
		rect02.set_stroke(WHITE,1)
		group06 = VGroup(angle02,rect02)
		self.play(Write(group06))
	


		sign10 = TextMobject('ab').next_to(angle02,RIGHT)
		sign11 = TextMobject('$a^{2}$').next_to(angle02,UP)

		self.play(Write(sign10))
		self.play(Write(sign11))

		#左上的三角形
		angle03 = Polygon(np.array([-1.85,-0.2,0]),np.array([-1.85,0.83,0]),np.array([-0.062,0.83,0]),fill_color=BLUE,fill_opacity=0.8).scale(2.5).shift(0.64 * UP)
		rect03 = Square(side_length=0.5).shift(2.93 * LEFT + 2 * UP)
		rect03.set_stroke(WHITE,1)
		group07 = VGroup(rect03,angle03)

		self.play(Write(group07))



		sign12 = TextMobject('ba').next_to(angle03,LEFT)
		sign13 = TextMobject('$b^{2}$').next_to(angle03,UP)
		self.play(Write(sign12))
		self.play(Write(sign13))


		line01 = Line(np.array([-3.2,0,0]),np.array([1.3,0,0]),fill_color='#dd2a7b').shift(2.25 * UP)
		line01.set_stroke('#fad3cf',10)
		self.play(Write(line01))
		line02 = Line(np.array([1.3,0,0]),np.array([2.83,0,0]),fill_color='#dd2a7b').shift(2.25 * UP)
		line02.set_stroke('#a696c8',10)
		self.play(Write(line02))


		line03 = Line(np.array([-3.2,0,0]),np.array([2.83,0,0]),fill_color='#dd2a7b').shift(0.352 * DOWN)
		line03.set_stroke('#2470a0',10)
		self.play(Write(line03))

		#整体上移
		group08 = VGroup(group01,group03,group06,group07,sign10,sign11,sign12,sign13,line01,line02,line03)
		self.play(ApplyMethod(group08.shift,UP),run_time=2)

		sign14 = sign11.copy()
		sign15 = sign13.copy()
		sign16 = sign09.copy()
		sign17 = TextMobject('+').scale(2).shift( DOWN + 1.7 * LEFT)
		sign18 = TextMobject('=').scale(2).shift( DOWN + 0.8 * RIGHT)
		sign14.set_color('#a696c8').scale(2)
		sign15.set_color('#fad3cf').scale(2)
		sign16.set_color('#2470a0').scale(2)
		self.play(
			ApplyMethod(sign14.shift,4.7 * DOWN +  5 * LEFT),
			ApplyMethod(sign15.shift,4.7* DOWN + 0.5 * RIGHT),
			ApplyMethod(sign16.shift,0.2 * DOWN + 2 * RIGHT),
			
			run_time = 2,
		)
		self.play(Write(sign17),
			Write(sign18),
			run_time=2,
			)
		self.wait()