from __future__ import print_function
import random

buzz = ('continuous testing', 'continuous integration',
        'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
           'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


def sample(l, n=1):
    result = random.sample(l, 2)
    if n == 1:
        return result[0]
    return result


def generateBuzz():
    buzzTerms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzzTerms[0], sample(adverbs),
                       sample(verbs), buzzTerms[1]])
    return phrase.title()


if __name__ == "__main__":
    print(generateBuzz())
