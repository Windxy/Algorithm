# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
#
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
#
# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。
#
# 实现 MyCalendar 类：
#
# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/my-calendar-i
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from sortedcontainers import SortedDict
class MyCalendar:
    # TreeMap（有序字典/有序数组） + 二分
    def __init__(self):
        self.dict = SortedDict()

    def book(self, start: int, end: int) -> bool:
        idx = self.dict.bisect_left(end)  # 找到待预定时间end后的第一个已定日程的索引
        if idx == 0:
            self.dict[start] = end
            return True
        if self.dict.items()[idx-1][1] <= start:     # 如果前面一个日程的结尾，正好小于start，满足要求
            self.dict[start] = end
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)