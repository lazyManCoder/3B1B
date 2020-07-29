from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
	def construct(self):
		#创建矩形
		#边长为2的矩形
		rect01 = Polygon(np.array([-2,2,0]),np.array([-2,4,0]),np.array([0,4,0]),np.array([0,2,0]))
		#边长为1的矩形
		rect02 = Polygon(np.array([0,2,0]),np.array([0,3,0]),np.array([1,3,0]),np.array([1,2,0]))
		
		#组合两个矩形
		group01 = VGroup(rect01,rect02)
		self.play(Write(group01))

		#标记a b的位置
		sign01 = TextMobject("a").next_to(rect01,LEFT)
		sign02 = TextMobject("b").next_to(rect02,UP)
		group02 = VGroup(sign01,sign02)

		#一起显示
		self.play(Write(group02))

		#第三个矩形
		rect03 = Polygon(np.array([0,4,0]),np.array([-2,3,0]),np.array([-1,1,0]),np.array([1,2,0]))
		self.play(Write(rect03))

		sign03 = TextMobject("c").shift(1.3 * UP + 0.2 * RIGHT)
		self.play(Write(sign03))

		#创建颜色，画多边形
		#左上的三角形
		rect04 = Polygon(np.array([-2,4,0]),np.array([-2,3,0]),np.array([0,4,0]),fill_color='#41b6e6',fill_opacity=0.6)
		rect04.set_stroke('#41b6e6',2)
		#左下的三角形
		rect05 = Polygon(np.array([-2,2,0]),np.array([-2,3,0]),np.array([-1.5,2,0]),fill_color='#41b6e6',fill_opacity=0.6)
		rect05.set_stroke('#41b6e6',2)
		#将两个三角形组合起来，目的是为了，添加颜色
		group03 = VGroup(rect04,rect05)
		self.play(FadeIn(group03))

		#左边的矩形，目的重叠颜色
		rect06 =  Polygon(np.array([-2,2,0]),np.array([-2,4,0]),np.array([0,4,0]),np.array([0,2,0]),fill_color='#ff585d',fill_opacity=0.6)
		self.play(FadeIn(rect06))

	
		#最右边的小三角形
		rect07 = Polygon(np.array([1.03,2,0]),np.array([0.5,3.01,0]),np.array([1.03,3.01,0]),fill_color='#e59572',fill_opacity=0.6)
		rect07.set_stroke('#41b6e6',2)
		#右边的小矩形，目的是为了重新涂上颜色
		rect08 = Polygon(np.array([0,2,0]),np.array([0,3,0]),np.array([1,3,0]),np.array([1,2,0]),fill_color='#2694ab',fill_opacity=0.6)
		self.play(FadeIn(rect07))
		self.play(FadeIn(rect08))

		#开始转移 最上边的三角，也是最大的三角
		rect09 = rect04.copy()
		self.play(ApplyMethod(rect09.shift,2 * DOWN + RIGHT),run_time=2)

		#b旁边的三角移动到左下的三角
		#rect10 = rect07.copy()
		rect10 = Polygon(np.array([1,2,0]),np.array([0.49,3.01,0]),np.array([1,3.01,0]),fill_color='#e59572',fill_opacity=0.6).set_stroke('#41b6e6',2)
		
		
		self.play(ApplyMethod(rect10.shift,2 * LEFT + DOWN),run_time=2)


		#移动到b旁边的三角
		rect11 = rect05.copy()
		self.play(ApplyMethod(rect11.shift,2 * RIGHT + UP),run_time=2)

		#左边不规则的图形
		rect12 = Polygon(np.array([-2,3,0]),np.array([-1.5,2,0]),np.array([0,2,0]),np.array([0,4,0]),fill_color='#ff585d',fill_opacity=0.6)
		
		rect14 = rect12.copy()
		#右边不规则的图形
		rect13 = Polygon(np.array([0,3,0]),np.array([0,2,0]),np.array([1,2,0]),np.array([0.5,3,0]),fill_color='#ff585d',fill_opacity=0.6)
		rect15 = rect13.copy()



		self.wait(1)
		#消失全部的图像
		group07 = VGroup(group01,group02,rect03,sign03,group03,rect06,rect07,rect08,rect09,rect10,rect11)
		
		self.play(FadeOut(group07),run_time=2)

		#最左边的矩形，变换后
		group04 = VGroup(rect14,rect04,rect05)
		self.play(FadeIn(group04))
		

		# # #变换中间
		group05 = VGroup(rect15,rect07).shift(0.5 * UP)
		
		

		# 加号
		sign04 = TextMobject("+").shift(0.5 * LEFT + 2.9 * UP)

		self.play(
			ApplyMethod(group04.shift,LEFT),
			Write(sign04),
			Write(group05)
			
			)

		#变换后最右边的
		group06 = VGroup(rect12,rect10,rect09,rect13,rect11).shift(3.5 * DOWN + 0.6 * LEFT)
		self.play(Write(group06),run_time=2)

		self.wait(3)
		
		

