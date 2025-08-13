# Particles
image dust1:
    "particles/9.png"
    alpha renpy.random.uniform(1, 0.1)
    zoom .1
image dust2:
    "particles/9.png"
    alpha renpy.random.uniform(1, 0.1)
    zoom .05
image fog1:
    "particles/50.png"
    anchor (0.5, 0.5)
    zoom 1

# Transforms
transform shrink:
    zoom 1
    linear renpy.random.uniform(5, 20) zoom .01

transform colorizeBlight:
    matrixcolor TintMatrix("#b86800")
    linear renpy.random.uniform(0.1, 1) matrixcolor TintMatrix("#e6aa5c")
    linear 1 matrixcolor TintMatrix("#b86800")
    repeat

# Final SnowBlossom
image dust_fall_1 = SnowBlossom("dust1", count=50, border=20, xspeed=(-10, 10), yspeed=(10, 100), start=50, fast=False)
image dust_fall_2 = SnowBlossom("dust2", count=50, border=20, xspeed=(-10, 10), yspeed=(10, 100), start=50, fast=False)
image dust_rise_1 = SnowBlossom(At("dust1", shrink), count=50, border=20, xspeed=(-10, 10), yspeed=(-10, -100), start=50, fast=False)
image dust_rise_2 = SnowBlossom(At("dust2", shrink), count=50, border=20, xspeed=(-10, 10), yspeed=(-10, -100), start=50, fast=False)