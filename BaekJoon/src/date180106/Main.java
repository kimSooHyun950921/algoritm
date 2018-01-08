package date180106;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		;

		ArrayList<Integer> inputs = new ArrayList<Integer>();
		boolean[] PrimeNums = new boolean[246920];
		Arrays.fill(PrimeNums, true);

		int singleInput = 0;
		int biggestInput = 0;

		while (true) {
			singleInput = Integer.parseInt(br.readLine());
			
			if (singleInput == 0)
				break;
			if (biggestInput < singleInput)
				biggestInput = singleInput;
			inputs.add(singleInput);
			/*bw.write(Integer.toString(findPrimeNum(singleInput))+"\n");
			bw.flush();*/
			
			
			
		}
		//bw.close();/*
		ArrayList<Integer> results = findPrimeNums(PrimeNums, inputs, biggestInput);
		for(int  i = 0; i<results.size();i++) {
			bw.write(Integer.toString(results.get(i))+"\n");
			bw.flush();}
		bw.close();

	}

	private static ArrayList<Integer> findPrimeNums(boolean[] primeNums, ArrayList<Integer> inputs, int biggestInput) {
		int primeIndex = 2;
		while (primeIndex < biggestInput*2) {
			for (int numberIndex = primeIndex+1; numberIndex < biggestInput*2; numberIndex+=1) {
				if (primeNums[numberIndex] && numberIndex % primeIndex == 0)
					primeNums[numberIndex] = false;
			}
			int i = primeIndex;
			do {i++;}while   (!primeNums[i]);
				
			primeIndex = i;
		}
		primeNums[2] = true;
		primeNums[1] = false;
		return countEachNumOfPrimes(primeNums, inputs);
	}

	private static ArrayList<Integer> countEachNumOfPrimes(boolean[] primeNums, ArrayList<Integer> inputs) {
		ArrayList<Integer> primeCounts = new ArrayList<Integer>();
		for (int i = 0; i < inputs.size(); i++) {
			int n = inputs.get(i);
			int count = 0;
			int untilN = 2*n;
			if(n==1)
				count=1;
			if(n%2!=0)
				n+=1;
			for (int j = n + 1; j <= untilN; j+=2) {
				if (primeNums[j])
					count++;
			}
			
			primeCounts.add(count);

		}
		return primeCounts;
	}


}
