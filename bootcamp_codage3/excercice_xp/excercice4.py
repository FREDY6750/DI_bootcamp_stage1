disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)
disney_users_C = {}
sorted_users = sorted(users)
for i, user in enumerate(sorted_users):
    disney_users_C[user] = i
print(disney_users_C)
disney_users_A = {}
for i, user in enumerate(users):
    if "i" in user:
        disney_users_A[user] = i
print(disney_users_A)
disney_users_A = {}
for i, user in enumerate(users):
    if user[0] in ["m", "p"]:
        disney_users_A[user] = i
print(disney_users_A)
