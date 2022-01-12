def f(num:Int,arr:List[Int]):List[Int] = arr.flatMap(item => List.fill(num)(item))
