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
define blood = "{color=#8b0000}blood{/color}"
define Blood = "{color=#8b0000}Blood{/color}"
define blight = "{color=#ffa500}blight{/color}"
define corpse = "{color=#808000}corpse{/color}"

define config.default_textshader = "zoom:0.2|typewriter|slowalpha:0"

# Resources
default infection = 0
default research = 0

default companions = 0

# Initialise image settings
init:
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
    image bear:
        "sick girl.png"
        zoom 0.6
    image arm:
        "mother/infected arm.png"
        zoom 0.5
    image necro:
        "necromancer.png"
        zoom 0.2
    image necro reach:
        "necromancer reach.png"
        zoom 0.2
    image palad:
        "paladin.png"
        zoom 0.2
    image mothe:
        "mother/mother mouth closed.png"
        offset (-200, 100)
        zoom 0.4
    image mothe cry:
        "mother/mother crying.png"
        offset (-200, 100)
        zoom 0.4
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

# slight pause on specific punctuation
init python:
    def slow_punctuation(str_to_test):
        return (str_to_test
            .replace(", ", ",{w=0.05} ")
            .replace(". ", ".{w=0.15} ")
            .replace("! ", "!{w=0.15} ")
            .replace("? ", "?{w=0.15} ")
            .replace(": ", ":{w=0.15} ")
            .replace("— ", "—{w=0.15} ")
            .replace(" —", " —{w=0.15}")
            .replace("... ", "...{w=0.3} ")
            .replace("Dr.{w=0.15} ", "Dr. ")
            .replace("Mx.{w=0.15} ", "Mx. ")
            .replace("Ms.{w=0.15} ", "Ms. ")
            .replace("Mr.{w=0.15} ", "Mr. ")
            .replace("St.{w=0.15} ", "St. "))
    config.say_menu_text_filter = slow_punctuation

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
    scene home
    "Whilst venturing within the forest, you come upon a ruined farmstead."
    
    show palad at fade, left
    pal "{b}Halt.{/b} That... {shader=jitter:3,3}{color=#66b032}stench{/color}{/shader}.{p}I've smelt it before..."

    show necro at fade, right
    nec "I sense something too. Those ruins up ahead. I advise we investigate."

    pal "Agreed. There could be survivors."

    nec "{size=-10}-Or something else we could use to our {i}advantage{/i}.{/size}"

    menu:
        "A decision must be made."
        "1. Very well, but we must remain vigilant.":
            jump corpse_flower_2b
        "2. I believe it is best we move on.":
            jump camp_setup

label corpse_flower_2b:
    scene corpse flower
    "Upon entering the room, a foul {shader=jitter:3,3}{color=#66b032}stench{/color}{/shader} fills your nostrils. A trail of [blood] leads to a corner."
    "It is there a [corpse] of a man has been mangled and mutilated by a thick growth of glutinous {color=#228b22}vines{/color}."
    "At the centre of the [corpse] emerges some form of twisted {color=#228b22}flora{/color}."
    "It's veiny {color=#228b22}petals{/color} glow with thick pustules of [blight]."

    "Upon a closer look, the {color=#228b22}plant{/color} is swaying as if it were {shader=wave:1}breathing...{/shader}"
    "Perhaps the [corpse] beneath was."

    show palad at fade, left
    pal "By all that is {b}holy{/b}..."

    show necro at fade, right
    nec "I've never seen anything such as this before."
    nec "It seems humans are not the only thing this [blight] corrupts."
    nec "Fascinating..."

    pal "This poor man..."
    pal "We must allow his {color=#ffffff}soul{/color} to travel with the respect it deserves."
    pal "I shall recite the litanies, then burn this {shader=jitter:3,3}abhorrence{/shader} to ash."

    nec "You will do no such thing, [paladin]."
    nec "This specimen is more useful to us intact."

    pal "{shader=jitter:3,3}Useful? Intact?{/shader}"
    pal "I know you are one to dabble in {shader=jitter:3,3}sin{/shader}, but this is excessive, even to your standards!"

    nec "[champion], if I can conduct research on this corpse flower, we could better understand what we're fighting against."
    nec "Maybe even a way to use it to our advantage."

    pal "You {b}cannot{/b} be considering this, [champion]."
    pal "We must destroy this {shader=jitter:3,3}vile bloom{/shader} before it spreads."

    menu:
        "A decision must be made."
        "1. If we can safely study it, we can better know our enemy.":
            jump corpse_flower_3a
        "2. If we can find a way to harness its power for ourselves, it is worth the risk.":
            jump corpse_flower_3b
        "3. We've lost so much already. It is best to destroy it.":
            jump corpse_flower_3c

label corpse_flower_3a:
    scene corpse flower
    show necro at fade, right
    nec "Very well. I will use the upmost caution."

    show palad at fade, left
    pal "Hmph. Make haste, {shader=jitter:3,3}witch{/shader}. We've been here long enough."

    "The [paladin] stands aside, humming a prayer for the fallen farmer."
    "The [necromancer] approaches the Corpse Flower, gently cutting off part of a {color=#228b22}petal{/color}, and placing it within a mortar and pestle."
    "With the now powdered {color=#228b22}petal{/color}, she pours it into four vials, each with a {color=#00ffff}different {color=#ff0000}colour {color=#ffff00}of {color=#ff00ff}liquid{/color}."
    "The liquids begin to {shader=jitter:3,3}bubble{/shader} slightly, with the [necromancer] writing some notes down in her grimoire."

    nec "Interesting reaction... This discovery shall serve us well, [champion]. (+1 Research Points)"

    pal "We cannot afford to be doing these {shader=jitter:3,3}wild{/shader} experiments on everything we discover."
    pal "Do not push your {i}luck{/i}, [champion]."
    jump camp_setup

label corpse_flower_3b:
    scene corpse flower
    show necro at fade, right
    nec "I am glad you have the courage to do whatever it takes to overcome this plague."

    show palad at fade, left
    pal "This is not courageous, this is recklessness."
    pal "Such recklessness I will have no part in."

    hide palad
    "The [paladin] leaves the room."
    show necro reach at left
    "The [necromancer] holds out a hand. Necrotic energy begins pulsing towards the Corpse Flower."

    nec "Interesting reaction..."

    "The Corpse Flower begins to glow even brighter as it starts growing into a horrible bloated state. Pustles begin to pop one by one."
    "Then they start popping in clusters."

    nec "Almost... got it..."

    "Suddenly, the entire growth explodes. {color=#8b0000}Blood{/color}, guts and bile coat the room and your party."

    scene heart
    nec "Such {shader=jitter:3,3}volatile{/shader} power. It is {i}ours{/i} now."
    nec "Apologies for the mess, [champion]. But it was worth the discomfort I assure you. (+1 Blight Seed)"
    jump camp_setup

label corpse_flower_3c:
    scene corpse flower
    show palad at fade, left
    pal "Good. This is what needs to be done."

    show necro at fade, right
    nec "Pity. We could've gained so much..."

    "The [paladin] draws his blade, it begins to glow a warm yellow hue."

    pal "By order of the crown and the power entrusted to me by the sacred oath, I smite this unholy {shader=jitter:3,3}abomination{/shader} to ash!"

    "The [paladin] crashes his blade down into the Corpse Flower."
    "A flash of light blinds the room."
    "The unholy energy clashing with the holy aura causes a violent eruption. A shock wave knocks the party to their feet."
    "Once the light fades, a large hole in the wall remains where the Corpse Flower once was.(-5 health)"

    nec "{shader=jitter:3,3}W-what was that!?{/shader}"

    pal "{b}Divine judgment.{/b}"
    pal "Our wounds will heal, just as this land now will."
    jump camp_setup

#
# Scenario 2 - Village
#
label town_1:
    scene village start
    "Within the town, a [mother] and her [daughter] approach you."

    scene village
    show mothe at fade
    mom "Y-you're from out of town, right?"
    mom "D-do you know the way to the Capital?"
    mom "We need to find an apothecary." 
    mom "My husband left about a week ago to find aid, but has yet to return."
    mom "Perhaps we could find him on the way?"

    show daugh at fade
    dau "I gave daddy my special teddy bear, Benny!"
    dau "He's a real good protector, and will protect daddy from all the bad nasties out there!"

    scene bear
    "You remember the stuffed bear you retrieved earlier."
    "The one being held by the victim of the Corpse Flower."
    menu:
        "1. Tell them the truth and return the bear.":
            jump truth
        "2. Say nothing.":
            jump town_2

label truth:
    scene village
    "You give the stuffed bear to the [child] and you condolences to them both."

    show mothe at fade
    mom "No..."
    mom "Oh.. God...."
    show mothe cry
    "*she begins to break down into tears*"

    show daugh bear
    dau "S-so that mean that daddy..."
    dau"...isn't coming back?"
    "The two hug each other tightly."
    mom "That.. that still doesn't change things."
    mom "We still- He would want us to keep going."
    jump town_2

label town_2:
    scene arm
    "You notice the [mother]'s arm has a subtle rash with pustules peeping through her sleeve."
    "Your companions gather to your side to discuss among themselves."

    scene village start
    show palad at fade, left
    pal "The capital is completely overrun with the [blight]. Sending them there would be a death sentence."
    show necro at fade, right
    nec "Its where she should go."
    nec "Better to keep the [blight] close to where it began, than having pox-walkers spread it to the rest of the kingdom."
    pal "It is my oath to save the survivors."
    nec "Its also your oath to stop the spreading of the [blight]."
    pal "... We have to try to help her."
    nec "We could just {shader=jitter:3,3}kill{/shader} her where she stands."
    nec "It would be quick and painless."
    nec "A better way to go than whatever {shader=jitter:3,3}horrors{/shader} lie in the Capital."
    pal "{shader=jitter:3,3}I... [champion]...{/shader}"
    pal "...I require your counsel."
    pal "I imagine whatever we do, her [daughter] will stay at her side."

    menu:
        "1. Give her directions to the Capital":
            jump town_3a
        "2. Put an end to her suffering here.":
            jump town_3b
        "3. Try and cut off the infected limb.":
            jump town_3c
        "4. Continue moving forward.":
            jump town_3d

label town_3a:
    scene village
    "You give the [woman] directions to the Capital city, knowing it is overrun by the [blight]."

    show mothe at fade
    mom "Thank you."
    mom "We will head out soon."
    hide mothe
    "The two depart."

    show necro at fade, right
    nec "Good. That should buy this town some time."
    "*The [paladin] remains silent on the matter.*"
    jump camp_setup

label town_3b:
    scene village
    "You look to your companions, with your hand on the hilt of your blade."
    "The [paladin] sighs, and starts walking with the [child], taking her away from what is to come."

    show necro at fade, right
    nec "I'm sorry, but this is the best we can do."
    nec "It'll be over quick, I promise."
    "You walk up to the [mother], blade drawn."
    show mothe at fade
    mom "W-what- no! Please!"
    mom "There must be another way- What about my daugh-{w=0.25}{nw}"
    hide mothe

    "Her pleas are cut short by the swift slice of your blade."
    "{color=#8b0000}Blood covers the area.{/color}"
    "Your tabard of the kingdom is now drenched in the [blood] of the innocent."
    nec "I know that was difficult, but if we hadn't done it..."
    nec "This entire town would be dead in a week."
    nec "You should go check in with the [paladin]."
    nec "I'll take care of the body."
    jump camp_setup

label town_3c:
    scene village
    "You look to the [paladin], signaling him towards the [child]."
    "He sighs, then begins walking with her, taking her away from what is to come."
    "The Capital is completely overrun. That's assuming you even make it that far."
    "The best we can do is cut off that limb and hope the infection ceases its corruption."

    show mothe at fade
    mom "Y-you want to cut off my arm?"

    show necro at fade, right
    nec "I know this is a hard decision, but we're out of options."
    nec "It's either this or certain death."
    mom "... Okay. For my family."
    "You and the [necromancer] tie a tourniquet around the woman's arm."
    nec "Ready?"

    show mothe cry
    mom "*the [mother] nods with her eyes watering.*"
    "You draw your blade and swiftly cut the arm off."
    "{color=#8b0000}Blood splatters everywhere{/color}, with the woman screaming in agony."
    "You attempt to wrap the wound in cloth, but the {i}{color=#8b0000}bleeding doesn't stop{/color}{/i}."
    mom "{shader=jitter:3,3}T-tell her... I... I'm sorry...{/shader}"
    "The [mother]'s body falls into your arms."
    "Lifeless."
    jump camp_setup
    
label town_3d:
    scene village
    "I'm sorry, but we must be departing."

    show mothe at fade
    mom "What? No- please I beg of you!"
    "You and your companions continue to move through the town, leaving the [mother] and [daughter] behind."
    hide mothe

    show palad at fade, left
    pal "We should've done something. Anything would've been better than leaving them."
    show palad at fade, right
    nec "We don't have time to save them all. We must stay focused on our mission."
    pal "*the [paladin] grumbles.*"
    jump camp_setup
