package leetcode.validParenthesisString;

public class Main {
    public static final String in1 = "(*(()*((*)*()))"; // true
    public static final String in2 = "()()";    // true
    public static final String in3 = "(*)";
    public static final String in4 = "(*))";
    public static final String[] allInputs = {in1, in2, in3, in4};

    public static void main(String[] args) {
        for (String input : allInputs) runFunction(input);
    }

    public static void runFunction(String input) {
        boolean result = new ValidParenthesisString().checkValidString(input);
        System.out.printf("string: %s, %b\n", input, result);
    }
}
