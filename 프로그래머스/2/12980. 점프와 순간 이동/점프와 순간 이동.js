function solution(n) {
    let cnt = 1;
    while( n !== 1) {
        if(n % 2 === 0) n /= 2;
        else {
            n -= 1
            cnt++
        }
    }
    return cnt;
}
