package date171212;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

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
			// int findIndex = BinarySearch(inputNums, input);

			inputNums.add(input);
			numForCount[input + 4000]++;

			sum += input;

		}
		Sort sort = new Sort();
		Collections.sort(inputNums, sort);
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
		int count = numForCount[small + 4000];
		for (int i = small + 4000; i <= big + 4000; i++) {
			if (numForCount[i] < count)
				continue;

			if (count < numForCount[i])
				sameCount.removeAll(sameCount);
			// int findIndex = BinarySearch(sameCount, i - 4000);
			sameCount.add(i - 4000);
			count = numForCount[i];
		}
		if (sameCount.size() > 1)
			return sameCount.get(1);
		else
			return sameCount.get(0);

	}

}

class Sort implements Comparator<Integer> {
	@Override
	public int compare(Integer arg0, Integer arg1) {
		// TODO Auto-generated method stub
		return arg0.compareTo(arg1);
	}
}
