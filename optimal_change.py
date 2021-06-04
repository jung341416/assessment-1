# Write your solution here!
# creating function that takes two arguments:
def optimal_change(item_cost, amount_paid):

#Pseducode:
#create result string
    result_str_one = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is"
    result_str_two = ""
#create the list of dictionary which will store bills data
    bill_data_one = [
        {"$20" : 20},
        {"$10" : 10},
        {"$5" : 5},
        {"$1" : 1},
        ]
    bill_data_two =  [
        {"quarter" : 25},
        {"dime" : 10},
        {"Nickle" : 5},
        {"penny" : 1},
        ]
# create variable index which will track how many each bills needed
# iterate throught the list and get the key and number value and store it variables
#create change variable
    change = amount_paid - item_cost
    change = str(change).split('.')
    change_one = int(change[0])
    change_two = int(change[1])
    
    for dic in bill_data_one:
        for key in dic:
            bill_str = key
            bill_int = dic[key]
            count = int(change_one // bill_int) 
            countPlural = f"{'bills' if count > 1 else 'bill'}"
            if change_one >= bill_int:
                change_one = change_one - (bill_int * count)                
                result_str_one += f" {count} {bill_str} {countPlural},"
    
    for dic in bill_data_two:
        for key in dic:
            bill_str = key
            bill_int = dic[key]
            count = int(change_two // bill_int)
            plural = f"{'s' if count > 1 else ''}"
            if change_two > bill_int:
                change_two = change_two - (bill_int * count)
                if(key == "penny"):
                    result_str_two += f" and {count} pennies."
                else:
                    result_str_two += f" {count} {bill_str}{plural},"            
            

#print result string
    if change_two != None:
        print(result_str_one + result_str_two) 
    else: 
        print(result_str_one)


