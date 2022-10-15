"""Madlibs Stories."""


class Story:
    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            val = f'<b>{val}</b>'
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ['country','adverb','adjective','animal','verb_ending_in_ing','verb','verb_ending_in_ing_2','adverb_2','adjective_2','place','type_of_liquid','body_part','verb_2'],
    """If you are traveling in {country} and find yourself having to cross a piranha-filled river, here's how to do it {adverb}:\n -Piranhas are more {adjective} during the day, so cross the river at night.\n -Avoid areas with netted {animal} traps as piranhas may be {verb_ending_in_ing} there looking to {verb} them!\n -When {verb_ending_in_ing_2} the river, swim {adverb_2}. You don't want to wake them up and make them {adjective_2}!\n -Whatever you do, if you have an open wound, try to find another way to get back to the {place}. Piranhas are attracted to fresh {type_of_liquid} and will most likely take a bite out of your {body_part} if you {verb_2} in the water"""
)
story3 = Story(
    ['adjective','nationality','person','noun','adjective_2','noun_2','adjective_3','adjective_4','plural_noun','noun_3','number','shapes','food','food_2','number_2'],
    """Pizza was invented by a {adjective} {nationality} chef named {person}. To make a pizza, you need to take a lump of {noun}, and make a thin, round {adjective_2} {noun_2}. Then you cover it with {adjective_3} sauce, {adjective_4} cheese, and fresh chopped {plural_noun}. Next you have to bake it in a very hot {noun_3}. When it is done, cut it into {number} {shapes}. Some kids like {food} pizza the best, but my favorite is the {food_2} pizza. If I could, I would eat pizza {number_2} times a day!"""
)
stories = [story1,story2,story3]