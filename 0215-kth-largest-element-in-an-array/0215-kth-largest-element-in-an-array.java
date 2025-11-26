class Solution {
    public int findKthLargest(int[] nums, int k) {
        // 이진 힙으로 변환
        BinaryHeap maxHeap = new BinaryHeap();
        for (int i = 0; i < nums.length; i++) {
            maxHeap.insert(nums[i]);
        }
        // k번만큼 최대 값 추출
        for (int i = 0; i < k - 1; i++) {
            maxHeap.extract();
        }

        return maxHeap.extract();
    }
}

class BinaryHeap {

    public List<Integer> elems;

    public BinaryHeap() {
        elems = new ArrayList<>();
        elems.add(null);
    }

    public void swap(int i, int j) {
        int temp = elems.get(i);
        elems.set(i, elems.get(j));
        elems.set(j, temp);
    }

    // 업힙 연산
    public void percolateUp() {
        int idx = elems.size() - 1;
        int parentIdx = idx / 2;

        while (parentIdx > 0) {
            if (elems.get(idx) > elems.get(parentIdx)) {
                swap(idx, parentIdx);
            }
            idx = parentIdx;
            parentIdx /= 2;
        }
    }

    public void insert(int k) {
        // 신규 엘리먼트 추가
        elems.add(k);
        // 업힙 연산 수행
        percolateUp();
    }

    public void maxHeapify(int i) {
        int left = i * 2;
        int right = i * 2 + 1;
        int biggest = i;

        if (left <= elems.size() - 1 && elems.get(left) > elems.get(biggest)) {
            biggest = left;
        }
        if (right <= elems.size() - 1 && elems.get(right) > elems.get(biggest)) {
            biggest = right;
        }
        if (biggest != i) {
            swap(biggest, i);
            maxHeapify(biggest);
        }
    }

    public int extract() {
        int extracted = elems.get(1);

        elems.set(1, elems.get(elems.size() - 1));
        elems.remove(elems.size() - 1);
        maxHeapify(1);

        return extracted;
    }
}