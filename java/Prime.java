class Prime {
	
	public static  boolean isPrime(int n) {
		
		if (n == 1) return false;
		for( int i = 2; i < n; i++ ) {
        	if( n % i == 0)
            	return false;
    	}	
		return true;
	}
	
	
	public static int addFirstFiftyPrimes(){
		int sum = 0;
		for( int i = 0 ; i < 50; i++ ){
			if(isPrime(i)){
				sum += i;
			}
		}
		return sum;
	}

	public static int addFirstNprimes(int n){
		
		int num = 0;
		int sum = 0; 
		
		for(int i = 0 ; i <= 50;){
			if(isPrime(num)){
				sum += num;
				num++;
				i++;		
			}else{
				num++;
			}
		}
		return sum;
	}

	public static void main(String[] args){	
		System.out.println("Add the first primes in rage of [0 - 50]: " + addFirstFiftyPrimes());
		System.out.println("Add of the first 50's primes is: " + addFirstNprimes(50));
	}
}

