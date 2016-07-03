import objsets._

val a_tweet = new Tweet("aa", "test1", 15)
val b_tweet = new Tweet("ba", "test2", 10)
val c_tweet = new Tweet("ca", "test3", 30)
val d_tweet = new Tweet("da", "test4", 2)
val e_tweet = new Tweet("ea", "test5", 6)
val a = new NonEmpty(a_tweet, new Empty, new Empty)
val twSet = a incl b_tweet incl c_tweet incl d_tweet incl e_tweet
val filteredSet = twSet.filter(t => t.retweets > 10)

twSet.descendingByRetweet foreach println

