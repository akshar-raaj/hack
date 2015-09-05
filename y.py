def balanced_paranthesis(s):
    num_open = 0
    num_closed = 0
    for each in s:
        if each == '{':
            num_open = num_open + 1
        elif each == '}':
            num_closed = num_closed + 1
        if num_closed > num_open:
            return False
    if num_open != num_closed:
        return False
    return True

def permutation(li, r):
    stack = []
    if r==1:
        stack = [[each] for each in li]
        return stack
    if r:
        r = r-1
    if len(li)==1:
        return [li]
    else:
        for i, each in enumerate(li):
            left_list = li[:i]
            right_list = li[i+1:]
            left_list = left_list + right_list
            result = [e for e in permutation(left_list, r)]
            for res in result:
                res.insert(0, each)
                stack.append(res)
        return stack

def permutation_helper(li, r=None):
    if r and r>len(li):
        print("You can't arrange %d elements out of %d elements." % (r, len(li)))
        return
    else:
        return permutation(li, r)

result = permutation_helper(['a', 'b', 'c', 'd', 'e'], 5)

def create_lists(num):
    num = 3
    lists = []
    for each in num:
        '}}}'
        '{}}'
        '{{}'
        open_paranthesis = '{' * each
        closed_paranthesis = '}' * (num-each)
        final_string = open_paranthesis + closed_paranthesis
        lists.append(final_string)


#print balanced_paranthesis("{{}}"), True
#print balanced_paranthesis("{}}}"), False
#print balanced_paranthesis("{}{{"), False