# General data used to craft responses

# list of adjectives that can be used
adjectives = (
    "bad",
    "good",
    "nice",
    "awesome",
    "cool",
    "terrible",
    "the best",
    "the worst",
    "astonishing",
    "brilliant",
    "beautiful",
    "acceptable",
    "amazing",

)

# translate the person and tense of a response
translation = {
    "am": "are",
    "was": "were",
    "I": "you",
    "I'd": "you'd",
    "I've": "you've",
    "I'll": "you'll",
    "my": "your",
    "are": "am",
    "you've": "I've",
    "you'll": "I'll",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}

# trigger words and responses to them
responses = (
    (("i", "need",),
     ("Why do you need %1?",
      "What do you need %1 for?")),

    (("i", "dont",),
     ("Why dont you %1?",
      "But I always %1!")),

    (("i", "like",),
     ("You like %1? What is your favourite thing about it?",
      "Do you like %1 often?")),

    (("why", "do", "you",),
     ("How did you know I %1?",
      "I %1 because I'm %a.",
      "If I couldn't %1, what would I do?")),

    (("why", "do",),
     ("I didn't know that %1, that's %a.",
      "%1 because it's possible.",
      "Why wouldn't that be the case?")),


    (("how", "are",),
     ("%1? %a!",
      "What do you think about %1?")),

    (("why",),
     ("Why not?",
      "Because that's how I like it.",
      "why do you think?",
      "%1?")),

    (("hello",),
     ("Hi, How are you feeling?",
      )),

    (("quit",),
     ("Bye.",
      "Have a nice day.")),
)

# generic responses
unknown = (
    "I don't understand.",
    "What does that mean?",
    "Tell me more.",
    "I need more information than that.",
    "Could you rephrase that?"
)

if __name__ == "__main__":
    print("This file cannot be run and only contains data.")
