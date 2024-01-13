from manim import *

class CircleComposition(Scene):
    def construct(self):
        axes = Axes(tips=False)
        circle = Circle()
        dot = Dot()

        self.add(axes, circle, dot)
        self.play(MoveAlongPath(dot, circle), rate_func=linear)
        self.wait()

class PolygonTransform(Scene):
    def construct(self):
        polygons = []
        minSides = 3
        maxSides = 11
        colors = [BLUE, RED, GREEN]
        for i in range(minSides, maxSides + 1):
            polygons.append((RegularPolygon(n = i,
                                            color = colors[i % 3])
                                            .scale(3),
                            Text(str(i))))

        for i in range(maxSides - minSides):
            self.clear()
            self.play(Transform(polygons[i][1], polygons[i + 1][1]),
                      Transform(polygons[i][0], polygons[i + 1][0]))
            
        self.wait()

class DotTransform(Scene):
    def construct(self):
        dot = Dot(color=BLUE).scale(3)
        line = Line(color=BLUE).scale(3)
        triangle = Triangle(color=BLUE).scale(3)

        self.add(dot)
        self.wait()
        self.clear()
        self.play(FadeTransform(dot, line, stretch=True, dim_to_match=0))
        self.wait()
        self.clear()
        self.play(Transform(line, triangle))
        self.wait()

def sine_wave(self, z, color, t):
    xmax= 2 * PI
    k = 3 * PI / xmax
    A = np.angle(z)
    R = abs(z) 
    w = 2 * PI * self.frequency
    wta = w * t + A
    f = lambda x: R * np.sin(wta - k*x)
    
    return FunctionGraph(f, x_min=0, x_max=xmax, color=color)
