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
    "So, the king won't even bother to show up to this congregation. I'm not surprised."

    "Very well. You will have to do."

    "I take it you are aware of the lands of which we gather here today?"
    "How this stronghold falls within Lothdornel jurisdiction?"
    "As you can see, it is no longer occupied by the Crown."
    "That is why we of the Broken Blade seek to receive lawful authority to reside here."
    "With such written decree, it should clear any..."
    "...uncertainty regarding the matter."

    "The diplomat hands you a scroll detailing the terms of the agreement, recognising the Order of the Broken Blade as having the right to live on the land."
    "All the scroll requires now is your signature."
    menu:
        "Agree to land rights":
            $ bb_rights = "agree"
            jump agree
        "Disagree to land rights":
            $ bb_rights = "disagree"
            jump Disagree


