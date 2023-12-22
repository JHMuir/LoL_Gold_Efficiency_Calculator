import re 

def read_input():
    """
    This function simply reads and saves data from input.txt
    How it is saved is dependent on how input.txt is formatted
    
    rtype:
    full_cost_item: int
    item_name: str
    item_stats: list[(int, str)]
    """
    item_stats = []  
    with open('input.txt', 'r') as input:
        for i in input.readlines():
            tmp = i.split(',')
            #We check if the line starts with a symbol. The way it is saved is determined by that symbol.
            try: 
                if tmp[0].startswith("#"):
                    tmp[0] = tmp[0].replace("#","")
                    full_cost_item = int(tmp[0])
                    print("HERE!")
                    continue
                if tmp[0].startswith("$"):
                    tmp[0] = tmp[0].replace("$","")
                    item_name = str(tmp[0])

                    continue
                for j in tmp:
                #We seperate our stats line into a tuple of int and str
                    match = re.match(r"([0-9]+)([a-z]+)", j, re.I)
                    if match:
                        stats = match.groups()
                        #We append that tuple into our stats list
                        item_stats.append(stats)
            except:
                print("Please format the input correctly. See the README.md")
    return full_cost_item, item_name, item_stats


def gold_eff_algo(stats_item, full_cost_item, reference_stats):
    """
    This function does some basic math to find the gold efficiency.
    THe formula used is: gold efficiency = (sum gold value / item price) * 100
    stats_item: list[(int, str)]
    full_cost_item: int
    reference_stats = dict[str:int]
    
    rtype: float
    """
    sum = 0
    for i in range(0, len(stats_item)):
        #Multiply the item's stats by how each point of that stat is worth, using the reference items.
        sum = sum + (reference_stats[stats_item[i][1]] * int(stats_item[i][0]))
    #We divide that sum bu the full cost of the item, and multiply it by 100 to get our final value.
    try:
        gold_eff = (sum / full_cost_item) * 100
    except ZeroDivisionError:
        print("Error! The total cost must not be equal to or less than zero.")
        exit()
    return gold_eff
    

def main():
    #initializing our reference dictionary with how much a single point of a stat is worth
    reference_stats = {
        "AD":35, "AP":21.75, #Attack Damage and Ability Power
        "AR":20, "MR":18, #Armor and Magic Resistance
        "HP":2.67, "MP":1.4, #Health and Mana
        "HP5":3, "MP5":5, #Health Regen and Mana Regen
        "CR":40, "AS":25, #Critical Strike Chance and Attack Speed
        "MS":12, "MS%":80, #Flat and Percent Movement Speed
        "LS":53.57,"ARP":41.67, #Life Steal and Armor Penetration
        "MRP":31.11,"MRP%":42.79, #Flat and Percent Magic Penetration
        "OH":21.67,"AH":26.67, #On-Hit Damage and Ability Haste
        "HSP":68.75, "OV":39.67 #Heal and Shield Power and Omnivamp
        
    }
    
    full_cost_item, item_name, item_stats = read_input()
    gold_eff = gold_eff_algo(item_stats, full_cost_item, reference_stats)
    format_gold_eff = "{:.2f}".format(gold_eff)
    print(f"The gold efficiency of {item_name} is {format_gold_eff}%")

if __name__ == "__main__":
    main()