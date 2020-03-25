#include<stdlib.h>
#include<stdio.h>
int main(){
    printf("Which File You wanna execute?\n");
    printf("press 1 for data.asm\n");
    printf("press 2 for data2.asm\n");
    printf("press 3 for data4.asm\n");
    char* cmd="python3 F1.py > out1.txt";
    system(cmd);
    printf("YOUR PHASE1 CODE HAS BEEN EXECUTED,OUTPUT IS SAVED IN FILE out1.txt, DO YOU WANT TO RUN PHASE2 CODE? [Y/N]");
    char ans;
    scanf("%c",&ans);
    if(ans=='N'){
        return 0;
    }
    char* cmd2="python3 run3.py > out2.txt";
    system(cmd2);
    printf("YOUR PHASE2 OUTPUT IS SAVED IN out2.txt.\n");
}
