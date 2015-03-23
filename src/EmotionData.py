# Words that may hint an emotion is present
moodFlags = ["i'm", "im", "feeling", "feel", "mood", "am"]

# possible categories for X axis mood
responsesX = ("furious", "hateful", "angry", "upset", "irritated",
              "",
              "agitated", "aroused", "excited", "thrilled", "ecstatic")

# ranking for emotions on X axis
emotionXRank = {

    "furious": -5,
    "hateful": -4,
    "angry": -3,
    "upset": -2,
    "irritated": -1,

    "agitated": 1,
    "aroused": 2,
    "excited": 3,
    "thrilled": 4,
    "ecstatic": 5,

    # Additional Values
    "enraged": -5,
    "frantic": -4,
    "frightened": -4,
    "emotional": -3,
    "exhausted": -2,
    "restless": -1,

    "anxious": 1,
    "nervous": 2,
    "good": 3,
    "eager": 3,
    }

# possible categories for Y axis moods
responsesY = ("despairing", "depressed", "sad", "lonely", "bored",
              "",
              "pleased", "joyful", "happy", "delighted", "content")

# rankings for emotions on Y axis
emotionYRank = {
    "despairing": -5,
    "depressed": -4,
    "sad": -3,
    "lonely": -2,
    "bored": -1,

    "pleased": 1,
    "joyful": 2,
    "happy": 3,
    "delighted": 4,
    "content": 5,
    

    # Additional Values
    "bitter": -5,
    "dismal": -5,
    "mournful": -4,
    "bad": -3,
    "melancholy": -3,
    "somber": -3,
    "glum": -1,
    "moody": -1,

    "cheerful": 1,
    "merry": 2,
    "chirpy": 3,
    "good": 3,
    "elated": 4,
}

# possible categories for Z axis
responsesZ = ("afraid", "distressed", "insecure", "scared", "anxious",
              "",
              "delicate", "sympathetic", "friendly", "loving", "tender")

# # ranking for emotions on Z axis
emotionZRank = {
    "afraid": -5,
    "distressed": -4,
    "insecure": -3,
    "scared": -2,
    "anxious": -1,

    "delicate": 1,
    "sympathetic": 2,
    "friendly": 3,
    "loving": 4,
    "tender": 5,

    # Additional Values
    "stressed": -4,
    "bad": -3,
    "uneasy": -2,
    "nervous": -1,

    "timid": 1,
    "shy": 2,
    "caring": 3,
}

# words that change the meaning of following words
modifiers = {
    "bit": 0.8,
    "slightly": 0.7,
    "little": 0.6,
    "tiny": 0.4,

    "very": 1.9,
    "really": 1.4,
    "quite": 1.2,

    "not": -0.4,
    "never": -0.9,
    "dont": -0.9,
}

# responses to detected emotion(s)R
diagnosis = (
    # no mood
    ("You seem fairly neutral.",
     "I cant detect any overall emotion."),

    # one mood
    ("You sound %1.",
     "Are you %1?",
     "Do you feel %1?",
     "Why, do you feel %1?",),

    # two moods
    ("I think you sound %1, are you %2?",
     "Does feeling %1 make you feel %2?",
     "I think you are %1 and %2.",),

    # three moods
    ("You seem to be %1, %2 and %3.",
     "What is making you %1, %2 and %3?",),
)

if __name__ == "__main__":
    print("This file cannot be run and only contains data.")