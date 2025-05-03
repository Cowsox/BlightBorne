# Characters
define nec = Character("Necromancer")
define pal = Character("Paladin")

# Resources
default infection = 0
default research = 0

default companions = 0

# Initialise image settings
init:
    image campfire:
        "campfire.jpg"
        zoom 1.5
    image necro:
        "necromancer.png"
        zoom 0.2
    image palad:
        "paladin.png"
        zoom 0.2

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

# Required start point
label start:
    jump camp_main

# Camp introduction
label camp_setup:
    scene woods
    "This appears to be a good spot to make camp."
    jump camp_main

# Main camp actions
label camp_main:
    scene campfire
    menu:
        "The camp is quiet."
        "Move camp":
            jump camp_move
        "Talk to companions":
            jump camp_companions

# Move from camp actions
label camp_move:
    menu:
        "It is dangerous to stay in one place too long, where should we go?"
        "Abandoned Lab":
            jump senario_1
        "Ruined Buildings":
            jump senario_2
        "Stay... For now.":
            jump camp_main

# Talk to companions
label camp_companions:
    if companions:
        "Those that are still here, are huddled around a dying fire."
        menu:
            "Talk to whom?"
            "Necromancer":
                jump nec_talk
            "Paladin":
                jump nec_talk
            "Taking will waste valuable time.":
                jump camp_main
    else:
        menu:
            "There is no one here.":
                jump camp_main

# Talk to necromancer
label nec_talk:
    show Necromancer
    with dissolve
    "A quiet fellow."
    menu:
        "While he does not aknowledge your approach, experience tells you that he'll talk."
        "About him":
            jump nec_talk
        "About journey":
            jump nec_talk
        "About companions":
            jump nec_talk
        "Nevermind.":
            hide necromancer
            jump camp_main

# Corpse Flower
label senario_1:
    # Scene
    scene lab
    "The flower smells of death."

    # Characters
    show necro at fade, left
    nec "Use It!"
    show necro at darken, grayscale

    show palad at fade, right
    pal "No, Destroy It!"
    show palad at darken, grayscale

    # Choice
    menu:
        "A decision must be made."
        "Use It.":
            jump A
        "Destroy It.":
            jump B

label A:
    show necro at center:
        alpha 1.0
        xalign 0.0
        ease 1.0 xalign 0.5
    "The necromaner is delighted."
    jump senario_1_end

label B:
    show palad at center:
        alpha 1.0
        xalign 1.0
        ease 1.0 xalign 0.5
    "The paladin grins at the burning remains."
    jump senario_1_end

label senario_1_end:
    hide palad
    hide necro
    "Despite the outcome, this threat has been dealt with. We should move on."
    jump camp_setup
