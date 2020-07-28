
import math
from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
	def construct(self):

		#出现一个三角行
		triangle = Polygon(np.array([-2,0,0]),np.array([0,2,0]),np.array([2,0,0]))
		self.add(triangle)

		#描绘直线
		line01 = Line(np.array([-2,0,0]),np.array([0,2,0]),color=BLUE)
		self.play(Write(line01),run_time=0.2)
		sidec = TextMobject('c').shift(1.5* LEFT + UP)
		self.play(Write(sidec))

		line02 = Line(np.array([2,0,0]),np.array([0,2,0]),color=BLUE)
		self.play(Write(line02),run_time=0.2)
		sidec01 = TextMobject('c').shift(1.5* RIGHT + UP)
		self.play(Write(sidec01))


		line03 = Line(np.array([-2,0,0]),np.array([-1,0,0]),color=YELLOW)
		self.play(Write(line03),run_time=0.2)
		sideb = TextMobject('b').next_to(line03,DOWN)
		self.play(Write(sideb))


		line04 = Line(np.array([-1,0,0]),np.array([2,0,0]),color=RED)
		self.play(Write(line04),run_time=0.2)
		sided = TextMobject('d').next_to(line04,UP)
		self.play(Write(sided))



		line05 = Line(np.array([0,2,0]),np.array([-1,0,0]),color=YELLOW)
		self.play(Write(line05),run_time=0.2)
		sidea = TextMobject('a').shift(0.3 * LEFT + UP)
		self.play(Write(sidea))
		

		#绘制c边的正方形
		csquare = Square(side_length=3,color=GREY,fill_opacity=0.6).rotate(PI / 4).scale(0.93).shift(2 * LEFT + 2 * UP)
		self.add(csquare)
		self.wait(2)



		#c的平方
		sidecc = TextMobject('$c^{2}$',color=WHITE).shift(2 * LEFT + 2.2 * UP)
		self.play(FadeOut(sidec))
		self.play(Write(sidecc))

		#a的矩形
		asquare = Square(side_length=2,color=GREEN,fill_opacity=0.6).rotate(PI / 2.8).scale(1.1).shift(1.5 * LEFT + 1.48 * UP)

		self.play(GrowFromCenter(asquare),run_time=0.5)
		self.wait(1)

		#a的平方
		sideca = TextMobject('$a^{2}$',color=WHITE).shift(1.2 * LEFT + 1.5 * UP)
		self.play(Write(sideca))



		#往下的直线b
		lineb = Line(np.array([-1,0,0]),np.array([-1,-1,0]))
		self.play(Write(lineb))


		#一个灰色的小矩形
		small = Polygon(np.array([-1,0,0]),np.array([-1,-0.2,0]),np.array([-1.2,-0.2,0]),np.array([-1.2,0,0]),fill_color=GREY,fill_opacity=1)
		self.play(Write(small))
		#直线b
		sidecb = TextMobject('b',color=WHITE).shift(1.2 * LEFT + DOWN)
		self.play(Write(sidecb))
		

		#绘制bd
		bdarea = Polygon(np.array([-1,0,0]),np.array([-1,-1,0]),np.array([2,-1,0]),np.array([2,0,0]),fill_color='#f5587b',fill_opacity=0.3)
		self.play(Write(bdarea))

		#bd直线
		bdline = TextMobject('bd',color=WHITE).shift(0.5 * DOWN + 0.7 * RIGHT)
		self.play(Write(bdline))
		

		group02 = VGroup(triangle,line01,line02,sidec01,line03,sideb,line04,sided,line05,sidea,csquare,sidecc,asquare,sideca,lineb,small,sidecb,bdarea,bdline)

		group03 = group02.copy()
		group03 = group03.scale(0.6)

		self.play(
			ApplyMethod(
				group03.shift, 4.5 * RIGHT + 1.2 * DOWN,
				),
			ApplyMethod(
			
				group02.shift, 2.5 * LEFT + 0.1 * UP,
				),

			run_time = 2
		)
		

		#任意等腰三角形中：c ^ 2 = a ^ 2 + bd

		formula = TextMobject('$c ^ 2 = a ^ 2 + bd$',color=WHITE).shift(3 * DOWN + 4 * RIGHT)
		self.play(Write(formula))

		line06 = Line(np.array([-2.3,-3.5,0]),np.array([2.5,-3.5,0]))
		self.play(Write(line06))

		word = TextMobject('任意等腰三角形中：').shift(3 * DOWN,0.2 * RIGHT)
		self.play(Write(word))

		group04 = VGroup(bdarea,sidecb,lineb,bdline,small)
		
		self.play(FadeOut(group04))

		#垂线
		line07 = DashedLine(np.array([0,2,0]),np.array([0,0,0])).shift(2.5 * LEFT + 0.1 * UP)
		h = TextMobject('h').next_to(line07,RIGHT)


		#开始确定若隐若现的位置
		small_rect = Polygon(np.array([-0.2,0,0]),np.array([-0.2,0.2,0]),np.array([0,0.2,0]),np.array([0,0,0]),fill_color=GREEN,fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		xline = Line(np.array([-1,0,0]),np.array([0,0,0]),color=WHITE).shift(2.5 * LEFT + 0.1 * UP)
		x = TextMobject('x').next_to(xline,DOWN)
		
		group05 = VGroup(line07,h,small_rect,xline,x)
		self.play(FadeOut(sidea))
		self.add(group05)



		#整出x ^ 2 和 h ^ 2
		group06 = VGroup(x,h)
		x2 = Polygon(np.array([-1,0,0]),np.array([0,0,0]),np.array([0,-1,0]),np.array([-1,-1,0]),fill_color=GREEN,fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		h2 = Polygon(np.array([0,0,0]),np.array([2,0,0]),np.array([2,2,0]),np.array([0,2,0]),fill_color=GREEN,fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		
		xs2 = TextMobject('$x^2$').shift(3 * LEFT +0.2 * DOWN)
		hs2 = TextMobject('$h^2$').shift(1.5 * LEFT + UP)

		group07 = VGroup(x2,h2,xs2,hs2)
		
		self.play(FadeOut(group06))
		self.play(Write(group07))
		group08 = VGroup(group07,asquare,sideca)
		for i in range(2):
			self.play(FadeOut(group08))
			self.play(FadeIn(group08))

		group09 = VGroup(asquare,sideca)

		self.play(Transform(group08,group09),run_time=1.2)

		#公式的模块
		chunk01 = Polygon(np.array([0,0,0]),np.array([-2,0,0]),np.array([-2,-2,0]),np.array([0,-2,0]),fill_color='#41b6e6',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		#formula01 = TextMobject()


		h02 = Polygon(np.array([0,0,0]),np.array([2,0,0]),np.array([2,2,0]),np.array([0,2,0]),fill_color=GREEN,fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		hs02 = TextMobject('$h^2$').shift(1.5 * LEFT + UP)

		group10 = VGroup(chunk01,h02,hs02)
		self.play(FadeIn(group10))
		group11 = VGroup(group10,csquare,sidecc)
		group12 = VGroup(sidecc,csquare)

		for i in range(3):
			self.play(FadeOut(group11))
			self.play(FadeIn(group11))

		self.play(Transform(group11,group12),run_time=1.2)

		chunk02 = Polygon(np.array([0,0,0]),np.array([-2,0,0]),np.array([-2,-2,0]),np.array([0,-2,0]),fill_color='#41b6e6',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		x2 = Polygon(np.array([-1,0,0]),np.array([0,0,0]),np.array([0,-1,0]),np.array([-1,-1,0]),fill_color='#ff585d',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		group13 = VGroup(chunk02,x2)
		self.play(Write(group13))



		#梯形
		trap01 = Polygon(np.array([-1,0,0]),np.array([-2,0,0]),np.array([-2,-2,0]),np.array([-1,-1,0]),fill_color='#ffb549',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		trap02 = Polygon(np.array([-1,-1,0]),np.array([-2,-2,0]),np.array([0,-2,0]),np.array([0,-1,0]),fill_color='#ffb549',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		trap = VGroup(trap01,trap02)
		self.play(Transform(group13,trap),run_time=1.2)


		trap03 = Polygon(np.array([-1,0,0]),np.array([-1,-1,0]),np.array([1,-1,0]),np.array([0,0,0]),fill_color='#ffb549',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		trap04 = Polygon(np.array([0,0,0]),np.array([2,0,0]),np.array([2,-1,0]),np.array([1,-1,0]),fill_color='#ffb549',fill_opacity=0.3).shift(2.5 * LEFT + 0.1 * UP)
		trap05 = VGroup(trap03,trap04)
		
		
		
		self.play(Transform(trap,trap05),run_time=2)
		self.play(FadeOut(group13))
		bdline = bdline.shift(0.2 * LEFT)
		sidecb = sidecb.shift(0.2 * UP)
		group14 = VGroup(small_rect,bdline,sidecb)
		self.play(Write(group14))
	
		self.wait(2)











