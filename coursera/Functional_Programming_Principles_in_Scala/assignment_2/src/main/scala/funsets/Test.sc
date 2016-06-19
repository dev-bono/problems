object FunSets {
  type Set = Int => Boolean
  def contains(s: Set, elem: Int): Boolean = s(elem)
  def singletonSet(elem: Int): Set = (x: Int) => elem == x
  def union(s: Set, t: Set): Set = (x: Int) => contains(s, x) || contains(t, x)
  def intersect(s: Set, t: Set): Set = (x: Int) => contains(s, x) && contains(t, x)
  def diff(s: Set, t: Set): Set = (x: Int) => contains(s, x) && !contains(t, x)
  val bound = 1000
  def exists(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      if (a > bound) false
      else if (contains(s, a) && contains(p, a)) true
      else iter(a + 1)
    }
    iter(-bound)
  }

  def map(s: Set, f: Int => Int): Set = (x: Int) => exists(s, (y: Int) => f(y) == x)
//  def union(s: Set, t: Set): Set = s + t

}

import FunSets._

val setA = singletonSet(3) // 3
setA(3)
val setB = singletonSet(4) // 4
setB(4)

val setC = union(setA, setB) // 3, 4
setC(3)
setC(4)

val setD = intersect(setA, setC) // 3
setD(2)

val setE = diff(setC, setB) // 3
setE(4)

val setF = map(setC, x => x+2)
setF(7)