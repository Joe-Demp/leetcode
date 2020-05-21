package leetcode.validParenthesisString;

/**
 * This solution was not completed by me
 *
 * @author leetcode
 */
class ValidParenthesisString {
    /*
    A valid string is a balanced string.
    Balance:
    The balance at point i is the number of extra open left brackets in the string from index 0 to index (i - 1)

    Consider "(***)"
    balance("(") = [1]
    balance("(*") = [0, 1, 2]
    balance("(**") = [0, 1, 2, 3]
    balance("(***") = [0, 1, 2, 3, 4]
    balance("(***)") = [0, 1, 2, 3]

    These states are always contiguous
     */

    public boolean checkValidString(String s) {
        /*
        lo = the smallest possible number of open left brackets
        hi = the largest possible number of open left brackets
         */
        int lo = 0, hi = 0;
        for (char c: s.toCharArray()) {
            /*
            lo++ If '(' is encountered then the minimum number of open left brackets surely increases by 1
            lo-- If anything else is encountered, then we could have written a ')'
            Since we are getting the minimum, we assume every * is a ')' and close the respective '('
             */
            lo += c == '(' ? 1 : -1;
            /*
            hi++ If something that can be a '(' is encountered then the max number of open '(' increases
            hi-- If ')' appears, it must serve to close a potential '('
             */
            hi += c != ')' ? 1 : -1;
            /*
            If hi < 0, then the preceding sequence can not be made valid under any circumstances
             */
            if (hi < 0) break;
            /*
            We can never have less than 0 open '(' (logically)
             */
            lo = Math.max(lo, 0);
        }
        /*
        At the end there should be exactly 0 open '('
         */
        return lo == 0;
    }
}
