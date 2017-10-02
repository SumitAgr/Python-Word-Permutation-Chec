def is_permutation(a, b):

    a_list = a.split()
    b_list = b.split()
    
    def a_list_length:
        for character in a_list:
            return (ord(a_list))

    def b_list_length:
        for character in b_list:
            return (ord(b_list))


    if a == b:
        print(a, "is a permutation of", b)
    elif len(a) == len(b):
        # added_list = a_list + b_list
        if a_list_length == b_list_length:
            print(a, "is a permutation of", b)
    else:
        print(a, "is not a permutation of", b)
