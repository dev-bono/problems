package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }

    println("Excercise 2")
    println(balance("((daf)ddd(dfdfddd))".toList))
    println(balance("(()))".toList))
    println(balance("))((".toList))
    println(balance("dddd()dd(()".toList))
    println(balance("d(dd)d)d)d(d(".toList))
    println(balance("aaaaa((aaaa)aaaa)aaaa(aaf)".toList))

    println("Excercise 3")
    println(countChange(4, List(1, 2)))
    println(countChange(6, List(1, 2))) // 111111, 11112, 1122, 222
    println(countChange(5, List(1, 3))) // 11111, 113
    println(countChange(8, List(1, 3))) // 11111111, 111113, 1133
  }

  /**
    * Exercise 1
    * 역으로 추적해가는 방식
    * 왼쪽 또는 오른쪽 끝에 도달한 경우에는 무조건 1
    */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0) 1
    else if (c == r) 1
    else
      pascal(c - 1, r - 1) + pascal(c, r - 1)
  }

  /**
    * Exercise 2
    * '('로 시작하는 경우에 startCount를 + 1
    * ')'로 시작하는 경우에 startCount를 - 1
    * startCount가 마이너스가 되면 false
    * chars가 empty가 되었을 때 startCount가 0이 아니면 false
    * 좀더 줄일수 있을 듯
    */
  def balance(chars: List[Char]): Boolean = {
    def loop(remainChars: List[Char], startCount: Int): Boolean = {
      if (remainChars.isEmpty)
        startCount == 0
      else {
        val c = remainChars.head
        val calStartCount = getStartCount(c, startCount)
        if (calStartCount >= 0) loop(remainChars.tail, calStartCount)
        else false
      }
    }

    def getStartCount(headChar: Char, startCount: Int): Int = {
      if (headChar == '(') startCount + 1
      else if (headChar == ')') startCount - 1
      else startCount
    }

    loop(chars, 0)
  }

  /**
    * Exercise 3
    * https://gist.github.com/ngocdaothanh/3764694https://gist.github.com/ngocdaothanh/3764694
    * 참고함, recursive 어렵네
    * 즉, (money에서 첫번째 coin을 뺀 금액, 원래 coin 리스트) + (money, coin 리스트에서 첫번째를 삭제한 리스트)을 recursive하게 호출
    *
    */
  def countChange(money: Int, coins: List[Int]): Int = {
    if (money < 0 || (money > 0 && coins.isEmpty)) 0
    else if (money == 0) 1
    else
      countChange(money-coins.head, coins) + countChange(money, coins.tail)
  }
}
