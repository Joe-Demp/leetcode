package leetcode.unionfind;

/**
 * A data structure that tracks a set of elements partitioned into a number of disjoint subsets
 *
 * <p>
 * Operation {@code makeSet} is O(1).
 * Operation {@code find} and {@code union} are O(m * alpha(n)) for m disjoint-set operations on n elements, where
 * alpha is the inverse Ackermann function. alpha(n) < 5 for all n that can be written in this universe. Therefore,
 * {@code find} and {@code union} are essentially O(1).
 * </p>
 */
public interface IUnionFind {
    /**
     * Makes a new singleton set. If x is already present in the {@code IUnionFind}, the set will not be made.
     *
     * @param x the element that is to be the sole member of the new set.
     * @return {@code true} if a new set was made, {@code false} otherwise.
     */
    boolean makeSet(int x);

    /**
     * Returns the parent element of the subset that contains {@code x} in the {@code IUnionFind}. If x is not in the
     * {@code IUnionFind}, {@code Integer.MIN_VALUE} is returned. This should not be used as a flag, since getting this
     * value could simply mean that {@code Integer.MIN_VALUE} is the parent element of the subset that contains
     * {@code x}.
     *
     * @param x the element you wish to check for presence in a subset.
     * @return If x is present in the IUnionFind, the element denoted as <em>parent</em> for the disjoint set that
     * {@code x} belongs to. Otherwise {@code Integer.MIN_VALUE}.
     */
    int find(int x);

    /**
     * Joins the sets that the specified elements are members of. If the elements are members of the same sets, then
     * this method does nothing.
     *
     * @param x a member, identifying a set, to be unified with the set containing {@code y}
     * @param y a member, identifying a set, to be unified with the set containing {@code x}
     */
    void union(int x, int y);

    /**
     * Checks if the given element is present anywhere in the {@code IUnionFind}.
     *
     * @param x the element to check for membership.
     * @return {@code true} if {@code x} is present, {@code false} otherwise.
     */
    boolean contains(int x);
}
