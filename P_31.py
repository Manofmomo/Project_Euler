amount=200
dict_coins={1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0}
for kitne,coin in enumerate(dict_coins):
    kitne=amount//coin
    dict_coins[coin]=kitne
print(dict_coins)
