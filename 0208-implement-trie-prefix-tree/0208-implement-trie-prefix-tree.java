class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        char[] parts = word.toCharArray();
        TrieNode node = root;
        for (int i = 0; i < parts.length; i++) {
            int index = parts[i] - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        char[] parts = word.toCharArray();
        TrieNode node = root;
        for (int i = 0; i < parts.length; i++) {
            int index = parts[i] - 'a';
            if (node.children[index] != null) {
                node = node.children[index];
            } else {
                return false;
            }
        }
        if (node.isEnd) {
            return true;
        } else {
            return false;
        }
    }
    
    public boolean startsWith(String prefix) {
        char[] parts = prefix.toCharArray();
        TrieNode node = root;
        for (int i = 0; i < parts.length; i++) {
            int index = parts[i] - 'a';
            if (node.children[index] == null) {
                return false;
            }
            node = node.children[index];
        }
        return true;
    }
}

public class TrieNode {
    boolean isEnd;
    TrieNode[] children = new TrieNode[26];
}



/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */