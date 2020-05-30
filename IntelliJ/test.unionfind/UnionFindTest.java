package leetcode.unionfind;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

class UnionFindTest {
    static UnionFind emptyUnionFind;
    static UnionFind fullUnionFind;

    static int[] numbers = {0, 1, 2, 6, 3, 9, 13, 14, 22, 57};

    static final int NON_MEMBER_NUMBER = 99;

    @BeforeEach
    void beforeEach() {
        emptyUnionFind = new UnionFind();
        fullUnionFind = new UnionFind();

        for (int i : numbers) {
            fullUnionFind.makeSet(i);
            if (i == NON_MEMBER_NUMBER) {
                throw new RuntimeException("OTHER_NUMBER is present in 'numbers'. The test class is broken.");
            }
        }
    }

    @Test
    void makeSet() {
        assertFalse(emptyUnionFind.contains(NON_MEMBER_NUMBER));
        assertTrue(emptyUnionFind.makeSet(NON_MEMBER_NUMBER));
        assertTrue(emptyUnionFind.contains(NON_MEMBER_NUMBER));

        assertFalse(emptyUnionFind.makeSet(NON_MEMBER_NUMBER));

        int someNumber = numbers[5];

        assertTrue(fullUnionFind.makeSet(NON_MEMBER_NUMBER));
        assertFalse(fullUnionFind.makeSet(someNumber));

        assertTrue(fullUnionFind.contains(NON_MEMBER_NUMBER));
        assertTrue(fullUnionFind.contains(someNumber));
    }

    @Test
    void findElementNotIn() {
        assertFalse(emptyUnionFind.contains(Integer.MIN_VALUE));
        assertEquals(Integer.MIN_VALUE, emptyUnionFind.find(1));
    }

    @Test
    void unionFindOne() {
        int x = 9;
        int y = 14;

        assertEquals(x, fullUnionFind.find(x));
        assertEquals(y, fullUnionFind.find(y));
        assertNotEquals(x, y);

        fullUnionFind.union(x, y);
        assertEquals(fullUnionFind.find(x), fullUnionFind.find(y));
    }

    @Test
    void unionFindMany() {
        int[] numbersToUnion = Arrays.copyOfRange(numbers, 5, numbers.length);
        int first = numbersToUnion[0];

        for (int num : numbersToUnion) {
            assertEquals(num, fullUnionFind.find(num));
            fullUnionFind.union(first, num);
        }

        int parent = fullUnionFind.find(first);
        for (int num : numbersToUnion) {
            assertEquals(parent, fullUnionFind.find(num));
        }

        assertNotEquals(fullUnionFind.find(numbers[0]), fullUnionFind.find(parent));
    }

    @Test
    void contains() {
        int someInt = new Random().nextInt();
        assertFalse(emptyUnionFind.contains(someInt));

        someInt = new Random().nextInt(numbers.length);
        int someNumber = numbers[someInt];
        assertTrue(fullUnionFind.contains(someNumber));

        Random rand = new Random();
        do {
            someInt = rand.nextInt();
        } while (numbersHas(someInt));
        assertFalse(fullUnionFind.contains(someInt));
    }

    private static boolean numbersHas(int x) {
        for (int i : numbers) {
            if (i == x) {
                return true;
            }
        }
        return false;
    }
}