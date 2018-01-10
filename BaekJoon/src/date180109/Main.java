package date180109;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int input;
		ArrayList<Integer> PrimeNum = findPrimeNum();
		for(int i = 0; i<N;i++) {
			input = Integer.parseInt(br.readLine());
			String result = findPrimesSsang(input,PrimeNum);
			bw.write(result+"\n");
			bw.flush();
			
			
		}
		bw.close();

	}

	private static String findPrimesSsang(int input, ArrayList<Integer> primeNum) {
		int primeIndex = input/2;
		int firstNum = 0;
		int secondNum = 0;
		while(firstNum+secondNum!=input) {
			while(primeNum.get(primeIndex)==0) primeIndex--;
			firstNum = primeNum.get(primeIndex);
			secondNum = input-firstNum;
			if(primeNum.get(secondNum)==0) {
				firstNum--;
				primeIndex = firstNum;
			}			
		}
		
		return firstNum+" "+secondNum;
	}

	private static ArrayList<Integer> findPrimeNum() {
		ArrayList<Integer> primes = new ArrayList<Integer>();
		primes.add(0,0);
		primes.add(1,0);
		primes.add(2,2);
		boolean isPrime = true;
		for(int i = 3; i<10000;i++) {
			for(int j = 2;j<i;j++) {
				if(i%j==0) {isPrime=false;primes.add(i,0);break;}
			}
			if(isPrime) primes.add(i,i);
			isPrime=true;
		}					
		return primes;
	}

}
