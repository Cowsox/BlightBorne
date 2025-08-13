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
    pal "The capital is completely overrun with the blight. Sending them there would be a death sentence."
    show necro at fade, right
    nec "Its where she should go."
    nec "Better to keep the blight close to where it began, than having pox-walkers spread it to the rest of the kingdom."
    pal "It is my oath to save the survivors."
    nec "Its also your oath to stop the spreading of the blight."
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
    "You give the [woman] directions to the Capital city, knowing it is overrun by the blight."

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