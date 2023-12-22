#include <iostream>
#include <fstream>
#include <map>

void read_input(int &full_cost,std::string &item_name, std::map<std::string, int> &item_stats);

int main(){
    int full_cost = 0;
    std::string item_name = "None";
    std::map<std::string, int> item_stats;
    std::map<std::string, int> reference_stats = {
        {"AD",35}, {"AP",21.75}, //Attack Damage and Ability Power
        {"AR",20}, {"MR",18}, //Armor and Magic Resistance
        {"HP",2.67}, {"MP",1.4}, //Health and Mana
        {"HP5",3}, {"MP5",5}, //Health Regen and Mana Regen
        {"CR",40}, {"AS",25}, //Critical Strike Chance and Attack Speed
        {"MS",12}, {"MS%",80}, //Flat and Percent Movement Speed
        {"LS",53.57},{"ARP",41.67}, //Life Steal and Armor Penetration
        {"MRP",31.11},{"MRP%",42.79}, //Flat and Percent Magic Penetration
        {"OH",21.67},{"AH",26.67}, //On-Hit Damage and Ability Haste
        {"HSP",68.75}, {"OV",39.67} //Heal and Shield Power and Omnivamp
    };

    read_input(full_cost, item_name, item_stats);
}

void read_input(int &full_cost,std::string &item_name, std::map<std::string, int> &item_stats){

}