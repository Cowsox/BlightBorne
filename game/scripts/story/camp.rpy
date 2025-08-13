# Camp introduction
label camp_setup:
    scene woods
    "This appears to be a good spot to make camp."
    jump camp_main

# Main camp actions
label camp_main:
    scene campfire
    show snow1 at colorizeBlight
    show snow2 at colorizeBlight
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
        "Farmstead (Corpse Flower)":
            jump corpse_flower_1
        "Small Town (Mother & Daughter)":
            jump town_1
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
    show necro
    with dissolve
    "A quiet fellow."
    menu:
        "While he does not acknowledge your approach, experience tells you that he'll talk."
        "About him":
            jump nec_talk
        "About journey":
            jump nec_talk
        "About companions":
            jump nec_talk
        "Nevermind.":
            hide necro
            jump camp_main