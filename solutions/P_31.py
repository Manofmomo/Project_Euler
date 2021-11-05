amount=200
dict_coins={1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0}
for kitne,coin in enumerate(dict_coins):
    kitne=amount//coin
    dict_coins[coin]=kitne
print(dict_coins)
count=0
# dict_coins=sorted(dict_coins,reverse=True)
# for kitne,coin in enumerate(dict_coins1):
#     summu=0
#     summu+=coin*kitne
#     if summu==amount:
#         count+=1
#     if summu<amount:
