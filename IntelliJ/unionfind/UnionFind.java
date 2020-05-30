package leetcode.unionfind;

import java.util.HashMap;
import java.util.Map;

// todo consider using an array to store child-parent relationships i.e. parent[i] holds the parent of element i.

public class UnionFind implements IUnionFind {
    Map<Integer,Element> elements = new HashMap<>();

    @Override
    public boolean makeSet(int k) {
        if (contains(k)) {
            return false;
        }
        elements.put(k, new Element(k));
        return true;
    }

    @Override
    public int find(int k) {
        if (!contains(k)) {
            return Integer.MIN_VALUE;
        }

        // Using path-halving to flatten the structure of the tree
        // Every other node on the path is made point to its grandparent
        Element current = elements.get(k);
        while (current != current.parent) {
            current.parent = current.parent.parent;
            current = current.parent;
        }
        return current.id;
    }

    @Override
    public void union(int x, int y) {
        if (!(contains(x) && contains(y))) {
            return;
        }

        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            Element rootXElement = elements.get(rootX);
            Element rootYElement = elements.get(rootY);

            // Ensure rootX has the larger rank
            // i.e. the rootYElement should point to the rootXElement
            if (rootXElement.rank < rootYElement.rank) {
                Element temp = rootXElement;
                rootXElement = rootYElement;
                rootYElement = temp;
            }

            rootYElement.parent = rootXElement;
            if (rootXElement.rank == rootYElement.rank) {
                rootXElement.rank++;
            }
        }
    }

    @Override
    public boolean contains(int k) {
        return elements.containsKey(k);
    }

    private static class Element {
        int id;
        Element parent;

        // For a leaf, 0. For any other Element, 1 + the max rank of the children.
        int rank = 0;

        public Element(int x) {
            this.id = x;
            this.parent = this;
        }
    }
}
