#STEP 1: Edit this to change what words are affected by the tooltip
# Element 1 is the key, this must be unique for each tooltip, Element 2 is an array of words to compare against, Element 3 is the title string to display
# And Element 4 is the description string to display
define inline_tooltip_list = [
    inline_tooltip_data("elf", [_("Elf"), _("Elves"), _("Elvhen"), ("elves")], _("The Elves"), _("The Elves are a pointy eared people with a lot of rizz.")),
    inline_tooltip_data("dwarf", [_("Dwarf"), _("Dwarves"), _("Dwarven")], _("The Dwarves"), _("The Dwarves are a subteranean society of cool guys.")),
    inline_tooltip_data("blight", [_("Blight"), _("blight")], _("The Blight"), _("A mysterious and deadly disease that has spread throughout the kingdom.")),
]

# Edit this style to change how the text you hover over appears
style inline_tooltip is say_dialogue:
    hyperlink_functions (inline_tooltip_styler, inline_tooltip_clicked, inline_tooltip_hovered)
    hover_underline True
    hover_color "#d6406d"
    color "#ac0360"

#STEP 2:  You might need to add the hyperlink function to whatever style the About screen text/say dialogue uses, but if you're using the default screen setup, this should work
style gui_text:
    hyperlink_functions (inline_tooltip_styler, inline_tooltip_clicked, inline_tooltip_hovered)

style say_dialogue:
    hyperlink_functions (inline_tooltip_styler, inline_tooltip_clicked, inline_tooltip_hovered)

style bubble_what:
    hyperlink_functions (inline_tooltip_styler, inline_tooltip_clicked, inline_tooltip_hovered)

define tooltip_width = 600

#STEP 3: Edit this screen to change the appearance of the tooltip
screen inline_tooltip(title, description, position):
    frame:
        xsize tooltip_width
        xanchor 0.5
        xpos min(max(position[0], int(tooltip_width / 2) + 50), config.screen_width - int(tooltip_width / 2) - 50)
        
        if position[1] < config.screen_height / 2:
            yanchor 0.0 ypos max(position[1], 0) + 50
        else:
            yanchor 1.0 ypos min(position[1], config.screen_height) - 50
                
        padding (25, 25, 25, 25)
        background Frame(Solid("#000000"))
        vbox:
            label title
            text description
                
python early:
    import string
    class inline_tooltip_data():
        """
        Data used to store the data to compare against and the strings to display for inline tooltips
        """
        def __init__(self, key, strings, title, description):
            """
            Set up the data for using the reactivity
            Parameters:
            -----------
            key : string
                The key used to identify this bit of data
            strings : string[]
                An array of strings to which this tooltip will apply
            title : string
                Title to be shown at the top of the tooltip
            description : string
                Description text to be shown in the tooltip
            """
            self.key = key
            self.strings = strings
            self.title = title
            self.description = description

        def replace_tooltip(self, text):
            for key in self.strings:
                if key in text and self.test_surrounding_index(text, key):
                    new_key = "{a=tooltip:" + self.key + "}" + key + "{/a}"
                    text = text.replace(key, new_key)
            
            return text

        def test_surrounding_index(self, text, key):
            start_index = text.index(key)
            end_index = start_index + len(key)
            
            if (start_index is 0 or text[start_index-1].isspace() or text[start_index - 1] in string.punctuation) and (end_index >= len(text) or text[end_index].isspace() or text[end_index] in string.punctuation):
                return True
            else:
                return False

init python:
    def hyperlink_style_selector(arg):
        if arg.split(':')[0] == "tooltip":
            return style.inline_tooltip
        else:
            return style.hyperlink_text

    def apply_inline_tooltip(text): 
        global inline_tooltip_list
        for tooltip in inline_tooltip_list:
            text = tooltip.replace_tooltip(text)
        return text

    def inline_tooltip_styler(*args):
        return style.inline_tooltip

    def inline_tooltip_hovered(*args):
        if args[0] is None:
            renpy.hide_screen("inline_tooltip")
        else:
            values = args[0].split(':')
            if values[0] == "tooltip":
                values = args[0].split(':')
                data = None
                for tooltip in inline_tooltip_list:
                    if tooltip.key == values[1]:
                        data = tooltip 
                
                renpy.show_screen("inline_tooltip", data.title, data.description, renpy.get_mouse_pos())
            else:
                style.hyperlink_text.hyperlink_functions[2]
        
        renpy.restart_interaction()

    def inline_tooltip_clicked(*args):
        if args[0] is not None:
            values = args[0].split(':')
            if values[0] != "tooltip":
                return hyperlink_function(args[0])
        return None
    
define config.say_menu_text_filter = apply_inline_tooltip
define config.hyperlink_styler = hyperlink_style_selector
