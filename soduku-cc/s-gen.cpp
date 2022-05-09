#include <iostream>
#include <list>
#include <ctime>
#include <algorithm>
#include <string>

struct FIELD{
    int field[9][9];
    bool solved = false;
    bool visible[9][9];
    FIELD(){
        for (int i =0; i <9; i++){
            for (int k =0; k <9; k++){
                field[i][k] = 0;
                visible[i][k]=false;
            }
        }
    };
};
struct SEED{
    std::list<int> seed_vertical;
    std::list<int> seed_horizontal;
};

void printfield(FIELD field, bool all){
    std::cout<<std::endl;
    for (int i =0; i <9; i++){
        for (int k =0; k <9; k++){
            if(field.visible[i][k] || all){
                std::cout<<field.field[i][k]<<"  ";
            }
            else std::cout<<"   ";
            if (k == 2|| k == 5) std::cout<<"|  ";
        }
        std::cout<<std::endl;
        if (i == 2|| i == 5){ 
        for(int m = 0; m<=10; m++) std::cout<<"-  ";
        std::cout<<std::endl;}  
    }
    std::cout<<std::endl;
}


bool inlist(std::list<int> list,int item){
    bool found =std::find(list.begin(), list.end(), item) != list.end();
    return found;
}

bool iscorrect(int y, int x, int num, FIELD field){
    for (int i=0; i<9; i++){
        if (field.field[y][i] == num) return false;
        if (field.field[i][x] == num) return false;
    }
    int x0 = (x/3)*3;
    int y0 = (y/3)*3;
    for (int i=0; i<3; i++){
        for (int k=0; k<3; k++){
            if (field.field[y0+i][x0+k] == num) return false;
        }
    }
    return true;
}

FIELD solve(FIELD field){
    for (int i = 0; i < 9; i++){
        for (int k = 0; k <9; k++){
            if (field.field[i][k] == 0){
                for (int sub = 1; sub<=9; sub++){
                    if(iscorrect(i,k,sub,field)){ 
                        field.field[i][k]=sub;
                            if (i == 8 && k==8) {
                                field.solved = true;
                                return field;
                            }
                            field = solve(field); 
                    }
                }
                if (field.solved==false){
                    field.field[i][k] = 0;
                    return field;}
    
            }
        }
    }
    return field; 
}
   
FIELD fill( SEED seed){
    FIELD field;

    for (int i=0; i<9; i++){
        int num = seed.seed_vertical.front();
        field.field[i][0]= num;
        seed.seed_vertical.pop_front();

        if (i!=0){
        num = seed.seed_horizontal.front();
        field.field[0][i]= num;
        seed.seed_horizontal.pop_front();
        }
    }
    return field;
}

FIELD set_visible(FIELD field, int limit){
    int loc = limit/9;
    limit--;

    do{
        for (int i = 0; i < 9; i+=3){
            for (int k = 0; k <9; k+=3){
                int loclim = loc;
                for (int i0 = 0; i0 < 3; i0++){
                    for (int k0 = 0; k0 <3; k0++){   
                        if(std::rand()%2 && limit >=0 && loclim >=0 && not field.visible[i+i0][k+k0]){
                            limit--;
                            loclim--;
                            field.visible[i+i0][k+k0] = true;
                        }
                    }
                }
            }
        }
    }
    while(limit >= 0);
    return field;
}

SEED ranseed (){
    std::list<int> seed;
    int p_num = 0;
    int count = 0;
    std:: list<int> repeat = {0, 0, 0, 0, 0};

    do{
        int num = std::rand()%9 + 1;
        count = 0;
        for (int i : seed) if(i == num) count++;
        if (seed.size()>1 && count >=2 || inlist(repeat, num)) continue;
        if(repeat.size()>=8) repeat.pop_front();
        repeat.push_back(num);
        seed.push_back(num);
    }
    while(seed.size() <= 17);

    SEED output;

    for (int i = 0; i < 9; i++){
        int num = seed.front();
        output.seed_vertical.push_back(num);
         seed.pop_front();
    }
    for (int i = 0; i <8; i++){
        int num = seed.front();
        output.seed_horizontal.push_back(num);
        seed.pop_front();
    }
    output.seed_vertical.reverse();
    return output;
}

int main (){
    srand(std::time(NULL));
    SEED seed = ranseed();
    FIELD field = fill(seed);
    std::cout<<"Input number of clues: ";
    int lim;
    std::cin>> lim;
    std::cout<< std::endl;
    field = solve(field);
    field = set_visible(field, lim);
    printfield(field, false);
}