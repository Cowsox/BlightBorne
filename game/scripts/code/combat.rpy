init python:
    # fighter class definition
    class fighter:
        def __init__(self, name, image, hp, max_hp, atk, defe, my_type, can_heal, controllable):
            self.name = name
            self.image = image
            self.hp = hp
            self.max_hp = max_hp
            self.atk = atk
            self.defe = defe
            self.max_defe = 6 # CHANGE LATER
            self.my_type = my_type
            self.can_heal = can_heal
            self.can_block = True # CHANGE LATER
            self.controllable = controllable

    # fighters implemented
    p1 = fighter("Champion",        "sick girl.png", 10, 10, 2, 0, 0, False, True)
    p2 = fighter("Necromancer",     "sick girl.png", 15, 15, 2, 0, 0, True, True)
    p3 = fighter("Paladin",         "sick girl.png", 10, 10, 2, 0, 0, False, True)
    p4 = fighter("Oathbreaker",     "sick girl.png", 10, 10, 2, 0, 0, False, True)
    e1 = fighter("Plague Body",     "sick girl.png", 10, 10, 2, 0, 0, False, False)
    e2 = fighter("Bandit",          "sick girl.png", 10, 10, 2, 0, 0, False, False)
    e3 = fighter("Plague Knight",   "sick girl.png", 10, 10, 2, 0, 0, False, False)
    e4 = fighter("Oathbreaker",     "sick girl.png", 10, 10, 2, 0, 0, False, False)

    turn_order = [p1, p2, p3]
    turn_num = 0
    current_fighter = p1

    sub_size = 20

    # attack on target from source
    def attack(source, target):
        damage = source.atk + 1 - target.defe * 0.5
        if damage <= 0:
            damage = 0
        target.hp -= damage
        return damage
    # defence on target
    def defence(target, amount):
        defence = amount
        target.defe += amount
        return defence
    def def_down(target, amount):
        if target.defe > 0:
            target.defe += amount
    # heal on target
    def heal(target, amount):
        over_max = target.hp + amount
        if over_max > target.max_hp:
            target.hp = target.max_hp
        else:
            target.hp += amount
    #def attack_buff
    #def defence_debuff

# GUI screen
transform rot90:
    rotate 270
    rotate_pad False

transform red:
    matrixcolor TintMatrix("#b80000")

transform blue:
    matrixcolor TintMatrix("#00b899")

screen hp_bar(pos):
    for char in turn_order:
        $ pos += 0.1
        frame:
            xalign pos
            vbox:
                spacing 10
                xmaximum 200
                xminimum 200
                hbox:
                    spacing 10
                    xalign 0.5
                    image "images/icons/heart-organ.png" zoom 0.07 at red
                    text "[char.hp]/[char.max_hp]":
                        xalign 0.5
                hbox:
                    spacing 5
                    xalign 0.5
                    ymaximum 500
                    text "[char.name]" at rot90:
                        yalign 0.9
                        size 40
                    vbar value StaticValue(char.hp, char.max_hp) at red:
                        xsize 30
                        bottom_bar "images/bars/bottom.png"
                        top_bar "images/bars/top.png"
                    vbar value StaticValue(char.defe, char.max_defe) at blue:
                        xsize 10
                        bottom_bar "images/bars/bottom.png"
                        top_bar "images/bars/top.png"
                hbox:
                    spacing 10
                    xalign 0.5
                    image "images/icons/shield.png" zoom 0.07 at blue
                    text "[char.defe]/[char.max_defe]":
                        xalign 0.5
                        tooltip "Defence"

screen targeting:
    vbox:
        align (0.5, 0.5)
        for item in turn_order:
            $ var = item.name
            textbutton "[var]" action Return(item)

label combat_start:
    # setup GUI and Background
    show screen hp_bar(0.0)
    show image "images/backgrounds/simple background.jpg":
        zoom 1
    jump turn

# Switch current active turn
label turn:
    # Set current fighter
    $ current_fighter = turn_order[turn_num]
    $ def_down(current_fighter, -1)
    
    # find out if controllable
    if current_fighter.controllable == True:
        jump combat_menu
    else:
        jump ai

label turn_cycle:
    # rotate through the turn_order
    if turn_num == len(turn_order) - 1:
        $ turn_num = 0
    else:
        $ turn_num += 1
    jump turn

# Generalised turn menu
label combat_menu:
    show necro_battle at grayscale:
        xalign 0.0
        yalign 1.0
    "It is the [current_fighter.name]'s turn."
    menu:
        "Attack":
            call screen targeting
            $ target = _return
            $ e = attack(current_fighter, target)
            show necro_battle with hpunch:
                easein_elastic 1 xpos 0.2
            "The [current_fighter.name] attacks and delt [e] damage! [target.name] has [target.hp] hp left!"
        "Heal Party" if current_fighter.can_heal:
            $ heal(current_fighter, 3)
            $ heal(p1, 3)
            "The [current_fighter.name] heals their party, +3 health for all!"
        "Block": #if current_fighter.can_block
            $ e = defence(current_fighter, 2)
            "The [current_fighter.name] puts up their guard, gains [e] defence. [current_fighter.defe] total defence."
    jump turn_cycle

# AI Combat Options
label ai:
    $ i = renpy.random.randint(1, 3) #enemy ai (baby ah 123 random ai)
    if i == 2:
        $ e = attack(p3, p1)
        "The enemy makes an attack with [e] damage, reducing you to [p1.hp] health!"
    elif i == 3:
        $ e = attack(p3, p2)
        "The enemy makes an attack with [e] damage, reducing companion's health to [p2.hp]!"
    else:
        $ defence(p3, 2)
        "The enemy is shielding! [p3.defe] defence"
    jump turn_cycle

# check if combat should end
label win_check:
    if p1.hp <= 0:
        jump lose
    if p3.hp <= 0:
        jump win
    return

# Win and Loss conditions
label win:
    "You look around..."
    "No more monsters around, you're safe"
label lose:
    "You Died"