package date171212;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		/*
		 * input을받으면서 binarySearch를 통해 index할 위치 찾기 똑같은 숫자가 나왔다면 특정값을 리턴해 빈도수를 위한
		 * arrayList에 넣어준다.
		 *
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> inputNums = new ArrayList<Integer>();
		int[] numForCount = new int[8001];
		// ArrayList<Integer> numForCount = new ArrayList<Integer>();
		int smallestNum = 0;
		int biggestNum = 0;

		long sum = 0;
		double sansulAvg = 0;
		int middleVal;
		int countVal;
		int range;

		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());
			int findIndex = BinarySearch(inputNums, input);

			inputNums.add(findIndex, input);
			numForCount[input + 4000]++;

			sum += input;

		}
		smallestNum = inputNums.get(0);
		biggestNum = inputNums.get(inputNums.size() - 1);

		sansulAvg = (double) sum / (double) N;
		middleVal = inputNums.get((inputNums.size() - 1) / 2);
		countVal = findCountVal(numForCount, biggestNum, smallestNum);
		range = biggestNum - smallestNum;

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(Math.round(sansulAvg) + "\n");
		bw.write(middleVal + "\n");
		bw.write(countVal + "\n");
		bw.write(range + "\n");
		bw.flush();
		bw.close();

	}

	private static int findCountVal(int[] numForCount, int big, int small) {
		ArrayList<Integer> sameCount = new ArrayList<Integer>();
		int count = numForCount[small+4000];
		for (int i = small+4000; i <= big+4000; i++) {
			if (numForCount[i] < count)
				continue;
			
			
			if (count < numForCount[i])
				sameCount.removeAll(sameCount);
			int findIndex = BinarySearch(sameCount, i - 4000);
			sameCount.add(findIndex, i - 4000);
			count = numForCount[i];
		}
		if(sameCount.size()>1)
			return sameCount.get(1);
		else
			return sameCount.get(0);
		

	}

	private static int BinarySearch(ArrayList<Integer> inputNums, int input) {
		// TODO Auto-generated method stub
		int first = 0;
		int last = inputNums.size() - 1;
		int middle = (first + last) / 2;
		int index = 0;
		if (inputNums.size() == 0)
			return 0;
		if (inputNums.get(first) > input)
			return 0;
		else if (inputNums.get(last) < input)
			return inputNums.size();
		while (last - first > 1) {
			boolean isSameWithInput = inputNums.get(middle) ==input  || inputNums.get(first)==input || inputNums.get(last) ==input;
			if (isSameWithInput) {
				index = -1;
				break;
			}
			if (inputNums.get(middle) > input)
				last = middle;

			else if (inputNums.get(middle) < input)
				first = middle;

			middle = (first + last) / 2;
		}
		index = last;
		return index;
	}

}
