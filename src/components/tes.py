


class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i, x in enumerate(temperatures):
            while st and x > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)

        return ans
    
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')