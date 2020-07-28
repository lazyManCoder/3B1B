from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
    #A few simple shapes

    global array
    array = []
    

    #创建圆
    def outerCircle(self,num,time):
    	#清除前一个数据的圆环转换成直线的影响
    	if num == 101:
    		array.clear()
    	for i in range(num):
    		a = 2 * (i / (num -1) )
    		circle = Circle(radius=(2 - a))
    		array.append(circle)
	    	self.play(GrowFromCenter(circle),run_time=time)
	    	

	#从圆变成直线
    def innerCircle(self,num,time):
    	for j in range(num):
	    	a = 2 * (j / (num - 1))
    		circle = array[j]
	    	line = Line(np.array([-PI * (2-a),-(2-a),0]),np.array([PI * (2 - a),-(2-a),0]),color=BLUE)
	    	self.play(Transform(circle.rotate(PI / 2),line),run_time=time)


    def construct(self):
    	#圆点
    	circle_point = Dot(np.array([0,0,0]))
    	self.add(circle_point)

    	#半径直线
    	rline = Line(np.array([0,0,0]),np.array([0,-2,0]))

    	#外圆
    	circle0 = Circle(radius=2).set_color(WHITE)
    	group = VGroup(rline,circle0)
    	self.add(group)

    	num = 11
    	time = 0.8
    	self.outerCircle(num,time)
    	self.innerCircle(num,time)

    	#画三角形的线
    	triangle = Polygon(np.array([-PI * 2,-2,0]),np.array([PI * 2,-2,0]),np.array([0,0,0]),fill_opacity=0,color=GREEN)
    	

    	#勾股定理公式
    	text01 = TextMobject("三角形面积 = ").next_to(triangle,DOWN + 0.2 * LEFT)
    	text02 = TextMobject(r"$2 \pi r  $").next_to(text01,RIGHT)
    	text03 = VGroup(text01,text02).next_to(triangle,DOWN)
    	

    	self.play(
    		Write(triangle),
    		Write(text03),

    	)

    	self.wait(3)

    	#将第一个圆进行隐藏起来
    	group01 = VGroup(text03,circle_point,rline,circle0,triangle)
    	self.play(FadeOut(group01))


    	# print(linegroup)
    	for i in array: self.play(FadeOut(i),run_time=0.1)

    	group02 = VGroup(circle_point,rline,circle0)
    	self.play(FadeIn(group02))


    	#第二个圆分布的更细
    	num = 101
    	time = 0.1
    	
    	self.outerCircle(num,time)
    	self.innerCircle(num,time)

    	group03 = VGroup(triangle,text03)
    	self.play(FadeIn(group03))
    	self.wait(3)






 




	    