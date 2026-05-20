# from collections import deque
# d=deque([1,2,3])
# d.append(4)
# d.appendleft(0)
# d.pop()
# d.popleft()
# d.rotate(1)
# print(d)


# from collections import Counter
# c=Counter("Hello")
# # print(c.most_common(2))
# c.update("World")
# print(c)

# from collections import defaultdict
# d=defaultdict(int)
# d['a']=1
# d['b']=2
# print(d['c'])
# print(d['d'])


# Questions-->

# 1)
# word count from the given sentense.

# from collections import Counter
# sentence = "the quick brown fox jumps over the lazy dog" 
# worlds=sentence.split()
# print(worlds)
# word_Count=Counter(worlds)
# print(word_Count)



# 2)
# from collections import Counter

# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] 
# count=Counter(data)
# print(count)
# print(count.most_common())


# 3)
# from collections import Counter
# s = "hello world" 
# count=Counter(s)
# print(count)
# print(count.most_common()[:-3:-1])   