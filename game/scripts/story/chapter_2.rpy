label c2_intro:
    scene evil_cave

    show palad at fade, left
    pal "These caverns are where the Necromancer lurks.{p}Remain vigilant."

    nec "Vigilance will not save you..."

    pal "Show yourself, witch!"

    nec "Ah, the feeble knight."

    pal "I'm a paladin now."

    nec "I know who you are."
    nec "You were a knight when you volunteered to {i}execute{/i} me."

    show necro at fade, right
    "The Necromancer emerges from the shadows."

    nec "Now, you and your friend will tell me why you have come."
    nec "I haven't had many visitors since I was exiled..."

    menu:
        "I am the King's Champion. We only wish to speak with you.":
            jump c2_plague_nice
        "I am the King's Champion, and by order of the Crown, you will heed my word.":
            jump c2_plague_mean

label c2_plague_nice:
    nec "A Champion?"
    nec "Coming to visit little old me?"
    nec "{size=-10}This should be interesting...{/size}"
    nec "Very well, I shall listen."
    nec "For now..."

    "A devastating plague has besieged our kingdom."
    "We are aware of your affinity with the dark arts."
    "If you have any knowledge on such a plague, we {b}must{/b} know."

    nec "Not any more than you would, Champion."
    nec "I have yet to uncover the mysteries of this... blight."

    call c2_plague
    jump c2_request_nice

label c2_plague_mean:
    nec "I wil do what I please, 'Champion'."
    nec "Whatever it is you have to say, spare your breath."
    nec "I no longer serve this kingdom, nor do I have any intention to."

    "A devastating plague has besieged our kingdom."
    "Whatever it is you have done, you will reverse it at once!"

    nec "What {b}I{/b} have done?"
    nec "You are mistaken."
    nec "Whatever this plague is, I have had no part in it."

    call c2_plague
    jump c2_request_mean

label c2_plague:
    pal "{sc}You lie!{/sc}"

    nec "See for yourself..."
    "The Necromancer holds out a jar containing blighted flesh."

    pal "...by the king, what is that?"

    nec "A sample."
    nec "I... aquired it from some ill peasant."
    nec "Notice anything with your 'divine sense'?"

    "The Paladin's {goldsweep}eyes glow{/goldsweep} for a moment."
    pal "I..."
    pal "Champion, the unholy aura coming from that jar is... different..."
    pal "Too different, at least, from that witch's energies."
    pal "I'm afraid she speaks the truth."

label c2_request_nice:
    "Very well..."
    "Necromancer, I humbly ask you to accompany us on this journey."
    "Your expertise could be useful."

    nec "It has been quite a while since I've done some field research..."
    nec "Though I ask to recieve any artifacts we may encounter along the way."
    jump chapter_select

label c2_request_mean:
    "Very well..."
    "Necromancer, you will be under my custody."
    "With this I give you a chance to repay your lengthy debt to society."
    "Fail to comply, and I'll kill you where you stand."

    "The Necromancer gives you a stern glare."
    nec "I will do this..."
    nec "but only for my own benefit - not yours, nor the kingdom's."
    jump chapter_select