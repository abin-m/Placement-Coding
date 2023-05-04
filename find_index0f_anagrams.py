# # find the index of Anagrams
# #

# 1: create a dict
# 2: if sorted word not in dict,
#     set word key & index as Value
# 3: if sorted word in dictionary,append index for word.

def anagrams(A):
    if A == None:
        return
    else:
        dict = {}
        for i in range(len(A)):
            word = ''.join(sorted(A[i]))
            if word not in dict:
                dict[word] = [i+1]
            else:
                dict[word].append(i+1)
        return dict


A = ["cat", "dog", "tca", "act"]
print(anagrams(A))
# added
