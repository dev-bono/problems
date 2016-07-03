import objsets._

val first_tweet = new Tweet("aa", "test", 0)
val tweetSet1 = new NonEmpty(first_tweet, new Empty, new Empty)
val filteredSet = tweetSet1.filter(first_tweet => first_tweet.retweets > 10)

