# 思路. 
1.首先最大的数不可能算入和式，那把第二大的数与其组合在一起即可  
2.把数组排好序，取0，2，4。。。这些序号的元素和即可。

# python知识点. 
1.sorted（list）返回一个新的排好序的数组.   
2.求和可以用while依次把对应好加起来，也可以用sum(list[::2])
