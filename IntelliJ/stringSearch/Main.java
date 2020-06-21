package stringSearch;

import java.util.Arrays;

public class Main {
    public static final int ONE_HUNDRED_THOUSAND = 100_000;

    public static void main(String[] args) {
//        printRabinKarpResult("the quick brown fox jumps over the lazy dog", "row");

//        printLongestDuplicateSubstringResult("banana");
//        printLongestDuplicateSubstringResult("abcabcabca");

        String j10 = "jjjjjjjjjj";
        printLongestDuplicateSubstringResult(j10);
        printLongestDuplicateSubstringResult("abcd");

        String a100000 = "a".repeat(ONE_HUNDRED_THOUSAND);

        long start = System.currentTimeMillis();
        int lenLongDup = LongestDuplicateSubstring.longestDuplicateSubstring(a100000).length();
        long end = System.currentTimeMillis();

        System.out.println("The length of the longest duplicate substring in a100000 is: " + lenLongDup);
        System.out.println("That took: " + (end - start) + " milliseconds");
    }

    public static void printRabinKarpResult(String text, String sample) {
        int firstMatch = RabinKarp.rabinKarp(text, sample);

        if (firstMatch >= 0) {
            System.out.printf("The first instance of \"%s\" in \"%s\" is at index %d", sample, text, firstMatch);
        } else {
            System.out.printf("There is no instance of \"%s\" in \"%s\"", sample, text);
        }
        System.out.println("\n");
    }

    public static void printLongestDuplicateSubstringResult(String text) {
        String lds = LongestDuplicateSubstring.longestDuplicateSubstring(text);
        System.out.printf(
                "The longest duplicate substring in\n%s\nis\n%s\nof length: %d",
                text, lds, lds.length()
        );
        System.out.println();
    }
}
