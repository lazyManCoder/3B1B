from big_ol_pile_of_manim_imports import *  

class Shapes(Scene):
	

	def construct(self):
		#创建三个矩形
		
		rect01 = Square(side_length=1,fill_color='#ffee93',fill_opacity=1).rotate(PI/3).shift(2.08 * UP + 1.85 * LEFT)
		rect02 = Square(side_length=1.99,fill_color='#50C1E9',fill_opacity=1).shift(0.675 * LEFT + 0.36 * UP)
		rect03 = Square(side_length=1.7,fill_color='#7A57D1',fill_opacity=1).rotate(PI/3).shift(2.57 *UP)

		group01 = VGroup(rect01,rect02,rect03).shift(DOWN)
		self.play(Write(group01))


		line01 = DashedLine(np.array([0,0,0]),np.array([1.78,0,0])).rotate(PI/3).shift(2.46*UP + 2.5* LEFT)
		line02 = DashedLine(np.array([0,0,0]),np.array([1,0,0])).rotate(PI/1.2).shift(3*UP + 1.25* LEFT)
		line03 = DashedLine(np.array([0,1,0]),np.array([0,2.85,0])).shift(0.32 * UP + 1.15* LEFT)
		self.play(Write(line01))
		self.play(Write(line02))
		self.play(Write(line03))
	

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

		#复制原先得矩形
		angle01 = Square(side_length=1,fill_color='#ffee93',fill_opacity=0.6).rotate(PI/3).shift(1.08 * UP + 1.85 * LEFT)
		angle02 = Square(side_length=1.99,fill_color='#50C1E9',fill_opacity=0.6).shift(0.675 * LEFT + 0.64 * DOWN)
		angle03 = Square(side_length=1.7,fill_color='#7A57D1',fill_opacity=0.6).rotate(PI/3).shift(1.57 *UP)

		self.add(angle01,angle02,angle03)

		#要转变得三角形
		rect05 = Polygon(np.array([-1.165,1.27,0]),np.array([-1.165,3.27,0]),np.array([-1.68,2.35,0]),np.array([-1.68,0.38,0]),fill_color='#ffee93',fill_opacity=1)
		#rect05 = Polygon(np.array([-1.68,2.35,0]),np.array([-1.68,0.38,0]),np.array([-1.16,1.27,0]),np.array([-1.16,3.27,0]),fill_color='#ffee93',fill_opacity=1)
		
		rect05.set_stroke(WHITE,1)
		rect06 = Polygon(np.array([-1.15,1.27,0]),np.array([-1.15,3.25,0]),np.array([0.3,2.4,0]),np.array([0.3,0.4,0]),fill_color='#7A57D1',fill_opacity=0.6)
		rect06.set_stroke(WHITE,1)


		self.play(Transform(angle01,rect05),run_time=2)
		self.play(FadeOut(line03))
		self.play(Transform(angle03,rect06),run_time=2)


		group02 = VGroup(rect05,rect06)
		
		self.play(ApplyMethod(group02.shift,2.02 * DOWN),run_time=2)
		self.play(FadeOut(angle01),FadeOut(angle03),FadeOut(line01),FadeOut(line02))
		self.wait(1.2)

		#变换成最后成型得矩形
		rect07 = Polygon(np.array([-1.7,0.38,0]),np.array([-1.15,0.38,0]),np.array([-1.15,-1.65,0]),np.array([-1.7,-1.65,0]),fill_color='#ffee93',fill_opacity=1)
		rect07.set_stroke(WHITE,1)


		rect08 = Polygon(np.array([-1.15,0.38,0]),np.array([-1.15,-1.65,0]),np.array([0.35,-1.65,0]),np.array([0.35,0.38,0]),fill_color='#7A57D1',fill_opacity=1)
		rect08.set_stroke(WHITE,1)
		self.wait()
		group03 = VGroup(rect07,rect08).rotate(PI * 2)

		self.play(Transform(group02,group03),run_time=2)
		self.wait()



