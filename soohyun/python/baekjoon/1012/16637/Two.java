import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Two {
    /*
    로직을 참고한 문제 (참고사이트: https://11001.tistory.com/16)
    1. 괄호를 묶는 방법: 다음 수식을 미리 계산하고 현재 값과 더하거나,
    2. 괄호를 묶지 않는 방법: 현재 수식을 계산하는 방법
    3. 주의할점: 첫시작도 고려해야한다.
     */
    public static int[] num;
    public static char[] op;

    public static int calc(int num1, int num2, char op){
        if (op == '+') 
            return num1 + num2;
        else if (op == '-')
            return num1 - num2;
        else if (op == '*')
            return num1 * num2;
        return Integer.MIN_VALUE;
    }

    public static int dfs(int opIdx, int calcResult){
        //System.out.println(opIdx+" "+calcResult);
        int answer = Integer.MIN_VALUE;
        if(opIdx > op.length-1){
            return Math.max(answer, calcResult);
        }
        char operator = (opIdx == -1) ? '+' : op[opIdx];
        // 괄호미리묶기
        // 다음연산자를 미리 계산해놓고 현재 결과와 더해보기
        if (opIdx + 2 <= op.length){
            int bracket = calc(num[opIdx+1], num[opIdx+2], op[opIdx+1]);
            int curCalc = calc(calcResult, bracket, operator);
            int result = dfs(opIdx+2, curCalc);
            answer = Math.max(result, answer);
        }
        //괄호 미리 묶지 않고 계산하기
        int curCalc = calc(calcResult, num[opIdx+1], operator);
        int result = dfs(opIdx+1, curCalc);
        answer = Math.max(result, answer);

        return answer;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int length = Integer.parseInt(br.readLine());
        String calc = br.readLine();
        num = new int[(int)(length/2+1)];
        op = new char[(int)(length/2)];
        int answer = 0;

        // 숫자와 연산자 나누기
        for (int i = 0; i < length; i++){
            char character = calc.charAt(i);
            if (i%2 == 0)
                num[(int)(i/2)] = (int)(character - '0');
            else
                op[(int)(i/2)] = character;
        }

        //dfs 연산
        answer = dfs(-1, 0);
        System.out.println(answer);        


    }
    
}
