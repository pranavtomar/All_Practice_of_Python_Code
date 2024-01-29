def cost(str1):
    st = str1.replace("(","").replace(")","").strip()
    str2 = st.split(",")
    cost = int(str2[0]) * int(str2[1])
    return cost

def calculate_cost(str):
    chocolates = str.split(") ")

    for chocolate in chocolates:
        str = chocolate.split(" : (")
        cost1 = cost(str[1])
        print(str[0],"price:",cost1)
   

str = "Dairy Milk : (41,21) 5 Star : (31,15) fantacy : (13,22)"
calculate_cost(str)

