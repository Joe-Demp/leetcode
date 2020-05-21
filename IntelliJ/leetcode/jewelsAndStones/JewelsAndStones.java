package leetcode.jewelsAndStones;

import java.util.HashSet;
import java.util.Set;

public class JewelsAndStones {
    Set<Character> jewels;

    public int numJewelsInStones(String J, String S) {
        int numberOfJewels = J.length();
        jewels = new HashSet<>(numberOfJewels);
        for (int i = 0; i < numberOfJewels; i++) {
            jewels.add(J.charAt(i));
        }

        int numberOfStones = S.length();
        int countJewels = 0;
        for (int i = 0; i < numberOfStones; i++) {
            if (jewels.contains(S.charAt(i))) {
                countJewels++;
            }
        }
        return countJewels;
    }
}
