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
    #config.say_menu_text_filter = slow_punctuation