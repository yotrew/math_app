#Yotrew 20251011
#高斯消去法 Gaussian_elimination
import pprint
import math
v_n=int(input("請輸入變數個數:").strip())
matrix=[] #增廣矩陣 Augmented Matrix
row=1
while row <= v_n:
    nums=input(f"請輸入第{row}列元素,之間使用空格隔開,(ex.1 2 3):")
    nums=nums.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")
    nums=nums.split(" ")
    nums=list(map(int,nums))
    #print(nums)
    if len(nums)!=v_n+1:
        print(f"第{row}輸入錯誤,請重新輸入")
        continue
    matrix.append(nums)
    row+=1
base_col=0
for row in range(v_n):
    flag=False
    for other_row in range(1,v_n):
        o_row=(other_row+row)%v_n
        #求2列之間第row元素的最小公倍數
        lcm=math.lcm(matrix[row][base_col],matrix[o_row][base_col])
        
        if lcm==0:#
            continue
        sign=1
        flag=True
        factor1=lcm//matrix[row][base_col]   #第row列和要相約列各要乘以多少才會相等
        factor2=lcm//matrix[o_row][base_col]

        #第row列的第row欄元素與第o_row列的第row欄元素相同符號就用減,相異就用加的
        if matrix[row][base_col]*factor1>=matrix[o_row][base_col]*factor2:
            sign=-sign
        
        tmp=[x*(factor1) + y*(factor2)*sign for x, y in zip(matrix[row], matrix[o_row])]
        #print(f"lcm={lcm},base_col={base_col},row={row},o_row={o_row}")
        matrix[o_row]=tmp
    print(matrix)
    if flag:
        base_col+=1
    print("-"*50)
#print(matrix)
#solution=[None for _ in range(v_n)] #rank(簡化矩陣)=rank(增廣矩陣)=v_n才有唯一解
#對各列約分
for row in range(v_n):
    #Ref:https://stackoverflow.com/questions/29194588/python-gcd-for-list
    gcd=math.gcd(*matrix[row]) #求各列中所有元素的最大公因數
    #print(f"row={row+1},gcd={gcd}")
    if gcd==0:
        #solution[row]=f"{matrix[row][v_n]}/{matrix[row][row]}"
        continue
    if matrix[row][row]!=0 and matrix[row][row]//gcd<=0:
        gcd=-gcd

    tmp=[x//gcd for x in matrix[row]]
    matrix[row]=tmp
    #solution[row]=f"{matrix[row][v_n]}/{matrix[row][row]}={matrix[row][v_n]/matrix[row][row]}"
print(f"解為:")
pprint.pprint(matrix)
