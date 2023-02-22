from sys import stdout

userLimit, serviceLimit, duration = map(int, input().split())
systemLoad = {}
userLoad = {}

while True:
    req = input()
    if req == "-1":
        break

    time, userId = map(int, req.split())
    status = "200"
    if not userLoad.get(userId):
        userLoad[userId] = {}

    for t in systemLoad.copy().keys():
        if t + duration < time:
            del systemLoad[t]

    for t in userLoad[userId].copy().keys():
        if t + duration < time:
            del userLoad[userId][t]

    if sum(userLoad[userId].values()) >= userLimit:
        status = "429"
    else:
        userLoad[userId][time] = userLoad[userId].get(time, 0) + 1

    if status == '200':
        if sum(systemLoad.values()) >= serviceLimit:
            status = "503"
            userLoad[userId][time] = userLoad[userId].get(time, 0) - 1
        else:
            systemLoad[time] = systemLoad.get(time, 0) + 1

    if len(userLoad[userId]) == 0:
        del userLoad[userId]

    print(status)
    stdout.flush()
