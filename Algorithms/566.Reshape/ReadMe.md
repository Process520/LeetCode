# 思路1
1.先把要输出的二维矩阵初始化好 ：List = [ [0 for x in row] for y in column] 
2.行‘之’型扫描原始矩阵，填入List。List[count/column][count%column] 

# 思路2
把原矩阵装变成单行：[1,2,...],再用slice每次截取row个元素，放入List。List动态增加[].


# python
1.L = [1,2]+[3,4].  L内容为：[1,2,3,4]  
2.定义二维矩阵：List = [ [0 for x in row] for y in column]
