from gl import RayTracer, color
from sphere import * 
from obj import Envmap
import random

brick = Material(diffuse = color(0.8, 0.25, 0.25), spec = 16)
stone = Material(diffuse = color(0.4, 0.4, 0.4), spec = 4)

width = 512
height = 512
r = RayTracer(width, height)

r.point_light = PointLight(position = [0, 0, -8], intensity = 2)
r.ambient_light = AmbientLight(strength = 1)

r.scene.append(Room([0, 0, -4.8], 5, stone))
r.scene.append(Cube([2, -2, -6.5], 1.2, brick))
r.scene.append(Cube([-2, -2, -6.5], 1.2, brick))


r.glRayTracingRender()

r.glFinish('output.bmp')
