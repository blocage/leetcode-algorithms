

int addDigits(int num){
    return num ? 1 + (num - 1) % 9 : 0;
}