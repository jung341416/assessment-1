# write a function that takes two arguments item_cost, amount_paid
def optimal_change(item_cost, amount_paid):
    #declare template string which will be the first half of expected output string
    result_string_template = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is"
    #declare empty string which will go through loop and be the added to template string
    result_string_to_be_added = ""
    #declare change variable and round it up 2 decimals
    change = amount_paid -item_cost
    #make list of dictionaries for money string and money number for calculation
    moneys = [
        {"$20":20}, 
        {"$10":10} ,
        {"$5" :5}, 
        {"$1" :1}, 
        {"quarter": 0.25}, 
        {"dime": 0.1}, 
        {"nickle": 0.05}, 
        {"penny": 0.01}]
    #loop counter    
    loop_count = 0
    #make for loop 
    for index, money_dic in enumerate(moneys):
        for key in money_dic:
            #number value in money dictionary which will use for calculation
            money_amt = money_dic[key]
            #make while loop that run until the change is less than or equal to money to be handed
            while change >= money_amt:
                # make variable that will count amounts that need for each bill
                money_count = int(change // money_amt)
                change = round(change - (money_amt * money_count),2)
                loop_count = loop_count + 1
                #if money counnt is greater than 1 need plurals for each bill coin and penny cases 
                bill_count_plural_check = f"{' bills' if money_count > 1 else ' bill'}"
                coin_count_plural_check = f"{'s' if money_count > 1 else ''}"
                penny_plural_check = f"{'pennies' if key == 'penny' and money_count > 1 else 'penny'}"
                bill_or_coin_plural_check = bill_count_plural_check if index < 4 else coin_count_plural_check
                no_more_change = change == 0
                # change went only one loop then no need to add and still need to check coin or bill plural
                    # morethan one loop change end in coin then and comes before the end still need to check coin or bill plural
                    # change end in bill then and comes before the end still need to check coin or bill plural
                if key == 'penny' and loop_count == 1:
                    result_string_to_be_added += f" {money_count} {penny_plural_check}."
                elif no_more_change and loop_count == 1:
                    result_string_to_be_added += f" {money_count} {key}{bill_or_coin_plural_check}."
                elif not no_more_change:
                    result_string_to_be_added += f" {money_count} {key}{bill_or_coin_plural_check},"
                elif no_more_change and key != 'penny':
                    result_string_to_be_added += f" and {money_count} {key}{bill_or_coin_plural_check}."
                else:
                    result_string_to_be_added += f" and {money_count} {penny_plural_check}."
        
               
    return result_string_template + result_string_to_be_added
