class A(object):
    NAME = 'akshar'
def search(search_term, strings):
    for term in strings:
        if search_term in term:
            yield term

#strings = ['abc is good', 'bad', 'sad is bad', 'cde is after abc']
#results = search("abc", strings)
#for result in results:
    #print result

def dedup(input):
    seen = []
    for each in input:
        if each not in seen:
            seen.append(each)
            yield each


def bubble_sort(seq, key=None):
    # How will this work with dict?
    seq_len = len(seq)
    num_iterations = seq_len - 1
    for iteration in range(num_iterations):
        for index in range(seq_len-1):
            value = seq[index]
            value = value if not key else key(value)
            next_value = seq[index+1]
            next_value = next_value if not key else key(next_value)
            if value > next_value:
                seq[index], seq[index+1] = seq[index+1], seq[index]
    return seq

def str_p(s):
    print s

str_p(s='ab\
cd')