package leetcode.lastStoneWeight;

import java.util.*;
import java.util.stream.Collectors;

public class LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> stoneQueue = new PriorityQueue<>(stones.length, (a, b) -> b - a);
        stoneQueue.addAll(Arrays.stream(stones).boxed().collect(Collectors.toList()));

        while (stoneQueue.size() >= 2) {
            int y = stoneQueue.poll();
            int x = stoneQueue.poll();

            int newStone = y - x;
            if (newStone > 0) {
                stoneQueue.offer(newStone);
            }
        }

        return stoneQueue.isEmpty() ? 0 : stoneQueue.poll();
    }
}
