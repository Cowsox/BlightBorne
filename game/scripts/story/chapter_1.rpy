label c1_letter:
    "To my chosen champion,"
    "You are to venture to the northern garrison and discuss diplomatic relations with the deserters that reside there."
    "They call themselves 'The Order of the Broken Blade'." 
    "We have maintained an uneasy armistice for the moment, but they continue to make demands." 
    "I trust you will deal with them accordingly."
    "This letter should inform them to treat your words as if they were my own."
    "Alas, I have more pressing matters to attend to."
    "Signed, King Harridan II"

label c1_diplomat:
    scene bb
    show diplo at fade, left
    dip "So, the king won't even bother to show up to this congregation. I'm not surprised."

    dip "Very well. You will have to do."

    dip "I take it you are aware of the lands of which we gather here today?"
    dip "How this stronghold falls within Lothdornel jurisdiction?"
    dip "As you can see, it is no longer occupied by the Crown."
    dip "That is why we of the Broken Blade seek to receive lawful authority to reside here."
    dip "With such written decree, it should clear any..."
    dip "...uncertainty regarding the matter."

    "The diplomat hands you a scroll detailing the terms of the agreement, recognising the Order of the Broken Blade as having the right to live on the land."
    "All the scroll requires now is your signature."
    menu:
        "Agree to land rights":
            jump c1_agree
        "Disagree to land rights":
            jump c1_disagree

label c1_agree:
    "You sign the document, endorsing the proposal."

    dip "I am glad that despite our troubled past, we can negotiate successfully."
    dip "I assure you we will pursue continued relations with the Kingdom."
    call c1_capital
    jump c1_pursue_agree

label c1_disagree:
    "You sign the document, condemning the proposal."

    dip "I should've known that this was going to be a waste of time."
    dip "You people will never understand-"
    call c1_capital
    jump c1_pursue_disagree

label c1_capital:
    "Though before the Diplomat could countinue, you are interrupted."

    show palad at fade, right
    pal "Forgive my interruption Champion, but I bare important tidings!"
    pal "There is word of the Captial being held under siege!"
    pal "Though the attackers are described as horribly mutilated by some sickening affliction..."

    pal "I have heard of such horrors before..."
    pal "This must be the works of the wretched necromancer."
    pal "I should've killed that witch long ago!"
    pal "We must bring her to justice before she gets away."

label c1_pursue_agree:
    dip "I wish you well on such an endeavour, Champion"
    dip "Perhaps we shall meet again."
    jump chapter_select

label c1_pursue_disagree:
    dip "Putting us down then walking away. Typical."
    dip "Now that your home is in danger, you are quick to act."
    dip "Don't expect us to be there in your hour of need, 'Champion'."
    jump chapter_select


