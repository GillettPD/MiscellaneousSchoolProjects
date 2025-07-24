#HW 3


import nltk
from nltk.corpus import movie_reviews


#find average word length in movie_reviews
word_list = [w for w in movie_reviews.words()]

length_list = [len(x) for x in word_list]

average = sum(length_list) / len(length_list)

print("the average word length is ", average)

#conditional frequency distribution

cfd = nltk.ConditionalFreqDist(
    (attit, word)
    for attit in movie_reviews.categories()
    for word in movie_reviews.words(categories=attit)
    )

cfd.tabulate(samples=["good", "bad", "awful", "no", "not"])

#check balancing of categories

pos_reviews = movie_reviews.fileids('pos')
neg_reviews = movie_reviews.fileids('neg')

pos_size = len(movie_reviews.words(fileids=pos_reviews))
neg_size = len(movie_reviews.words(fileids=neg_reviews))

print("the positive reviews contain a total of ", pos_size,
      " words, and the negative reveiws contain a totoal of ", neg_size,
      " words.")


#question 4
#out of the target words, "bad" and "awful" are fairly strong predictors of
#a negative review, but conversely, "good" is only a very weak predictor of
#a positive review, and "no" and "not" do not seem to have any strong predictive
#power, except perhaps "no" which is more strongly associated with negative
#reviews. This was surprising at first but makes sense upon reflection:
#positive reviews do not contain as much unique vocabulary as do negative ones,
#since negative reviews will often use positive vocabulary when denying those
#features were found in the movie in question.
