init:
    image c1_i:
        "map/c1_idle.png"
        zoom 0.7
    image c1_h:
        "map/c1_hover.png"
        zoom 0.7
    image c2_i:
        "map/c2_idle.png"
        zoom 0.7
    image c2_h:
        "map/c2_hover.png"
        zoom 0.7
    image c3_i:
        "map/c3_idle.png"
        zoom 0.7
    image c3_h:
        "map/c3_hover.png"
        zoom 0.7
    image c4_i:
        "map/c4_idle.png"
        zoom 0.7
    image c4_h:
        "map/c4_hover.png"
        zoom 0.7
    image c5_i:
        "map/c5_idle.png"
        zoom 0.7
    image c5_h:
        "map/c5_hover.png"
        zoom 0.7
    image c6_i:
        "map/c6_idle.png"
        zoom 0.7
    image c6_h:
        "map/c6_hover.png"
        zoom 0.7

screen MapUI():
    add "map/bg_map.jpg" zoom 0.7 align(0.5,0.5)

    imagebutton:
        xpos 694
        ypos -6
        idle "c1_i"
        hover "c1_h"
        action Jump("c1_letter")
    
    imagebutton:
        xpos 1329
        ypos 9
        idle "c2_i"
        hover "c2_h"
        action Jump("c2_intro")
    
    imagebutton:
        xpos 1121
        ypos 166
        idle "c3_i"
        hover "c3_h"
        action Jump("corpse_flower_1")

    imagebutton:
        xpos 1136
        ypos 344
        idle "c4_i"
        hover "c4_h"
        action Jump("c4_intro")

    imagebutton:
        xpos 810
        ypos 290
        idle "c5_i"
        hover "c5_h"
        action Jump("town_1")

    imagebutton:
        xpos 891
        ypos 528
        idle "c6_i"
        hover "c6_h"
        action NullAction()

label chapter_select:
    scene home
    show image "images/backgrounds/simple background.jpg":
        zoom 1
    menu:
        "Camp":
            jump camp_setup
        "Map":
            jump map
        "Particle Demo":
            jump particle_demo

label map:
    call screen MapUI
    pause
    jump map
