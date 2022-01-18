'''
nltk nlp sentiment analysis test using vader
After: https://www.nltk.org/book/ch05.html
'''
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import nltk.data
nltk.download('vader_lexicon')

'''
Useful references:
http://text-processing.com/demo/tag/
https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
https://en.wikipedia.org/wiki/Inside–outside–beginning_(tagging)
https://github.com/cjhutto/vaderSentiment
https://stackoverflow.com/questions/40325980/how-is-the-vader-compound-polarity-score-calculated-in-python-nltk
https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664
'''

# Need 'Negative' text - we look to Marvin the Paranoid Android!!
sentences = ["Life? Don't talk to me about life.",
    "Here I am, brain the size of a planet, and they tell me to take you up to the bridge. Call that job satisfaction? 'Cos I don't.",
    "I think you ought to know I'm feeling very depressed. Pardon me for breathing, which I never do anyway so I don't know why I bother to say it, Oh God, I'm so depressed.",
    "You think you've got problems? What are you supposed to do if you are a manically depressed robot? No, don't try to answer that. I'm fifty thousand times more intelligent than you and even I don't know the answer. It gives me a headache just trying to think down to your level.",
    "And then, of course, I've got this terrible pain in all the diodes down my left side."
    ]

# Now positivity - from Happy - Pharrell Williams
happy = ["It might seem crazy what I am about to say \
Sunshine she's here, you can take a break \
I'm a hot air balloon that could go to space \
With the air, like I don't care, baby by the way",
"Huh (Because I'm happy) \
Clap along if you feel like a room without a roof \
(Because I'm happy) \
Clap along if you feel like happiness is the truth \
(Because I'm happy) \
Clap along if you know what happiness is to you \
(Because I'm happy) \
Clap along if you feel like that's what you wanna do",
"I said \
Clap along if you feel like a room without a roof \
(Because I'm happy) \
Clap along if you feel like happiness is the truth \
(Because I'm happy) \
Clap along if you know what happiness is to you \
(Because I'm happy) \
Clap along if you feel like that's what you wanna do \
Clap along if you feel like a room without a roof \
(Because I'm happy) \
Clap along if you feel like happiness is the truth \
(Because I'm happy) \
Clap along if you know what happiness is to you \
(Because I'm happy) \
Clap along if you feel like that's what you wanna do",
"Bring me down (Happy, happy, happy, happy) \
Can't nothing (Happy, happy, happy, happy) \
Bring me down, my level's too high \
To bring me down (Happy, happy, happy, happy) \
Can't nothing (Happy, happy, happy, happy) \
Bring me down",
]

print("Hello NLP - Vader Sentiments, see https://github.com/cjhutto/vaderSentiment\nScoring description: https://stackoverflow.com/questions/40325980/how-is-the-vader-compound-polarity-score-calculated-in-python-nltk\n")
print("What the scores mean:\n" \
"SentimentIntensityAnalyzer is an object and polarity_scores uses the following categories:\n" \
"Positive; Negative; Neutral; Compound\n" \
"The compound score is the sum of positive, negative & neutral scores which is then normalized between -1 (most extreme negative) and +1 (most extreme positive). " \
"The more Compound score closer to +1, the higher the positivity of the text.\n")

sentences.extend(happy)
for sentence in sentences:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{:-<15} {}, '.format(k, ss[k]))
    print()
