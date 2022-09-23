class Stack:
    def __init__(self,fixed_size=0):
        self.__data = []
        self.__fixed_size=fixed_size
    def isEmpty(self):
        if len(self.__data)==0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.__data)==self.__fixed_size:
            return True
        else:
            return False
    def show(self):
        print(self.__data)
    def push(self, value):
        if self.isFull():
            return
        elif type(value)==str:
            self.__data.append(value)

        else:
            print('Nonvalid type')

    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.__data.pop()

    def length(self):
        return len(self.__data)
    def clear(self):
        self.__data=[]
st=Stack(5)
st.show()
st.push('sad')
st.push('sa')
st.push('d')
st.push('d')
st.push('d')
st.push('d')
st.pop()
st.pop()
st.pop()
st.show()
st.clear()
st.show()