emoji = '\U0001f600'

for num in range(1, 11):
	print(emoji * num)

for num in range(1, 11):
	smileys = ""
	for i in range(0, num):
		smileys += emoji
	print(smileys)

num = 1
while num < 11:
	print(emoji * num)
	num += 1

num = 1
while num < 11:
	i = 0
	smileys = ""
	while i < num:
		smileys += emoji
		i += 1
	print(smileys)
	num += 1
