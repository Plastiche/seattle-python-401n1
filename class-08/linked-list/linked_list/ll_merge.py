def merge_list(a, b):

    current_a = a.head
    current_b = b.head

    while current_a and current_b:
        next_a = current_a.next
        next_b = current_b.next

        current_a.next = current_b

        if not next_a:
            break

        current_b.next = next_a

        current_a = next_a
        current_b = next_b

    return a


# current_a = mango
# current_b = kiwi
# next_a = None
# next_b = strawberry

# a = apple  orange     mango
#      |     /  |    /    |
# b = cherry  banana     kiwi -> strawberry -> pear
#                          
#
#  apple -> cherry -> orange -> banana ->mango -> kiwi

# apple -> cherry -> orange -> banana -> mango -> kiwi -> strawberry -> pear




# a = 1 -> 4 -> 8
# b = 3 -> 5
#      ^

# 1 -> 3 -> 4 -> 5 -> 8
