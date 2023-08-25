first_name = "Brian"
last_name = "Mathenge"

output1 = "Hello, " + first_name + ' ' + last_name
print(output1)

output2 = "Hello, {} {}".format(first_name, last_name)
print(output2)

output3 = "Hello, {0} {1}".format(first_name, last_name)
print(output3)

output4 = f"Hello, {first_name} {last_name}"
print(output4)