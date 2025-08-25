init python:
    # fighter class definition
    class fighter:
        def __init__(self, name, hp, max_hp, atk, defe, my_type, can_heal, controllable):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.atk = atk
            self.defe = defe
            self.max_defe = max_defe
            self.my_type = my_type
            self.can_heal = can_heal
            self.can_block = can_block
            self.controllable = controllable

    # fighters implemented
    p1 = fighter("Champion", 10, 10, 2, 0, 0, False, True)
    p2 = fighter("Necromancer", 15, 15, 2, 0, 0, True, True)
    p3 = fighter("Paladin", 10, 10, 2, 0, 0, False, True)
    p4 = fighter("Oathbreaker", 10, 10, 2, 0, 0, False, True)
    e1 = fighter("Plague Body", 10, 10, 2, 0, 0, False, False)
    e2 = fighter("Bandit", 10, 10, 2, 0, 0, False, False)
    e3 = fighter("Plague Knight", 10, 10, 2, 0, 0, False, False)
    e4 = fighter("Oathbreaker", 10, 10, 2, 0, 0, False, False)

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
screen hp_bars_1v1:
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.1
        xmaximum 600
        text "[p1.name]"
        bar value StaticValue(p1.hp, p1.max_hp):
            left_bar "images/bars/full.png"
            right_bar "images/bars/empty.png"
        text "Health: [p1.hp]/[p1.max_hp]" size 20
        text "Defence: [p1.defe]" size 20
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.4
        xmaximum 600
        text "[p2.name]"
        bar value StaticValue(p2.hp, p2.max_hp):
            left_bar "images/bars/full.png"
            right_bar "images/bars/empty.png"
        text "Health: [p2.hp]/[p2.max_hp]" size 20
        text "Defence: [p2.defe]" size 20
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.1
        xmaximum 600
        text "[p3.name]"
        bar value StaticValue(p3.hp, p3.max_hp):
            left_bar "images/bars/full.png"
            right_bar "images/bars/empty.png"
        text "Health: [p3.hp]/[p3.max_hp]" size 20
        text "Defence: [p3.defe]" size 20

screen targeting:
    vbox:
        align (0.5, 0.5)
        for item in turn_order:
            $ var = item.name
            textbutton "[var]" action Return(item)

label combat_start:
    
    # setup GUI and Background
    show screen hp_bars_1v1
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
    "It is the [current_fighter.name]'s turn."
    menu:
        "Attack":
            call screen targeting
            $ target = _return
            $ e = attack(current_fighter, target)
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