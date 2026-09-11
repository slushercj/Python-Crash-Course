guest_list = ["Napoleon", "Julius Caesar", "Nietzsche"]

invitation = "Please come to my dinner, "

guest_list.insert(0, "Albert Einstein")
guest_list.insert(2, "Yennefer")
guest_list.append("Walter White")

print(invitation + guest_list[0])
print(invitation + guest_list[1])
print(invitation + guest_list[2])
print(invitation + guest_list[3])
print(invitation + guest_list[4])
print(invitation + guest_list[5])

print("\nI can only invite 2 people to my dinner")
message = "Sorry, I don't have space for you "
print(message + guest_list.pop())
print(message + guest_list.pop(0))
print(message + guest_list.pop(0))
print(message + guest_list.pop(1))

message = "You're on the invitation list. Welcome, "
print(message + guest_list[0])
print(message + guest_list[1])

del guest_list[0]
del guest_list[0]

print(guest_list)