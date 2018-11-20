#include <iostream>
using namespace std;


bool has7(int n) {
   if (n < 10) return n == 7;
   return (n%10 ==7 or has7(n/10));
}

int isDivisible(int num){

    if (num < 100){
        if (has7(num)) return 2;
        return 1;
    }
    else {
        int num_petit = num%10;
        int num_gran = num/10;

        num_petit = num_petit *2;
        int new_num = num_gran - num_petit;
	//cerr << new_num << "  " << has7(new_num) << endl;
        if (has7(new_num)){
            return 2 + isDivisible(new_num);
        }
        else{
            return 1 + isDivisible(new_num);
        } 

    }
}

int main (){

    int x; cin >> x;
    for (int i = 0; i < x; ++i){
        int n; cin >> n;
        int res = isDivisible(n);
       	cout << "Case #" <<  i+1 <<  ": " << res  << endl;
    }

}
