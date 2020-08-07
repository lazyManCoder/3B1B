from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
	def construct(self):
		# 坐标轴
		# for i in range(160):
		# 	n = 160
		# 	i = 0.5 * i
		# 	# x轴上的变化
		# 	y = Line(np.array([-n, i, 0]), np.array([n, i, 0]))
		# 	y.set_stroke(WHITE, 0.5)
		# 	x1 = Line(np.array([-n, -i, 0]), np.array([n, -i, 0]))
		# 	x1.set_stroke(WHITE, 0.5)
		# 	x = Line(np.array([i, -n, 0]), np.array([i, n, 0]))
		# 	x.set_stroke(WHITE, 0.5)
		# 	y1 = Line(np.array([-i, -n, 0]), np.array([-i, n, 0]))
		# 	y1.set_stroke(WHITE, 0.5)
		# 	self.add(x, x1, y, y1)
		# dot = Dot(np.array([0, 0, 0]))
		dot03 = Dot(np.array([-1, 1, 0]))
		dot04 = Dot(np.array([2, 1, 0]))
		dot05 = Dot(np.array([0, 3, 0]))
		# self.play(Write(dot))

		sign01 = TextMobject('A').next_to(dot05,UP).scale(0.8)
		sign02 = TextMobject('B').next_to(dot03,LEFT).scale(0.8)
		sign09 = TextMobject('C').next_to(dot04, RIGHT).scale(0.8)

		sign04 = TextMobject(r'$\alpha $').shift(0.7 * LEFT+1.3* UP).scale(0.5).rotate(PI/6)
		sign10 = TextMobject(r'$\alpha $').shift(0.6 * LEFT+1.1* UP).scale(0.5)
		sign11 = TextMobject(r'$\beta $').shift(1.5 * RIGHT + 1.1 * UP).scale(0.5)
		sign12 = TextMobject(r'$\beta  $').shift(1.55 * RIGHT + 1.3 * UP).scale(0.5)



		triangle = Polygon(np.array([-1, 1, 0]), np.array([0, 3, 0]), np.array([2, 1, 0]))
		group08 = VGroup(triangle,sign01,sign02,sign09)
		self.play(Write(group08))


		#画对交线并标出角的大小
		line01 = DashedLine(np.array([-1,1,0]),np.array([2,2.83,0]))
		self.play(Write(line01))

		#组成弧
		line03 = Line(np.array([0,0,0]),np.array([0.3,0,0]))
		line04 = Line(np.array([0, 0, 0]), np.array([0, 0.3, 0])).rotate(-PI/3,about_point=np.array([0,0,0]))
		arc01 = Arc(radius=0.3,angle=PI/6)

		group01 = VGroup(line03,line04,arc01).set_color(RED).set_fill(color=RED,opacity=1).shift(UL)
		group09 = VGroup(group01,sign10)
		self.play(Write(group09))

		group02 = group01.copy().rotate(PI/6,about_point=np.array([-1,1,0]))
		group10 = VGroup(group02,sign04)
		self.play(Write(group10))

		#右边的弧
		line02 = DashedLine(np.array([2,1,0]),np.array([-1.5,2.42,0]))
		self.play(Write(line02))
		arc02 = Arc(radius=0.3,angle=PI/10)
		line05 = Line(np.array([0,0,0]),np.array([0.3,0,0]))
		line06 = Line(np.array([0, 0, 0]), np.array([0, 0.3, 0])).rotate(-PI/2.4,about_point=np.array([0,0,0]))
		group03 = VGroup(arc02,line05,line06).shift(2 * RIGHT + UP).rotate(PI/1.3,about_point=np.array([2,1,0])).set_color(RED).set_fill(color=RED,opacity=1)
		group04 = group03.copy().rotate(PI/8,about_point=np.array([2,1,0])).set_color(RED).set_fill(color=RED,opacity=1)
		group11 = VGroup(group03,sign12)
		group12 = VGroup(group04,sign11)
		self.play(Write(group11))
		self.play(Write(group12))
		self.wait()
		#显示I和ma
		# 显示出重心
		dot01 = Dot(np.array([0.2, 1.73, 0]))
		sign05 = TextMobject('I(重心)').scale(0.5)
		sign05.next_to(dot01,RIGHT)
		# ma
		group13 = VGroup(dot01,sign05)
		dot02 = Dot(np.array([0.2, 1, 0]))
		sign03 = TextMobject('$M_{A}$').scale(0.8).next_to(dot02,DOWN)
		group14 = VGroup(dot02,sign03)
		self.play(Write(group13))
		self.play(Write(group14))

		#将上面线进行消失
		group05 = VGroup(group01,line01,line02,group02,group11,group12,group09,group10)
		self.play(FadeOut(group05))



		#三个矩形标注是直角三角形  rect01 BIC   rect03 ABI   rect04 AIC
		rect01 = Square(side_length=0.2).set_stroke('#0087cb',1).shift(1.1 * UP+0.1 * RIGHT)
		rect03 = rect01.copy().shift(0.5* LEFT +0.85 *  UP).rotate(-PI/1.5)
		rect04 = rect01.copy().shift(0.65 * RIGHT + 1* UP).rotate(PI/1.35)

		rect05 = rect01.copy()
		rect06 = rect03.copy()
		rect07 = rect04.copy()

		line12 = DashedLine(np.array([0.2, 1.73, 0]), np.array([0.2, 1, 0]))
		sign13 = TextMobject('r').scale(0.5).next_to(line12, RIGHT).shift(0.1 * LEFT)
		group15 = VGroup(line12,sign13,rect01)
		circle = Circle(radius=0.72).shift(1.73 * UP+0.2 * RIGHT)
		self.play(Write(group15))
		self.play(Write(circle))


		#动态绘制圆的过程
		#连接三边的垂线段

		dot06 = Dot([0.7,2.25,0])
		dot07 = Dot([-0.48,2.08,0])
		sign14 = TextMobject('$M_{B}$').scale(0.8).next_to(dot06,RIGHT)
		sign15 = TextMobject('$M_{C}$').scale(0.8).next_to(dot07,LEFT)
		group16 = VGroup(dot06,dot07,sign14,sign15)
		self.play(Write(group16))


		line10 = DashedLine(np.array([0.2, 1.73, 0]),np.array([0.7,2.25,0]))
		line11 = DashedLine(np.array([0.2, 1.73, 0]),np.array([-0.48,2.08,0]))
		sign22 = TextMobject('r').scale(0.5).next_to(line10,UP).shift(0.3 * DOWN)
		sign23 = TextMobject('r').scale(0.5).next_to(line11,UP).shift(0.3 * DOWN)
		group22 = VGroup(line10,sign22,rect04)
		group23 = VGroup(line11,sign23,rect03)
		self.play(
			Write(group22),
			Write(group23),
		)

		# #连接A B C
		color = ['bce672', '44cef6', 'faff72']
		line07 = Line(np.array([0.2,1.73,0]),np.array([0,3,0])).set_stroke(color[0],6)
		line08 = Line(np.array([0.2,1.73,0]),np.array([-1,1,0])).set_stroke(color[1],6)
		line09 = Line(np.array([0.2,1.73,0]),np.array([2,1,0])).set_stroke(color[2],6)
		group06 = VGroup(line07,line08,line09)
		self.play(Write(group06))

		#显示角没有做，等下做
		arc03 = Arc(radius=0.3,angle=PI/3)
		line13 = Line(np.array([0,0,0]),np.array([0.3,0,0]))
		line14 = Line(np.array([0,0,0]),np.array([0,0.3,0])).rotate(-PI/6,about_point=np.array([0,0,0]))
		group17 = VGroup(arc03,line13,line14).set_color(RED).rotate(-PI/1.63,about_point=np.array([0,0,0])).shift(3 * UP)
		sign20 = TextMobject(r'$\gamma $').scale(0.5).shift(2.5 * UP + 0.1 * LEFT)
		sign21 = TextMobject(r'$\gamma $').scale(0.5).shift(2.5 * UP + 0.2 * RIGHT)
		group21 = VGroup(sign20,sign21,group17)
		self.play(Write(group21))


		#让角度一起再次显示
		arc04 = Arc(radius=0.3, angle=PI / 3)
		line15 = Line(np.array([0, 0, 0]), np.array([0.3, 0, 0]))
		line16 = Line(np.array([0, 0, 0]), np.array([0, 0.3, 0])).rotate(-PI / 6, about_point=np.array([0, 0, 0]))
		group17 = VGroup(arc04, line16, line15).set_color(RED).shift(UL)
		sign16 = TextMobject(r'$\alpha $').shift(0.7 * LEFT + 1.3 * UP).scale(0.5).rotate(PI / 6)
		sign17 = TextMobject(r'$\alpha $').shift(0.6 * LEFT + 1.1 * UP).scale(0.5)
		group19 = VGroup(sign16,sign17,group17)
		self.play(Write(group19))

		arc05 = Arc(radius=0.3, angle=PI / 4)
		line17 = Line(np.array([0, 0, 0]), np.array([0.3, 0, 0]))
		line18 = Line(np.array([0, 0, 0]), np.array([0, 0.3, 0])).rotate(-PI / 4, about_point=np.array([0, 0, 0]))
		group18 = VGroup(arc05, line17, line18).set_color(RED).rotate(PI / 1.3, about_point=np.array([0, 0, 0])).shift(2 * RIGHT + UP)
		sign18 = TextMobject(r'$\beta $').shift(1.5 * RIGHT + 1.1 * UP).scale(0.5)
		sign19 = TextMobject(r'$\beta  $').shift(1.55 * RIGHT + 1.3 * UP).scale(0.5)
		group20 = VGroup(sign18,sign19,group18)
		self.play(Write(group20))
		#第一个出现定义的界面
		self.wait(5)

		#ABI     BIC    AIC
		angle01 = Polygon(np.array([-1,1,0]),np.array([0.2,1.73,0]),np.array([0,3,0]),fill_color=color[0],fill_opacity=0.8).set_stroke(color[0],2)
		angle02 = Polygon(np.array([-1, 1, 0]), np.array([0.2, 1.73, 0]), np.array([2, 1, 0]),fill_color=color[1],fill_opacity=0.8).set_stroke(color[1],2)
		angle03 = Polygon(np.array([0, 3, 0]), np.array([0.2, 1.73, 0]), np.array([2, 1, 0]),fill_color=color[2],fill_opacity=0.8).set_stroke(color[2],2)

		#将mc转换成c依次进行


		self.play(Write(angle01))
		sign24 = TextMobject('c').next_to(triangle,LEFT).scale(0.8).shift(0.3 * RIGHT)
		self.play(Transform(sign15,sign24))
		self.play(Write(angle03))
		sign25 = TextMobject('b').next_to(triangle,RIGHT).scale(0.8).shift(0.9 * LEFT)
		self.play(Transform(sign14, sign25))
		self.play(Write(angle02))
		sign26 = TextMobject('a').next_to(triangle,DOWN).scale(0.8)
		self.play(Transform(sign03, sign26))



		#三角形开始进行旋转，先复制
		group24 = VGroup(angle01,group23,rect06)
		group25 = VGroup(angle02,group15,rect05)
		group26 = VGroup(angle03,group22,rect07)
		angle04 =group24.copy()
		angle05 = group25.copy()
		angle06 = group26.copy()
		# angle04 = angle01.copy()
		# angle05 = angle02.copy()
		# angle06 = angle03.copy()
		self.play(Write(angle04))


		for i in range(1, 11):
			x = 117.0 / 10
			angle04.rotate(x * DEGREES, axis=OUT, about_point=np.array([-1, 1, 0]))
			self.wait(0.1)

		#往下面移动 然后消失变成公式  公式部分省略
		self.play(ApplyMethod(
			angle04.shift,DOWN,
		),run_time=1.5)

		angle07 = angle04.copy()
		sign06 = TextMobject(r'$A_{1}  = \frac{1}{2}cr  $').shift(0.5 * DOWN + 0.3 * RIGHT)

		self.play(
			ApplyMethod(angle07.shift,2 * DOWN  +   RIGHT),
			Transform(angle07,sign06),
			run_time=2
		)
		self.wait()
		self.play(FadeOut(angle07))


		self.play(Write(angle06))
		for i in range(1,11):
			y = 135.0 / 10
			angle06.rotate(y * DEGREES, axis=IN, about_point=np.array([2, 1, 0]))
			self.wait(0.1)

		self.play(ApplyMethod(
			angle06.shift, DOWN,
		), run_time=1.5)

		angle08 = angle06.copy()
		sign07 = TextMobject(r'$A_{2}  = \frac{1}{2}br  $').shift(0.5 * DOWN + 0.3 * RIGHT)

		self.play(
			ApplyMethod(angle08.shift, 2 * DOWN +  RIGHT),
			Transform(angle08, sign07),
			run_time=2
		)
		self.wait()
		self.play(FadeOut(angle08))

		self.play(ApplyMethod(
			angle05.shift, DOWN,
		), run_time=1.5)

		angle09 = angle05.copy()
		sign08 = TextMobject(r'$A_{3}  = \frac{1}{2}cr  $').shift(0.5 * DOWN + 0.3 * RIGHT)

		self.play(
			ApplyMethod(angle09.shift, 2 * DOWN + 0.3 * RIGHT ),
			Transform(angle09, sign08),
			run_time=2
		)
		self.wait()
		self.play(FadeOut(angle09))

		#进行停止来写公式
		self.wait(4)

		#将三个三角形进行消失
		group07 = VGroup(angle04,angle05,angle06)
		self.play(FadeOut(group07))

		#这边要写公式，要进行暂停时间



		#旋转三角形拼接成矩形 移动到右边
		#CIM
		angle10 = Polygon(np.array([0.2, 1.73, 0]), np.array([0.7, 2.25, 0]), np.array([2, 1, 0]))
		self.play(Write(angle10))
		angle11 = Polygon(np.array([0.2, 1.73, 0]), np.array([2, 1.73, 0]), np.array([2, 1, 0]),fill_color=color[2],fill_opacity=0.8).set_stroke(WHITE,1)
		self.play(Transform(angle10,angle11))
		angle18 =  Polygon(np.array([0.2, 1.73, 0]), np.array([0.2,1,0]), np.array([2, 1, 0]),fill_color=color[1],fill_opacity=0.8).set_stroke(WHITE,1)
		group27 = VGroup(angle10,angle18)
		self.play(ApplyMethod(
			group27.shift,1.5 * DOWN + 0.3 * RIGHT,
		),run_time=2)


		angle12 = Polygon(np.array([-0.48, 2.08, 0]), np.array([0.2, 1.73, 0]), np.array([-1, 1, 0]))
		angle13 = Polygon(np.array([-1,1.73,0]), np.array([0.2, 1.73, 0]), np.array([-1, 1, 0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,1)
		self.play(Write(angle12))
		self.play(Transform(angle12, angle13))
		angle19 =Polygon(np.array([-1,1,0]), np.array([0.2, 1, 0]), np.array([0.2, 1.73, 0]),fill_color=color[1],fill_opacity=0.8).set_stroke(WHITE,1)
		group28 = VGroup(angle12,angle19)

		self.play(ApplyMethod(
			group28.shift, 1.5 * DOWN + 0.3 * RIGHT,
		), run_time=2)
		angle14 = Polygon(np.array([-0.48,2.08, 0]), np.array([0, 3, 0]), np.array([0.2, 1.73, 0]))
		angle15 = Polygon(np.array([-1.1, 3, 0]), np.array([0, 3, 0]), np.array([-1.1, 2.27, 0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,1)
		self.play(Write(angle14))
		self.play(Transform(angle14, angle15))
		angle16 = Polygon(np.array([0.7,2.25, 0]), np.array([0, 3, 0]), np.array([0.2, 1.73, 0]))
		angle17 = Polygon(np.array([-1.1,2.27, 0]), np.array([0, 2.27, 0]), np.array([0, 3, 0]),fill_color=color[2],fill_opacity=0.8).set_stroke(WHITE,1)
		self.play(Write(angle16))
		self.play(Transform(angle16, angle17))
		group29 = VGroup(angle14,angle16)
		self.play(ApplyMethod(
			group29.shift, 2.78 * DOWN + 0.7 * LEFT,
		), run_time=2)
        #进行写入公式  然后结束
		self.wait(5)