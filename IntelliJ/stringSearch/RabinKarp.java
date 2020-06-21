package stringSearch;

import static java.lang.Math.floorMod;

/**
 * A simple class to implement the Rabin-Karp pattern matching algorithm.
 * This version supports strings with characters ['a', 'b', 'c', ..., 'z']
 * BASE = the size of the alphabet
 */
public class RabinKarp {
    public static final int BASE = 26;
    public static final int N = 7919;

    private static int baseToThePowerOfSampleLength;

    /**
     * Finds the first occurrence of {@code sample} in {@code text}
     *
     * @return If {@code sample} is a substring of {@code text}, the zero based index of the first character of the
     * instance of {@code sample} in {@code text}. Else -1.
     */
    public static int rabinKarp(String text, String sample) {
        int[] hashes = hashes(text, sample.length());
        int hashOfSample = singleHash(sample);

        for (int i = sample.length() - 1; i < text.length(); i++) {
            if (hashOfSample == hashes[i]) {
                int startOfSuspectedMatch = i - sample.length() + 1;
                if (stringCompare(sample, text, startOfSuspectedMatch)) {
                    return startOfSuspectedMatch;
                }
            }
        }
        return -1;
    }

    public static boolean stringCompare(String sample, String text, int startIndex) {
        int i = 0, j = startIndex;
        int sampleLen = sample.length();
        int textLen = text.length();

        while (i < sampleLen && j < textLen && sample.charAt(i) == text.charAt(j)) {
            i++;
            j++;
        }
        return i == sampleLen;
    }

    public static int[] hashes(String text, int sampleLen) {
        int[] hashes = new int[text.length()];
        hashes[sampleLen - 1] = singleHash(text.substring(0, sampleLen));
        setBaseToThePowerOfSampleLength(sampleLen);

        int textLen = text.length();
        for (int i = sampleLen; i < textLen; i++) {
            int formerHash = hashes[i - 1];

            // Math.floorMod used here to turn negative operands into positives
            //  e.g. -1 % 5 = -1 but floorMod(-1, 5) = 4

            int lastCharValue = floorMod(baseToThePowerOfSampleLength * text.charAt(i - sampleLen), N);
            int lessTheLastChar = floorMod(formerHash - lastCharValue, N);
            hashes[i] = floorMod(lessTheLastChar * BASE % N + text.charAt(i), N);
        }

        return hashes;
    }

    public static int singleHash(String str) {
        int hash = 0;

        for (int i = 0; i < str.length(); i++) {
            hash = (hash * BASE) % N + str.charAt(i);
        }
        return hash;
    }

    private static void setBaseToThePowerOfSampleLength(int sampleLen) {
        int result = 1;
        for (int i = 0; i < sampleLen - 1; i++) {
            result *= BASE;
            result %= N;
        }
        baseToThePowerOfSampleLength = result;
    }
}
