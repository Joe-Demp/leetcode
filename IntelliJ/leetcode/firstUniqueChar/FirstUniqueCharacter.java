package leetcode.firstUniqueChar;

public class FirstUniqueCharacter {
    public int firstUniqChar(String s) {
        int alphaLen = 26;
        int[][] alpha = new int[alphaLen][2];

        int len = s.length();
        for (int i = 0; i < len; i++) {
            int currentIndex = s.charAt(i) - 'a';

            alpha[currentIndex][0]++;
            if (alpha[currentIndex][0] == 1) {
                alpha[currentIndex][1] = i;
            }
        }

        int minIndex = len;
        for (int i = 0; i < alphaLen; i++) {
            if (alpha[i][0] == 1) {
                minIndex = Integer.min(minIndex, alpha[i][1]);
            }
        }
        return minIndex < len ? minIndex : -1;
    }
}
