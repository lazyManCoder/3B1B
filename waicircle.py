from big_ol_pile_of_manim_imports import *  

class Shapes(Scene):
	def construct(self):
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

		
		circle = Circle(radius=2).set_color(BLUE)
		self.play(Write(circle))

		line01 = Line(np.array([-1.75,-1,0]),np.array([1.75,-1,0])).set_color(PINK)
		line02 = Line(np.array([1.75,-1,0]),np.array([0.5,1.9,0])).set_color(PINK)
		line03 = Line(np.array([0.5,1.9,0]),np.array([-1.5,1.3,0])).set_color(PINK)
		line04 = Line(np.array([-1.5,1.3,0]),np.array([-1.75,-1,0])).set_color(PINK)
		line05 = Line(np.array([-1.5,1.3,0]),np.array([1.75,-1,0])).set_color(PINK)
		line06 = Line(np.array([-1.75,-1,0]),np.array([0.5,1.9,0])).set_color(PINK)

		group08 = VGroup(line01,line02,line03,line04,line05,line06)
		dot01 = Dot(np.array([-1.75,-1,0]))
		dot02 = Dot(np.array([1.75,-1,0]))
		dot03 = Dot(np.array([0.5,1.9,0]))
		dot04 = Dot(np.array([-1.5,1.3,0]))
		dot05 = Dot(np.array([0,0,0]))

		dot06 = Dot(np.array([-1.75,1,0]))
		dot07 = Dot(np.array([1.75,1,0]))

		
		self.play(Write(line01),run_time=1.5)
		self.play(Write(line02),run_time=1.5)
		self.play(Write(line03),run_time=1.5)
		self.play(Write(line04),run_time=1.5)
		self.play(Write(line05),run_time=1.5)
		self.play(Write(line06),run_time=1.5)
		group01 = VGroup(dot01,dot02,dot03,dot05,dot04)
		self.add(group01)



		#标记
		sign01 = TextMobject('A').next_to(dot01,LEFT).set_color(YELLOW)
		sign02 = TextMobject('B').next_to(dot02,RIGHT).set_color(YELLOW)
		sign03 = TextMobject('C').next_to(dot03,RIGHT).set_color(YELLOW)
		sign04 = TextMobject('D').next_to(dot04,LEFT).set_color(YELLOW)
		sign05 = TextMobject('O').next_to(dot05,LEFT).set_color(YELLOW)
		sign06 = TextMobject('C').next_to(dot07,RIGHT).set_color(YELLOW)
		sign07 = TextMobject('D').next_to(dot06,LEFT).set_color(YELLOW)
	
		group02 = VGroup(sign01,sign02,sign03,sign04,sign05)

		self.play(Write(group02))

		#group01 = VGroup(line01,line02,line03,line04,line05,line06)
		line07 = Line(np.array([-1.75,1,0]),np.array([-1.75,-1,0])).set_color(PINK)
		line08 = Line(np.array([-1.75,1,0]),np.array([1.75,1,0])).rotate(PI).set_color(PINK)
		line09 = Line(np.array([1.75,1,0]),np.array([1.75,-1,0])).rotate(PI).set_color(PINK)

		line10 = Line(np.array([-1.75,1,0]),np.array([1.75,-1,0])).set_color(PINK)
		line11 = Line(np.array([-1.75,-1,0]),np.array([1.75,1,0])).set_color(PINK)

		group03 = VGroup(dot04,sign04)
		group04 = VGroup(dot03,sign03)

		group05 = VGroup(dot06,sign07)
		group06 = VGroup(dot07,sign06)


		group07 = VGroup(sign03,sign04,sign05,group01,group08)
		group09 = group07.copy()
		group09.set_color(BLUE).set_opacity(0.5)

		self.wait(4)
		self.add(group09)
		self.play(
			ReplacementTransform(line04,line07),
			ReplacementTransform(line03,line08),
			ReplacementTransform(line02,line09),
			ReplacementTransform(line05,line10),
			ReplacementTransform(line06,line11),
			ReplacementTransform(group03,group05),
			ReplacementTransform(group04,group06),
			run_time=2,
			)


		self.wait(6)

