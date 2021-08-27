# https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant/
from typing import List
def displayTable(orders: List[List[str]]) -> List[List[str]]:
    # step1获取所有餐品，用set，之后排序
    # step2遍历并获取所有的餐桌号，之后排序
    # step3遍历所有行，用dict: {table:{name1:num1,name2,num2}}来表示，dict[table_num][foor_name]来计数

    dict_foot_name = set()
    dict_table_num = set()
    for li in orders:
        if li[2] not in dict_foot_name:
            dict_foot_name.add(li[2])
        if li[1] not in dict_table_num:
            dict_table_num.add(int(li[1]))
    dict_foot_name = sorted(dict_foot_name)
    dict_table_num = sorted(dict_table_num)

    all_orders = {i:{j:0 for j in dict_foot_name} for i in dict_table_num}
    for li in orders:
        all_orders[int(li[1])][li[2]] += 1
    ans = []
    temp = ["Table"]
    for i in dict_foot_name:
        temp.append(i)
    ans.append(temp)
    for k in all_orders:
        temp = [str(k)]
        for d in all_orders[k]:
            temp.append(str(all_orders[k][d]))
        ans.append(temp)
    print(ans)
    return ans

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

displayTable(orders)