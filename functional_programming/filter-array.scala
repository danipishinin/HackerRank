def f(delimiter: Int, arr: List[Int]): List[Int] = {
  val l = scala.collection.mutable.ListBuffer.empty[Int]
  arr.foreach(i => {
    if (i < delimiter) l += i
  })
  
  l.toList
}