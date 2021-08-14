# 习题4 变量和命名
cars = 100 # 总车数
space_in_a_car = 4.0 # 车的可容纳空间大小
drivers = 30 # 司机数量
passengers = 90 # 乘客数量
cars_not_driven = cars - drivers # 没被开走的车
cars_driven = drivers # 开走的车
carpool_capacity = cars_driven * space_in_a_car # 总容量
average_passengers_per_car = passengers / cars_driven # 平均每辆车有多个乘客

print("There are", cars, "cars avaiable.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "In each car.")
