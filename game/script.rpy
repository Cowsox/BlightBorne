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
            jump corpse_flower_1
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

label corpse_flower_1:
    scene lab
    "*Whilst venturing within the forest, you come upon a ruinedfarmstead."
    
    show palad at fade, left
    pal "Halt. That stench. I've smelt it before..."

    show necro at fade, right
    nec "I sense something too. Those ruins up ahead. I advise we investigate."

    pal "Agreed. There could be survivors."

    nec "-Or something else we could use to our advantage."

    menu:
        "*A decision must be made."
        "1. Very well, but we must remain vigilant.":
            jump corpse_flower_2b
        "2. I believe it is best we move on.":
            jump camp_setup

label corpse_flower_2b:
    scene lab
    "*Upon entering the room, a foul stench fills your nostrils.A trail of blood leads to a corner."
    "*It is there a corpse of a man has been mangled and mutilated by a thick growth of glutinous vines."
    "*At the centre of the corpse emerges someform of twisted flora."
    "*It's veiny petals glow with thick pustules of blight."

    "*Upon a closer look, the plant is swaying as if it were breathing..."
    "*Perhaps the corpse beneath was."

    show palad at fade, left
    pal "By all that is holy..."

    show necro at fade, right
    nec "I've never seen anything such as this before."
    nec "It seems humans are not the only thing this blight corrupts."
    nec "Fascinating..."

    pal "This poor man..."
    pal "We must allow his soul to travel with the respect it deserves."
    pal "I shall recite the litanies, then burn this abhorrence to ash."

    nec "You will do no such thing, Paladin."
    nec "This specimen is more useful to us intact."

    pal "Useful? Intact?"
    pal "I know you are one to dabble in sin, but this is excessive, even to your standards!"

    nec "Champion, if I can conduct research on this corpse flower, we could better understand what we're fighting against."
    nec "Maybe even a way to use it to our advantage."

    pal "You cannot be considering this, Champion."
    pal "We must destroy this vile bloom before it spreads."

    menu:
        "*A decision must be made."
        "1. If we can safely study it, we can better know our enemy.":
            jump corpse_flower_3a
        "2. If we can find a way to harness it's power for ourselves, it is worth the risk.":
            jump corpse_flower_3b
        "3. We've lost so much already. It is best to destroy it.":
            jump corpse_flower_3c

label corpse_flower_3a:
    scene lab
    show necro at fade, right
    nec "Very well. I will use the upmost caution."

    show palad at fade, left
    pal "Hmph. Make haste, witch. We've been here long enough."

    "*The Paladin stands aside, humming a prayer for the fallenfarmer."
    "*The Necromancer approaches the Corpse Flower, gentlycutting off part of a petal, and placing it within a mortarand pestle."
    "*With the now powdered petal, she pours it intofour vials, each with a different colour of liquid."
    "*The liquids begin to bubble slightly, with the Necromancer writing some notes down in her grimoire."

    nec "Interesting reaction... This discovery shall serve us well, Champion. (+1 Research Points)"

    pal "We cannot afford to be doing these wild experiments on everything we discover."
    pal "Do not push your luck, Champion."
    jump camp_setup

label corpse_flower_3b:
    scene lab
    show necro at fade, right
    nec "I am glad you have the courage to do whatever it takes to overcome this plague."

    show palad at fade, left
    pal "This is not courageous, this is recklessness."
    pal "Such recklessness I will have no part in."

    "*The Paladin leaves the room."
    "*The Necromancer holds out a hand. Necrotic energy beginspulsing towards the Corpse Flower."

    nec "Interesting reaction..."

    "*The Corpse Flower begins to glow even brighter as it startsgrowing into a horrible bloated state. Pustles begin to popone by one."
    "*Then they start popping in clusters."

    nec "Almost... got it..."

    "*Suddenly, the entire growth explodes. Blood, guts and bilecoat the room and your party."

    nec "Such volatile power. It is ours now."
    nec "Apologies for the mess, Champion. But it was worth the discomfort I assure you. (+1 Blight Seed)"
    jump camp_setup

label corpse_flower_3c:
    scene lab
    show palad at fade, left
    pal "Good. This is what needs to be done."

    show necro at fade, right
    nec "Pity. We could've gained so much..."

    "*The paladin draws his blade, it begins to glow a warm yellow hue."

    pal "By order of the crown and the power entrusted to me by the sacred oath, I smite this unholy abomination to ash!"

    "*The paladin crashes his blade down into the Corpse Flower."
    "*A flash of light blinds the room."
    "*The unholy energy clashingwith the holy aura causes a violent eruption. A shock waveknocks the party to their feet."
    "*Once the light fades, a largehole in the wall remains where the Corpse Flower once was.(-5 health)"

    nec "W-what was that!?"

    pal "Divine judgment."
    pal "Our wounds will heal, just as this land now will."
    jump camp_setup

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
