f = open("count_log.txt", 'w', encoding="utf8")
for i in range(1, 11):
    data = "%dth line.\n" % i
    f.write(data)
f.close()

with open("count_log.txt", 'a', encoding='utf8') as f:
    for i in range(1, 11):
        data = "%dth line.\n" % i
        f.write(data)
