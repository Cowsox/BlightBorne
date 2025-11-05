label c6_intro:
    scene ci
    "The Magistrate notices your arrival, putting down a handful of scrolls."

    show magis at fade, left
    mag "Finally, my request is heeded."
    mag "Well met, Champions of the Crown."
    mag "There has been a rapid influx of sick individuals present in Oakshire."
    mag "Our healers are insufficent to help this many people, which is why we need the Capital to-"

    show palad at fade, right
    pal "The Capital is besiged."

    mag "-What?"

    pal "We were hoping you could be the one to help us."
    pal "Do you know of anything regarding what's happening in the Capital?"
    pal "Any information is better than charging in blindly."

    mag "Only that the sickly have fleed from it."
    mag "They spoke of these... monsters..."
    mag "But I had assumed it was just some sort of mass hysteria."

    "You feel the air getting colder around you, as a horrible chill goes down your spine..."

    show oathe at fade, center
    oat_hide "They speak the truth."
    oat_hide "These monsters are {i}real{/i}"

    "You turn around to see a knight clad in dark armour."
    "Skulls adorne arcross their chestplate as their crimson red eyes gaze down upon you."

    "The Paladin draws his sword."

    pal "DEFILER!{p}I WILL BURN YOU TO ASH!"

    "The Paladin swings his blade towards the unknown knight."
    "You watch as it glides vigourously through the air."
    "..."
    "...Abruptly, the blade stops?"
    "The dark gauntlet of the knight holds it in place."

    oat_hide "Your {i}faith{/i} blinds you."
    oat_hide "I do not seek destruction."
    oat_hide "I herald the approaching doom."

    pal "You carry the mark of the Blight."
    pal "Death is the only path left for you."

    show necro at fade, right
    nec "Hold on, we should hear what they have to say."

    pal "I have no care for whatere {b}blasphemy{/b} they spill!"
    pal "This ends now!"

    menu:
        "No mercy for the wicked.":
            jump c6_combat
        "Heed the word of the harbringer.":
            jump c6_heed

label c6_combat:
    "You draw your blade."

    "FIGHT GOES HERE"
    jump chapter_select

label c6_heed:
    me "Stand down, we will hear their word."

    "The Paladin begrudgingly holds back his blade."

    pal "Speak then. What manner of vile being are you?"

    show oathe at fade, center
    oat "I once swore myself to the Light." # What is the Light?
    oat "To defend the kingdom with courage and honour."
    oat "But when this blight was unleashed, these was little I wcould do."
    oat "The radient powers of the Light were not enough."
    oat "I needed more..."
    oat "...More strength, more power."
    oat "So I let the Blight corrupt me..."
    oat "...allowing myself to wield the dark magic and mutated strength as a weapon against the Blight."

    pal "You were a paladin...{p}Your oath..."
    pal "How could you forsake it?"

    oat "I did what I had to do."
    oat "Someday you'll understand."
    oat "Regardless, heed my word."
    oat "The Capital has fallen.{p} This town {i}will{/i} be next to perish."

    pal "So long as I draw breath, Lothdornel will not fall."

    oat "And what hope do you -- any of you, have against an army of the blighted?"
    oat "One that approaches ever-"

    "The Oathbreaker slowly looks towards the entrance."

    oat "They're here....."

    "The Oathbreaker swiftly begins to leave the town hall."

    oat "I shall do what I can."
    hide oathe

    "You start to hear distant marches, followed by screams."

    mag "Asemble the guards!"
    mag "Evacuate the civilians!"
    mag "Champions, aid us in this battle!"

    "You and your companions run out of the town hall."
    jump c6_outside

label c6_outside:
    scene c6_outside_combat
    "Upon leaving the town hall, the woosh of the wind grows louder as the great boulder crashes into the town hall."
    "You look around and see fires ablaze, buildings collapsing."
    "People are running from mutated knights clad in rusting armour."
    "At the centre of it all, a grotesque amalgamation of flesh and metal roars."

    show groto at fade, center
    gro "Hunt them to the last!"
    gro "All will feel the festering might of the Blightborne!"

    "FIGHT GOES HERE"
    jump c6_end

label c6_end:
    "You see The Oathbreaker in the distance, retrieving their blade from the mutilated corpse of a plague knight."

    show oathe at fade, left
    oat "More will come..."
    oat "We cannot win this war by attrition alone."
    oat "Find a discreet way to the capital."
    oat "The sewers would be your best chance."

    show palad at fade, right
    pal "What of the endless hordes?"
    pal "We can't abandon our people!"

    oat "Everything will die if this infection is not cut from its source."
    oat "I'll hold off the tides as long as I can."
    oat "Fight hard, champions."
    oat "Die well."
    jump chapter_select