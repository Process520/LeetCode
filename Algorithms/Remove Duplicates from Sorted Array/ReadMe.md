#思路
1.逐个处理list数据时，注意如果第0个、第1个、第n-1个元素，直接从第1个遍历与前面比较，扫描指针可以从1到len(list);从0往后比较则，扫描指针从0到len(list)-1. 
2.逐个处理list，要考虑空集的case

#python知识点
1.for i in range(1,len(list_)):
2.list(set(list_)),  传list参数时，要改变list_,则需要这样调用：list[:] = ....;list[i] = a
