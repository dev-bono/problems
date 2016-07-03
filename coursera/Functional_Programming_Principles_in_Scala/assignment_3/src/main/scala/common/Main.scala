package common

import objsets._

/**
  * Created by blueshw on 2016. 6. 26..
  */
object Main {

  val set1 = new Empty
  val set2 = set1.incl(new Tweet("d", "da body", 18))
  val set3 = set2.incl(new Tweet("b", "b body", 20))
  val c = new Tweet("c", "c body", 29)
  val d = new Tweet("db", "d body", 26)
  val set4c = set3.incl(c)
  val set4d = set3.incl(d)
  val set5 = set4c.incl(d)
  val e = new Empty
  val set6 = set5 union e

  def main(args: Array[String]) = {
    val first_tweet = new Tweet("aa", "test", 0)
    val tweetSet1 = new NonEmpty(first_tweet, new Empty, new Empty)
    val filteredSet = tweetSet1.filter(tw => tw.user == "a")

//    println(set4d union set5)
//    println(set5.mostRetweeted)
//    println(set6.descendingByRetweet.foreach(t => println(t.text)))
  }
}
