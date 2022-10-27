# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print(f"Leek is {str(leek_price)} euro per kilo.")

order_0 = "leek 4"
amount_0 = int(order_0[5])


sum_total = leek_price * amount_0
print(sum_total)


broccoli_price = 2.34
order_1 = 'broccoli 1.6'
amount_1 = float(order_1[9:12])
sum_total_1 = round(broccoli_price * amount_1, 2)


print(f"{amount_1}kg {order_1[0:8]} costs {sum_total_1}e")