def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount = 0
    for transaction in trans_list:
        if transaction.startswith("D:"):
            amount = int(transaction[2:])
            net_amount += amount
        elif transaction.startswith("W:"):
            amount = int(transaction[2:])
            net_amount += amount
    return net_amount

trans_list = ["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
