list_days={"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}

year =1901
month =""
days =0
count=0
day_track=int(5)
while year < 2001:
    for days,months in enumerate(list_days):
        if days == 28:
            if year%4 ==0:
                days=29
            if year%100 ==0 and year%400 !=0:
                days=28
        day_track += int(days)%28
        day_track= day_track%7
        if day_track == 6:
            count +=1
    year+=1
print(count)
