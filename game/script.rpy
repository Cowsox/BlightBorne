define config.top_layers = [ 'toplayer' ]

# Characters
define nec = Character("Necromancer", who_color="#663399", what_color="#d8bfd8")
define pal = Character("Paladin", who_color="#daa520", what_color="#eee8aa")
define mom = Character("Mother", who_color="#6495ed", what_color="#87ceeb")
define dau = Character("Daughter", who_color="#db7093", what_color="#ffe4e1")
define me = Character("Champion")

# Character in-text colours
define paladin = "{color=#daa520}Paladin{/color}"
define necromancer = "{color=#663399}Necromancer{/color}"
define champion = "{color=#b0e0e6}Champion{/color}"
define mother = "{color=#6495ed}mother{/color}"
define woman = "{color=#6495ed}woman{/color}"
define daughter = "{color=#db7093}daughter{/color}"
define child = "{color=#db7093}child{/color}"

# key word colours
# capital words for start of sentence
define blood = "{color=#8b0000}blood{/color}"
define Blood = "{color=#8b0000}Blood{/color}"
#define blight = "{color=#ffa500}blight{/color}"
define corpse = "{color=#808000}corpse{/color}"

define config.default_textshader = "zoom:0.2|typewriter|slowalpha:0"

# Resources
default infection = 0
default research = 0

default companions = 2

# Initialise image settings
init:
    # Backgrounds
    image campfire:
        "camp.png"
        yalign 0.0
        zoom 0.6
    image corpse flower:
        "corps flower.png"
        yalign 0.0
        zoom 0.6
    image village:
        "village/village.png"
        yalign 1.0
        zoom 0.6
    image village start:
        "village/village with mother and dughter.png"
        yalign 1.0
        zoom 0.6
    image home:
        "home.png"
        zoom 0.6
    image heart:
        "heart hand.png"
        yalign 0.3
        zoom 0.5
    # Close Ups
    image bear:
        "sick girl.png"
        zoom 0.6
    image arm:
        "mother/infected arm.png"
        zoom 0.5
    # Necromancer
    image necro:
        "images/Necromancer/Nec_Pose1.png"
        zoom 0.3
    image necro_battle:
        "images/Necromancer/Nec_Pose2.png"
        zoom 0.2
    # Paladin
    image palad:
        "images/Paladin/Pal_Pose1.png"
        zoom 0.2
    # Mother
    image mothe:
        "mother/mother mouth closed.png"
        offset (-200, 100)
        zoom 0.4
    image mothe cry:
        "mother/mother crying.png"
        offset (-200, 100)
        zoom 0.4
    # Daughter
    image daugh:
        "child/child mouth closed.png"
        offset (-100, 200)
        zoom 0.4
    image daugh bear:
        "child/child bear.png"
        offset (-100, 200)
        zoom 0.4

    transform fade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

    transform darken:
        alpha 1.0
        linear 1.0 alpha 0.5

    transform grayscale:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 1.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)

    transform restore:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        alpha 1.0

################################# STORY CODE ##################################################
label particle_demo:
    show dust_rise_1 at colorizeBlight
    show dust_rise_2
    "text {a=jump:camp_main}camp{/a} {a=jump:combat_start}combat{/a}"
    "a blight game"
    "{ghostwrite}Ghostwrite{/ghostwrite}"
    "{burningforbigtext}Burning For Big Text{/burningforbigtext}"
    "{burningforsmalltext}Burning For Small Text{/burningforsmalltext}"
    "{blueburnbig}Blue Burn Big{/blueburnbig}"
    "{blueburnsmall}Blue Burn Small{blueburnsmall}"
    "{demo}Demo{/demo}"
    "{hollowglow}Hollow Glow{/hollowglow}"
    "{gradientglow}Gradient Glow{/gradientglow}"
    "{glow}Glow{/glow}"
    "{redalert}Red Alert{/redalert}"
    "{prey}Prey{/prey}"
    "{goldsweep}Gold Sweep{/goldsweep}"
    "{colorsweep}Colour Sweep{colorsweep}"
    "{textshadow}Text Shadow{textshadow}"
    "{reversed}Reversed{reversed}"
    "{flipped}Flipped{flipped}"
    "{cthonic}Cthonic{cthonic}"
    "{cthonicjitter}Cthonic Jitter{cthonicjitter}"
    "{redactedglitch}Redacted Glitch{redactedglitch}"
    "{cthonicglitch}Cthonic Glitch{cthonicglitch}"
    "{cthonicglitchcolor}Cthonic Glitch Colour{cthonicglitchcolor}"
    "{static}Static{static}"
    "{atl=bounce}Bounce{/atl}"
    "{bt=h10-s0.5-p10.0}Old Bounce{/bt}"
    "{atl=rotate_text~1.0}Rotate{/atl}"
    "{rotat}Old Rotate{/rotat}"
    "{atl=0.3,drop_text~#~ 1.5}Drop{/atl}"
    "{atl=-#,#,fade_in_text~1.0}Fade In{/atl}"
    "{fi=0-0.5}Old Fade In{/fi}"
    "{glitch=1.5}Glitch{/glitch}"
    "{gradient=#ff0000-#00ff00}Still Gradient{/gradient}"
    "{gradient2=6-#ff0000-#ffff00-10-#ffff00-#00ff00-10-#00ff00-#00ffff-10-#00ffff-#0000ff-10-#0000ff-#ff00ff-10-#ff00ff-#ff0000-10}Moving Gradient{/gradient2}"
    "{swap=Change@Switch@1.0}swap{/swap}"
    "{sc}Scared{/sc}"

# Required start point
label start:
    #show snow1 onlayer toplayer
    #show snow2 onlayer toplayer
    #jump particle_demo
    jump camp_main
