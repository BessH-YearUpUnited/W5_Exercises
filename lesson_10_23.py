# var = 'house'

# print(var[0])
# print(var[0:2])
# print(var[2:-1])
# print(var[:-2])
# print(var[2:])
# print(var[-1:3])

# print(len(var))

# #  0  1  2  3  4
# #  H  O  U  S  E
# # -5 -4 -3 -2 -1

# groc_list = "milk, eggs, bunew_itemtter, cheese"
# # full_name = "Harriet Beecher Stowe"

# clean_list = groc_list.split(',')
# # print(clean_list)
# # print(type(clean_list))

# # # weird_list = groc_list.split('e')
# # # print(weird_list)

# # # survey_result = "nameBetty ClarknameJefferson JonesnameJim ThomasnameLee Van"
# # # print(survey_result.split('name'))

# print(clean_list)
# print(type(clean_list))
# item2 = clean_list[1].strip()
# item3 = clean_list[2].strip()
# item4 = clean_list[3].strip()
# print(clean_list[0], item2, item3, item4)


item_price = input('Price of item: ')

print("Item costs $" + item_price)

# discount_amt = item_price * .8

print(type(item_price))
check_value = 'FOUR'
print(check_value == item_price.upper())
#print(discount_amt)