#tuple ->we cannot add or change
#type_of_accounts=("savings","current","credit","fixed")
#print(type_of_accounts)
#print(sorted(type_of_accounts))
#print(type_of_accounts[1:3])
#print(type_of_accounts[1], len(type_of_accounts))
#print(type_of_accounts.count("current"))
#reverse
#print(type_of_accounts[::-1])
#asc
#print(tuple(sorted(type_of_accounts)))
#s_acc=tuple(sorted(type_of_accounts))
#desc
#print(s_acc[::-1])
#t_acc=("saving",)
#print(type(t_acc))
#list we can add and change
'''
wc_teams=["india","australia","new zealand"]
wc_wins=[2,5,0]

wc_teams.append("srilanka")
wc_teams.insert(1,"west Indies")
wc_teams[4]="south africa"
wc_teams.extend(["nepal","banglore"])

for teams, wins in zip(wc_teams,wc_wins):
  print(teams,"won", wins,"worldcups")

teams=":".join(wc_teams) #converting list into string
print(teams)

wc_teams=["india","australia","new zealand","nepal","banglore"]

#wc_teams.sort()
#print(wc_teams)
#print(wc_teams[::-1]) descending 
#print(wc_teams[2:4])
wc_teams=["india","australia","new zealand","nepal","banglore"]
wc_teams.pop(1) -> list must have 1 arg as int, else it delete the last, but dict must have the arg "key"

#i_players=["rohit","sachin","rohit"]
#t_players=["dhoni","virat"]

#t_squad=[i_players,t_players]
#print(t_squad[0][1]) #i_players
#print(t_squad[1][1]) #t_players
#i_players.remove("rohit")
#print(i_players)
'''

#dict ->item cannot be accessed via index.
my_stocks={}#empty dict
my_stocks={"tcs":2700,"infosys":3400,"hsb":4500}
#print("stock price of tcs is ",my_stocks["tcs"])
my_stocks["sbi"]=1400 #add the item
#print("no of items", len(my_stocks))
#print("all stock name", my_stocks.keys())
#for stocks in my_stocks:
#    print(stocks)
 #   #print(stocks, "has price", my_stocks[stocks])

#for stocks in my_stocks.items():
 #   print(stocks)  #retun with key value in the tuple format by using items

#my_stocks.pop("tcs")
#my_stocks.popitem() #-> remove last item
 #del my_stocks["tcs"]
'''
swapped={}
for key, value in my_stocks.items():
    swapped[value]=key
print (swapped)
'''

#set - avoid duplicates, unique, but not in given order,union, intersection(common)
lucky_draws=set()
lucky_draw_o={7,9,4,3,8,6}
lucky_draw_s={2,5,10,12,9}
#lucky_draw_o.add(4)
#lucky_draw_o.discard(4)
#print("union",lucky_draw_o|lucky_draw_s)
#print("intersection",lucky_draw_o&lucky_draw_s)
print(lucky_draw_o)
print(lucky_draw_s)
print("difference",lucky_draw_o - lucky_draw_s) #remove the common numbers from both the sets and display value
set1={1,3,5}
set2={5,1,3}
set1==set2
#print(lucky_draw_s)

