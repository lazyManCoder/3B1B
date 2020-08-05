from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
	def construct(self):
		# #坐标轴
		# for i in range(160):
		# 	n = 160
		# 	i = 0.5 * i
		# 	#x轴上的变化
		# 	y = Line(np.array([-n,i,0]),np.array([n,i,0]))
		# 	y.set_stroke(WHITE,0.5)
		# 	x1 = Line(np.array([-n,-i,0]),np.array([n,-i,0]))
		# 	x1.set_stroke(WHITE,0.5)
		# 	x = Line(np.array([i,-n,0]),np.array([i,n,0]))
		# 	x.set_stroke(WHITE,0.5)
		# 	y1 = Line(np.array([-i,-n,0]),np.array([-i,n,0]))
		# 	y1.set_stroke(WHITE,0.5)
		# 	self.add(x,x1,y,y1)
		# dot = Dot(np.array([0,0,0]))
		# self.play(Write(dot))


		color = ['#FF6666','#FFFF00','#3399CC']

		dot01 = Dot(np.array([0.5,1,0]))
		dot02 = Dot(np.array([-0.5,2,0]))
		dot03 = Dot(np.array([1,2,0]))
		dot05 = Dot(np.array([-1,1,0]))
		dot06 = Dot(np.array([2,1,0]))
		dot07 = Dot(np.array([0,3,0]))

		line01 = Line(np.array([0.5,1,0]),np.array([-1,1,0])).rotate(PI)
		#ae
		line02 = Line(np.array([1,2,0]),np.array([0,3,0]))
		line03 = Line(np.array([-0.5,2,0]),np.array([-1,1,0]))

		#所有点连成的线
		line04 = Line(np.array([0,3,0]),np.array([0.5,1,0]))
		line05 = Line(np.array([-0.5,2,0]),np.array([2,1,0]))
		line06 = Line(np.array([-1, 1, 0]), np.array([1, 2, 0]))

		sign01 = TextMobject('A').next_to(dot05,LEFT).scale(0.6)
		sign02 = TextMobject('B').next_to(dot06,RIGHT).scale(0.6)
		sign03 = TextMobject('C').next_to(dot07,UP).scale(0.6)
		sign04 = TextMobject('D').next_to(dot01,DOWN).scale(0.6)
		sign05 = TextMobject('E').next_to(dot03,RIGHT).scale(0.6)
		sign06 = TextMobject('F').next_to(dot02, LEFT).scale(0.6)

		triangle = Polygon(np.array([-1, 1, 0]), np.array([0, 3, 0]), np.array([2, 1, 0]))
		group12 = VGroup(triangle,sign01,sign02,sign03)
		self.play(FadeIn(group12))
		#怎样将直线平滑的移动到右边
		group09 = VGroup(dot01,sign04)
		self.play(FadeIn(group09))
		self.play(Write(line01))
		for i in range(1,11):
			a = 180.0 / 10
			line01.rotate(a*DEGREES,axis=IN,about_point=np.array([0.5,1,0]))
			self.wait(0.1)
		self.play(FadeOut(line01))

		group10 = VGroup(dot03, sign05)
		self.play(FadeIn(group10))
		self.play(Write(line02))
		for i in range(1,11):
			a = 180.0 / 10
			line02.rotate(a * DEGREES,axis=IN,about_point=np.array([1,2,0]))
			self.wait(0.1)
		self.play(FadeOut(line02))

		group11 = VGroup(dot02,sign06)
		self.play(FadeIn(group11))
		self.play(Write(line03))
		for i in range(1,11):
			a = 180.0 / 10
			line03.rotate(a*DEGREES,axis=IN,about_point=np.array([-0.5,2,0]))
			self.wait(0.1)
		self.play(FadeOut(line03))

		group01 = VGroup(line04,line05,line06)
		self.play(FadeIn(group01))
		self.wait()

		#交线的焦点

		dot04 = Dot(np.array([0.35,1.65,0]))
		sign07 = TextMobject('Centroid').next_to(dot04,RIGHT).scale(0.4).shift(0.5 * LEFT)
		group13 = VGroup(dot04,sign07)
		self.play(FadeIn(group13))
		#后面部分 ef   bc
		line07 = Line(np.array([1,2,0]),np.array([-0.5,2,0])).set_stroke('#79BD8F',10)
		line08 = Line(np.array([-1,1,0]),np.array([2,1,0])).set_stroke('#79BD8F',10)
		self.play(Write(line07))
		self.play(Write(line08))

		# 画左侧三角形
		#画出三角形的面积
		angle01 = Polygon(np.array([0.35,1.65,0]),np.array([-0.5,2,0]),np.array([1,2,0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,0)
		angle02 = Polygon(np.array([0.35, 1.65, 0]), np.array([-1, 1, 0]), np.array([2, 1, 0]), fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,0)
		self.play(Write(angle01),Write(angle02),run_time=1.5)
		self.wait(5)
		group02 = VGroup(angle01,angle02,line07,line08,sign07)
		self.play(FadeOut(group02))
		line09 = Line(np.array([0,3,0]),np.array([0.35,1.65,0])).set_stroke('#79BD8F',3)
		line10 = Line(np.array([-1,1,0]),np.array([0.35,1.65,0])).set_stroke('#79BD8F',3)
		line11 = Line(np.array([-0.5,2,0]),np.array([-1,1,0])).set_stroke('#79BD8F',3)
		angle03 = Polygon(np.array([0.35,1.65,0]),np.array([-0,3,0]),np.array([-1,1,0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,0)

		group03 = VGroup(line09,line10,line11,angle03)
		self.play(FadeIn(group03))
		angle04 = Polygon(np.array([0.35,1.65,0]),np.array([0,3,0]),np.array([-0.5,2,0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,0)
		angle05 = Polygon(np.array([0.35,1.65,0]),np.array([-0.5,2,0]),np.array([-1,1,0]),fill_color=color[0],fill_opacity=0.8).set_stroke(WHITE,0)
		self.play(Write(angle04))
		self.play(Write(angle05))

		#左侧进行旋转的部分
		for i in range(1,11):
			x = 85.0 / 10
			y = 95.0 / 10
			angle04.rotate(x * DEGREES, axis=OUT, about_point=np.array([-0.5, 2, 0]))
			angle05.rotate(y * DEGREES, axis=IN, about_point=np.array([-0.5, 2, 0]) )
			self.wait(0.1)
		group06 = VGroup(angle04,angle05)

		#右侧的图形
		line12 = Line(np.array([0, 3, 0]), np.array([0.35, 1.65, 0])).set_stroke('#79BD8F', 3)
		line13 = Line(np.array([2, 1, 0]), np.array([0.35, 1.65, 0])).set_stroke('#79BD8F', 3)
		line14 = Line(np.array([2, 1, 0]), np.array([0, 3, 0])).set_stroke('#79BD8F', 3)
		angle08 = Polygon(np.array([0, 3, 0]), np.array([2, 1, 0]), np.array([0.35, 1.65, 0]), fill_color=color[1],fill_opacity=0.8).set_stroke(WHITE,0)

		group04 = VGroup(line12,line13,line14,angle08)
		self.play(FadeIn(group04))

		angle06 = Polygon(np.array([0.35, 1.65, 0]), np.array([0, 3, 0]), np.array([1, 2, 0]), fill_color=color[1],fill_opacity=0.8).set_stroke(WHITE,0)
		angle07 = Polygon(np.array([0.35, 1.65, 0]), np.array([2, 1, 0]), np.array([1, 2, 0]), fill_color=color[1],fill_opacity=0.8).set_stroke(WHITE,0)

		self.play(Write(angle06))
		self.play(Write(angle07))

		for i in range(1,11):
			x = 74.0 / 10
			y = 106.0 / 10
			angle06.rotate(x * DEGREES, axis=IN, about_point=np.array([1, 2, 0]))
			angle07.rotate(y * DEGREES, axis=OUT, about_point=np.array([1, 2, 0]) )
			self.wait(0.1)

		group07 = VGroup(angle06,angle07)
		#最下面的部分
		line15 = Line(np.array([-1, 1, 0]), np.array([0.35, 1.65, 0])).set_stroke('#79BD8F', 3)
		line16 = Line(np.array([2, 1, 0]), np.array([0.35, 1.65, 0])).set_stroke('#79BD8F', 3)
		#line17 = Line(np.array([2, 1, 0]), np.array([0, 3, 0])).set_stroke('#79BD8F', 3)
		angle10 = Polygon(np.array([-1, 1, 0]), np.array([2, 1, 0]), np.array([0.35, 1.65, 0]), fill_color=color[2],fill_opacity=0.8).set_stroke(WHITE,0)

		group05 = VGroup(line15, line16,angle10)
		self.play(FadeIn(group05))

		angle11 = Polygon(np.array([0.35, 1.65, 0]), np.array([-1, 1, 0]), np.array([0.5, 1, 0]), fill_color=color[2],fill_opacity=0.8).set_stroke(WHITE, 0)
		angle12 = Polygon(np.array([0.35, 1.65, 0]), np.array([2, 1, 0]), np.array([0.5, 1, 0]), fill_color=color[2],fill_opacity=0.8).set_stroke(WHITE, 0)

		self.play(Write(angle11))
		self.play(Write(angle12))

		for i in range(1, 11):
			x = 78.0 / 10
			y = 102.0 / 10
			angle11.rotate(x * DEGREES, axis=OUT, about_point=np.array([0.5, 1, 0]))
			angle12.rotate(y * DEGREES, axis=IN, about_point=np.array([0.5, 1, 0]))
			self.wait(0.1)

		group08 = VGroup(angle11,angle12)
		self.wait(2)
		group06.scale(0.98)
		group07.scale(0.98)

		self.play(
			ApplyMethod(group06.rotate, -63 * DEGREES,axis=OUT),
		)
		self.play(
			ApplyMethod(group06.shift, 3 * DOWN + 1.5 * LEFT),
			run_time=2,
		)

		self.play(
			ApplyMethod(group07.rotate, -85 * DEGREES, axis=OUT),
		)

		self.play(
			ApplyMethod(group07.shift, 3.1 * DOWN + RIGHT),
			run_time=2,
		)

		self.play(
			ApplyMethod(group08.rotate, -56 * DEGREES, axis=OUT),

		)

		self.play(
			ApplyMethod(group08.shift, 1.4 * DOWN + 0.4 * LEFT),
			run_time=2,
		)

		for i in range(2):

			self.play(
				ApplyMethod(group06.shift,2.35 * RIGHT + 0.02 * DOWN),
				run_time=1.5,
			)

			self.play(
				ApplyMethod(group07.shift, 1.92 * LEFT + 0.02 * DOWN),
				run_time=1.5,
			)


			self.play(
				ApplyMethod(group06.shift, 2.35 * LEFT + 0.02 * UP),
				run_time=1.5,
			)

			self.play(
				ApplyMethod(group07.shift, 1.94 * RIGHT + 0.02 * UP),
				run_time=1.5,
			)

		self.wait(4)