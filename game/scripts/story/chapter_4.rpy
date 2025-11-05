label c4_intro:
    scene woods

    "Continuing further through the forest, you hear a rustle in the bushes..."
    menu:
        "Tell your companions to halt.":
            jump c4_stop
        "It's probably just a squirrel, we should remain focused.":
            jump c4_continue

label c4_stop:
    "You signal to your companions to stop."

    show necro at fade, left
    nec "What now?"

    show palad at fade, right
    pal "I heard it too, something in the bushes..."

    nec "You're both just being paranoid, we must keep moving."

    "The rustling continues once again."

    pal "Over there!"

    "A small silhouette leaps out of the bush, running right towards your party!"
    "It's...!"
    "...just a squirrel."

    nec "See? Told you both were just over-"

    "You see a glint of metal shine from between the leaves."
    "This time, a larger silhouette leaps out."
    jump c4_choice

label c4_continue:
    "You continue your journey through the forest. There is no time to waste."
    "But..."
    "A few moments later, the bushes rustle once more."
    "This time, you see a glint of metal shine from between the leaves."
    "A shadowy figure leaps out, blade in hand."
    jump c4_choice

label c4_choice:
    show bandi at fade, center
    ban "What is it we have here hmmm?"
    ban "Those who carry the mark of the Crown?"
    ban "Must be pretty important huh?"
    menu:
        "Leave at once, before I show you just how important I am. <Draw Blade>":
            jump c4_coward
        "Easy, we don't want any trouble.":
            jump c4_avoid
        "In the name of the king, I will cut you thieves down! Prepare to face justice, wretches! <Attack>":
            jump c4_attack

label c4_coward:
    ban "O-okay, we'll uh..."
    ban "...we'll let you pass this time..."

    hide bandi
    "The bandits flee."

    nec "We should've showed those insolet fools we are not to be trifled with."

    pal "We have no time for distractions, the villages is not too far from here."
    pal "Make haste!"
    jump chapter_select

label c4_avoid:
    ban "Well I'm afraid you asked for trouble the moment you came walking into our turf!"
    jump c4_aftermath

label c4_attack:
    ban "I'll gut you like a fish!"
    jump c4_aftermath

label c4_aftermath:
    ban "Okay okay, we yield! We yield!"
    ban "Please- take whatever you want..."
    ban "...just d-don't kill us!"

    nec "Why shouldn't we? Nobody will miss these lowlives."

    pal "Because they are yet to have a fair trial."
    pal "They must answer to the law."
    pal "Their execution is not our choice to make."

    nec "Death would be a mercy..."
    nec "At this rate, are you so certain there is even a stockade still standing to deliver them to?"
    menu:
        "Execute.":
            jump c4_execute
        "Spare.":
            jump c4_spare

label c4_execute:
    "You rest your blade upon the bandit's neck."
    "Before he could begin to beg for his life,"
    "...you slit his throat."
    hide banti
    "Instantly he falls, gargling in a pool of his own blood."

    "The Necromancer then blasts the other two bandits with a wave of dark energy."
    "Their bodies start decaying, rapidly..."
    "...until there is only a pile of bones left."

    nec "Good, I could use a few extra skulls to decorate my cave."

    pal "The King will hear of this! I promise you..."
    pal "...Both of you..."
    jump chapter_select

label c4_spare:
    hide bandi
    "You stow your blade, allowing for the bandits to limp their way back into the forest."

    nec "Shame. I could have used a few extra skulls to decorate my cave with..."

    pal "Good. Now that's concluded, let us commence forth!"
    jump chapter_select

