# num1 = int(input("enter tehnum`1"))
# num2 = int(input("enter tehnum`2"))

# choice = input("enter operation ")

# if choice == "+":
#     print("addition" , num1 +num2)
# elif choice == "-":
#     print("sub" , num1 - num2)
# elif choice == "*":
#     print("mul" , num1 * num2)
# elif choice == "/":
#     print("div" , num1 / num2)


list_of_cloud = ["AWS" , "Azure" , "GCP" , "Oracle"]

print(list_of_cloud)

# add a new cloud
list_of_cloud.append("salesforce")
list_of_cloud.append("IBM cloud")
print(list_of_cloud)

list_of_cloud.insert(2, "Heruko")
print(list_of_cloud)

for i in list_of_cloud:
    print(i)

