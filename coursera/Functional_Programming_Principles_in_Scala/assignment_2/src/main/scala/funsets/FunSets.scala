package funsets


/**
  * 2. Purely Functional Sets.
  */
object FunSets {
  /**
    * We represent a set by its characteristic function, i.e.
    * its `contains` predicate.
    * 여기서 Set은 스칼라의 기본 자료구조인 Set이 아니다.
    * Int 입력을 받으면 Boolean 타입을 리턴하는 함수를 나타내는 타입의 이름(alias)일 뿐이다.
    */
  type Set = Int => Boolean

  /**
    * Indicates whether a set contains a given element.
    */
  def contains(s: Set, elem: Int): Boolean = s(elem)

  /**
    * Returns the set of the one given element.
    * 위의 contains 함수를 이용한다
    * singletonSet은 우측의 익명함수를 결과값으로 가지는 Set이므로
    * 해당셋을 인자로 받는 contains 함수에서의 두번째 파라미터인 elem은 x와 같다 (s(elem)을 보면 알수 있다)
    */
  def singletonSet(elem: Int): Set = (x: Int) => elem == x

  /**
    * Returns the union of the two given sets,
    * the sets of all elements that are in either `s` or `t`.
    * union 함수는 인자로 들어온 두 셋의 값들을 하나로 합쳐서 새로운 셋을 return 하는 함수이다.
    * 그러므로 s에 속하거나 t에 속하는 모든 요소들이 새로운 Set 타입의 요소가 될 수 있다.
    */
  def union(s: Set, t: Set): Set = (x: Int) => contains(s, x) || contains(t, x)

  /**
    * Returns the intersection of the two given sets,
    * the set of all elements that are both in `s` and `t`.
    * intersect 함수는 인자로 들어온 두 셋의 값들 중 공통된 것만 요소로 하는 새로운 셋을 return하는 함수이다
    * s에 속하고 t에도 역시 속하는 공통된 요소만 모아서 새로운 Set이 만들어진다.
    */
  def intersect(s: Set, t: Set): Set = (x: Int) => contains(s, x) && contains(t, x)

  /**
    * Returns the difference of the two given sets,
    * the set of all elements of `s` that are not in `t`.
    * 비슷함, s에는 속하고 t에는 속하지 않는 Set
    */
  def diff(s: Set, t: Set): Set = (x: Int) => contains(s, x) && !contains(t, x)

  /**
    * Returns the subset of `s` for which `p` holds.
    * 필터는 s Set 중에서 p 조건에 맞는 요소들을 추출해서 subset을 리턴하는 함수
    * intersect와 같은 기능을 한다
    */
  def filter(s: Set, p: Int => Boolean): Set = (x: Int) => contains(s, x) && contains(p, x)


  /**
    * The bounds for `forall` and `exists` are +/- 1000.
    */
  val bound = 1000

  /**
    * Returns whether all bounded integers within `s` satisfy `p`.
    */
  def forall(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      if (a > bound) true
      else if (contains(s, a) && !contains(p, a)) false
      else iter(a + 1)
    }
    iter(-bound)
  }

  /**
    * Returns whether there exists a bounded integer within `s`
    * that satisfies `p`.
    */
  def exists(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      if (a > bound) false
      else if (contains(s, a) && contains(p, a)) true
      else iter(a + 1)
    }
    iter(-bound)
  }

  /**
    * Returns a set transformed by applying `f` to each element of `s`.
    */
  def map(s: Set, f: Int => Int): Set = (x: Int) => exists(s, (y: Int) => f(y) == x)

  /**
    * Displays the contents of a set
    */
  def toString(s: Set): String = {
    val xs = for (i <- -bound to bound if contains(s, i)) yield i
    xs.mkString("{", ",", "}")
  }

  /**
    * Prints the contents of a set on the console.
    */
  def printSet(s: Set) {
    println(toString(s))
  }
}
