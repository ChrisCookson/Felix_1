# ability to choose a random entry from list
from random import choice

# punctuation to remove
from string import punctuation

# import data on moods
import EmotionData as Emotion

# import data for general responses
import GeneralData as General


def constrain(number, minimum, maximum):
    # if number is less than min number = min
    if number < minimum:
        number = minimum

    # if number above max number = max
    elif number > maximum:
        number = maximum

    return number


def formatstring(string):
    # remove anything that is in the punctuation list from string
    out = "".join(i for i in string if i not in punctuation)

    # return string in lower case
    return out.lower()


# Class for main program
class Felix:
    def __init__(self):
        pass

    # method to respond to user input
    def respond(self, user_in):
        # split the sentence into list of words
        words = user_in.split(" ")

        if self.detect_emotion(words):
            # if emotion flag is in the word
            moods = self.analyse_mood(words)
            # find out what mood(s) are shown
            return self.craft_emotion_response(moods)
            # respond according to mood(s)

        # if a phrase is found
        elif self.find_phrases(words):
            # make a response from the words entered
            return self.craft_general_response(words, self.find_phrases(words))
        else:
            # if no response is found say a general response
            return choice(General.unknown)

    # takes in words and turns them into moods
    def analyse_mood(self, words):
        # score words based on mood ratings
        mood_scores = self.score_mood(words)
        # constrain scores to be within +-5 of 0
        x, y, z = [constrain(round(i), -5, 5) + 5 for i in mood_scores]
        # from values lookup mood on model
        moods = Emotion.responsesX[x], Emotion.responsesY[y], Emotion.responsesZ[z]
        # strip any blank moods(may not have a mood on certain axis)
        moods = [x for x in moods if x]

        return moods

    def craft_general_response(self, words, hit):
        # gather all words after the word that was a 'hit'
        extra = words[words.index(hit[0])+1:]

        # replace %1 with all words after the hit, replace %a with a random adjective
        response = choice(hit[1]).replace("%1", self.translate(extra)).replace("%a", choice(General.adjectives))
        return response

    @staticmethod
    def craft_emotion_response(moods):
        # pick a response that matches the number of moods detected
        response = choice(Emotion.diagnosis[len(moods)])

        # replace %1 with mood one and so on
        replacements = ("%1", "%2", "%3")

        # if not zero - if the mood was not neutral
        if len(moods) != 0:
            for i in range(0, len(moods)):
                # insert each replacement
                response = response.replace(replacements[i], moods[i])

        return response

    @staticmethod
    def translate(words):
        # string to append
        translation = ""
        for word in words:
            # for each word
            if word in General.translation:
                # if there is a translation in the dictionary
                translation += (General.translation[word])
                # join the translated word
            else:
                # else add the vanilla word
                translation += word
            translation += " "

        # get rid of trailing space (loop adds space at the end)
        translation = translation[:-1]
        return translation

    @staticmethod
    def detect_emotion(words):
        emotion_detected = False

        for word in words:
            if word in Emotion.moodFlags:
                # if any word is in mood flags
                emotion_detected = True

        return emotion_detected

    @staticmethod
    # searches for a response, if there is one returns the trigger word and possible responses
    def find_phrases(words):
        # for every possible response trigger
        for i in range(0, len(General.responses)):
            # if all the triggers are in the word list
            if set(General.responses[i][0]).issubset(set(words)):
                return General.responses[i][0][-1], General.responses[i][1]

        return False

    @staticmethod
    def score_mood(words):
        # scores for mood start neutral
        x, y, z = 0, 0, 0

        # default modifier controls range of mood score
        default_modifier = 0.8

        modifier = default_modifier
        # for each word
        for word in words:
            # if the word is a modifier (not, very etc.)
            if word in Emotion.modifiers:
                # alter the modifier value
                modifier *= Emotion.modifiers[word]
            else:
                # if its not a modifier score it based on known moods
                if word in Emotion.emotionXRank:
                    x += modifier * Emotion.emotionXRank[word]
                    # reset the modifier to default
                    modifier = default_modifier

                if word in Emotion.emotionYRank:
                    y += modifier * Emotion.emotionYRank[word]
                    # reset the modifier to default
                    modifier = default_modifier

                if word in Emotion.emotionZRank:
                    z += modifier * Emotion.emotionZRank[word]
                    # reset the modifier to default
                    modifier = default_modifier

        return x, y, z


def startup():
    print("""
------------------------------
You are now talking to Felix:
He is a little emotional-
go easy on him.
Say quit to leave
------------------------------
""")

    # start as if user said hello
    user_in = "hello"

    # end when user types quit
    while user_in != "quit":
        print("Felix: " + Felix().respond(user_in))
        print("You: ", end="")
        user_in = formatstring(input())


if __name__ == "__main__":
    startup()