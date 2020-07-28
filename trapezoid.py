from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
	def construct(self):
		
		#创建梯形
		trape = Polygon(np.array([-2,2,0]),np.array([0,2,0]),np.array([1,0,0]),np.array([-2,0,0]))


		#创建小方块
		rect01 = Polygon(np.array([0,0,0]),np.array([0.2,0,0]),np.array([0.2,0.2,0]),np.array([0,0.2,0]),fill_color=GREY,fill_opacity=0.6)
		rect02 = Polygon(np.array([-2,0,0]),np.array([-1.8,0,0]),np.array([-1.8,0.2,0]),np.array([-2,0.2,0]),fill_color=GREY,fill_opacity=0.6)
		rect03 = Polygon(np.array([-2,2,0]),np.array([-1.8,2,0]),np.array([-1.8,1.8,0]),np.array([-2,1.8,0]),fill_color=GREY,fill_opacity=0.6)

		#创建对角线
		line = Line(np.array([0,2,0]),np.array([0,0,0]))
		lined = DashedLine(np.array([-2,2,0]),np.array([1,0,0]))
		linec = DashedLine(np.array([-2,0,0]),np.array([0,2,0]))

		#标记数字和线段
		lineb = Line(np.array([-2,0,0]),np.array([1,0,0]))
		linea = Line(np.array([-2,2,0]),np.array([0,2,0]))
		lineh = Line(np.array([-2,0,0]),np.array([-2,2,0]))
		lines = Line(np.array([0,2,0]),np.array([1,0,0]))
		group01 = VGroup(line,linea,lineb,linec,lined,lineh,lines)

		textb = TexMobject('b').next_to(lineb,DOWN)
		texta = TexMobject('a').next_to(linea,UP)
		textc = TexMobject('c').shift(1.5 * LEFT + UP)
		textd = TexMobject('d').shift(0.6 * LEFT + 0.8 * UP)
		texth = TexMobject('h').next_to(lineh,LEFT)
		texts = TexMobject('s').shift(0.4 * RIGHT + 0.8 * UP)
		group02 = VGroup(texta,textb,textc,textd,texth,texts)

		group03 = VGroup(trape,rect01,rect02,rect03,group01,group02)
		self.play(Write(group03))


		group04 = group03.copy()
		group04 = group04.scale(0.6)
		self.play(ApplyMethod(
			group04.shift,3 * DR,

		),run_time = 2)



		#创建h和a 以及 c为边长的矩形
		recth = Polygon(np.array([-4,2,0]),np.array([-2,2,0]),np.array([-2,0,0]),np.array([-4,0,0]),fill_color='#2BDE73',fill_opacity=0.6)
		recta = Polygon(np.array([-2,2,0]),np.array([-2,4,0]),np.array([0,4,0]),np.array([0,2,0]),fill_color='#2BDE73',fill_opacity=0.6)
		rectc = Square(side_length=2.8,fill_color='#2BDE73',fill_opacity=0.6).rotate(PI/4)
		
		

		#h^2 和a ^ 2 以及 c ^2 = a^2 + h ^ 2的标记
		a = TextMobject('$a^{2}$').shift(LEFT + 3 * UP)
		h = TextMobject('$h^{2}$').shift(3 * LEFT + UP)
		ah = TextMobject('$c^{2} = a ^ {2} + h ^ {2}$').shift(0.3 * DOWN)
		group05 = VGroup(rectc,ah)
		group06 = VGroup(recth,recta,a,h)
		rect = VGroup(recth,recta,rectc,a,h,ah)
		
		self.add(rect)
		for i in range(2):
			self.play(FadeOut(rect),run_time=2)
			self.play(FadeIn(rect),run_time=2)

		#转换成c ^2 = a^2 + h ^ 2这块
		self.play(FadeOut(textb),run_time=0.8)
		self.play(FadeOut(group06))
		self.play(FadeOut(group05))

		#创建第二次显示的矩形

		sideh = Polygon(np.array([-4,2,0]),np.array([-2,2,0]),np.array([-2,0,0]),np.array([-4,0,0]),fill_color='#00A0FF',fill_opacity=0.6)
		sided = Polygon(np.array([-2,0,0]),np.array([1,0,0]),np.array([1,-3,0]),np.array([-2,-3,0]),fill_color='#00A0FF',fill_opacity=0.6)
		sideb = Square(side_length=3.6,fill_color='#00A0FF',fill_opacity=0.6).rotate(PI / 3.2).shift(2.5 * UP + 0.43 * RIGHT).scale(0.99)
		group07 = VGroup(sideh,sided,sideb)
		


		eqa = TextMobject('$h^{2}$').shift(3 * LEFT + 1 * UP)
		eqh = TextMobject('$b^{2}$').shift(0.5 * LEFT + 1.5 * DOWN)
		eqah = TextMobject('$c^{2} = a ^ {2} + h ^ {2}$').shift(3 * UP + 0.5 * RIGHT)

		group08 = VGroup(group07,eqa,eqh,eqah)
		group09 = VGroup(sideb,eqah)
		self.add(group08)
		for i in range(2):
			self.play(FadeOut(group08),run_time=2)
			self.play(FadeIn(group08),run_time=2)

		self.play(Transform(group08,group09))
		self.wait(0.5)
		self.play(FadeOut(group08))


		#建立四个矩形
		tube01 = Square(side_length=2,fill_color='#83FFE6',fill_opacity=0.6).shift(UR)
		tube02 = tube01.copy().shift(4 * LEFT)
		tube03 = tube01.copy().shift(2 * UL)
		tube04 = Square(side_length=3,fill_color='#f2317f',fill_opacity=0.6).shift(1.5 * DOWN + 0.5 * LEFT)
		tube05 = Square(side_length=1,fill_color='#00b9f1',fill_opacity=0.6).shift(0.5 * DR)

		group10 = VGroup(tube01,tube02,tube03,tube04)

		#标记 h ^ 2 
		ea = TextMobject('$a^{2}$').shift(3 * UP + 1 * LEFT)
		eh = TextMobject('$h^{2}$').shift(3 * LEFT + 1.2 * UP)
		eh01 = TextMobject('$h^{2}$').shift(1.2 * UP + 1.2 * RIGHT)
		eb = TextMobject('$b^{2}$').shift(0.2 * LEFT + 1.6 * DOWN)
		eba = TextMobject('$(b-a)^{2}$').shift(0.6 * RIGHT + 0.4 * DOWN).scale(0.6)
		group11 = VGroup(tube05,eba)

		group12 = VGroup(group10,ea,eh,eh01,eb)

		self.play(FadeIn(group12))
		self.play(FadeIn(group11),run_time=0.6)
		group13 = VGroup(tube03,ea)
		self.play(ApplyMethod(group13.shift,5 * DOWN + 2 * LEFT),run_time=2)
		#分割块  a(b-a)  ab  从b^2
		tube06 = Polygon(np.array([-2,0,0]),np.array([0,0,0]),np.array([0,-1,0]),np.array([-2,-1,0]),fill_color='#f2317f',fill_opacity=0.6)
		tube07 = Polygon(np.array([-2,-1,0]),np.array([-2,-3,0]),np.array([1,-3,0]),np.array([1,-1,0]),fill_color='#f2317f',fill_opacity=0.6)
		
		group14 = VGroup(tube06,tube07)
		group15 = VGroup(tube04,eb)


		#写出 a(b-a)  ab
		fa = TextMobject('$a b$').shift(2 * DOWN + 0.4 * LEFT)
		fab = TextMobject('$a(b-a)$').shift(0.5 * DOWN + 0.8 * LEFT).scale(0.8)

		group16 = VGroup(fa,fab)
		
		self.play(FadeOut(group15),run_time=0.8)
		self.play(FadeIn(group14))
		self.play(Write(group16))
			

		group17 = VGroup(fab,tube06)
		self.play(ApplyMethod(group17.shift,2 * LEFT),run_time=2.2)

		tube08 = Polygon(np.array([-4,0,0]),np.array([-2,0,0]),np.array([-2,-3,0]),np.array([-4,-3,0]),fill_color='#f2317f',fill_opacity=0.6)
		gab = TextMobject('$a b$').shift(3 * LEFT + 1.2 * DOWN)

		group18 = VGroup(tube08,gab)
		group19 = VGroup(group13,group17)
		self.play(Transform(group19,group18),run_time=1.3)
		self.wait(1)
		group20 = VGroup(tube01,eh01)

		#创建一个s边长的面积
		tube09 = Square(side_length=2.2,fill_color='#83FFE6',fill_opacity=0.6).shift(1.53 * UP + 1.49 * RIGHT).rotate(PI/ 1.53)
		ss = TextMobject('$s^{2}$').shift(1.5 * RIGHT + 1.4 * UP)
		group21 = VGroup(tube09,ss)
		self.play(Transform(group20,group21),run_itme=2)
		self.wait()