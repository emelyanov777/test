object StringProcessor {
  def processStrings(strings: List[String]): List[String] = {
    val result = strings // убрал пустой список, цикл for и if т.к не соотв. функц.программированию
      .filter(str => str.length > 3)  // фильтруем строки по длине
      .map(str => str.toUpperCase)  // переводим в верхний регистр
    result
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
