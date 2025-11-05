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

# === Ember Color & Motion ===
transform emberTint:
    matrixcolor TintMatrix("#ff4000")  # bright red-orange
    linear renpy.random.uniform(0.3, 1.0) matrixcolor TintMatrix("#ff8000")  # flicker
    linear renpy.random.uniform(0.3, 1.0) matrixcolor TintMatrix("#ff4000")
    repeat

transform emberRiseShrink:
    alpha 1.0
    zoom 1.0
    linear renpy.random.uniform(3.0, 6.0) alpha 0.0 zoom 0.6
    repeat

# === Rising Ember Particles ===
image ember_rise_1 = SnowBlossom(At("dust1", emberTint, emberRiseShrink),
    count=60,
    border=50,
    xspeed=(-20, 20),
    yspeed=(-100, -250),   # negative = rising upward
    start=100,
    fast=False)

image ember_rise_2 = SnowBlossom(At("dust2", emberTint, emberRiseShrink),
    count=40,
    border=50,
    xspeed=(-15, 15),
    yspeed=(-80, -200),
    start=100,
    fast=False)