# Write your solution here!
# creating function that takes two arguments:
def optimal_change(item_cost, amount_paid):

#Pseducode:
#create result string
    result_str = ""
#create change variable
    change = amount_paid - item_cost
#create the list of dictionary which will store bills data
    bill_data = [{
        "$20" : 20,
        "$10" : 10,
        "$5" : 5,
        "$1" : 1,
        "quarter" : 0.25,
        "dime" : 0.10,
        "Nickle" : 0.05,
        "penny" : 0.01
    }]
#create variable index which will track how many each bills needed
#print result string
    print(result_str)
pass
    