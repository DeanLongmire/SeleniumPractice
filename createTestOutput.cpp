#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

enum PCLASS{FR,SO,JR,SR};

class player{
private:
    std::string firstName, lastName, position;
    int pclass, tds;
    float yards;

public:
    //contructors
    //default sets all elements to blank, zero, or unitinialized
    player() {firstName = ""; lastName = ""; position = ""; pclass = -1; tds = 0; yards = 0;}
    player(std::string fn, std::string ln, std::string p, int pc, int td, float y)
    {
        firstName = fn;
        lastName = ln;
        position = p;
        pclass = pc;
        tds = td;
        yards = y;
    }
    friend std::ostream& operator<<(std::ostream& output, const player& p);
};

std::ostream& operator<<(std::ostream& output, const player& p)
{
    output << std::setw(10) << std::left << p.firstName << std::setw(10) << std::left << p.lastName
    << std::setw(4) << std::left << p.position;
    switch(p.pclass)
    {
        case 0:
            output << std::setw(4) << std::left << "FR";
            break;
        case 1:
            output << std::setw(4) << std::left << "SO";
            break;
        case 2:
            output << std::setw(4) << std::left << "JR";
            break;
        case 3:
            output << std::setw(4) << std::left << "SR";
            break;
    }
    output << std::setw(4) << std::right << p.tds << std::setw(8) << std::right << p.yards << "\n";

    return output;
}

int main()
{
    std::string firstName, lastName, position;
    int pclass, tds;
    float yards;
    std::fstream file;

    std::vector<player> Players;

    do{
        printf("Please enter player firstname, lastname, position, class, total tds, and yards(0 to quit)\n");
        std::cin >> firstName;
        if(firstName == "0") break;
        std::cin >> lastName >> position >> pclass >> tds >> yards;
        std::cout << firstName << "\n";
        player P(firstName,lastName,position,pclass,tds,yards);
        Players.push_back(P);
    }while(1);

    file.open("sampleFile.txt");
    if(file.fail()) std::cerr << "File could not be found or failed to open.\n";

    std::vector<player>::iterator it;
    for(it = Players.begin();it != Players.end();it++)
    {
        file << *it;
    }
    file.close();
}