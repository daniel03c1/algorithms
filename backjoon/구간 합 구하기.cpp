// 2019.2.14
// 2024번 문제
// SegTree...
#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <functional>

template<typename T>
struct SegTree {
    std::vector<T> tree;
    std::vector<int> indices;
    std::function<T(T, T)> op;
    int n, cur;
    
    // left node = node * 2 + 1
    // right node = (node+1) * 2
    
    SegTree(int n_leaf, int init, std::function<T(T, T)> bop) {
        n = n_leaf;
        op = std::move(bop);
        cur = 0;
        
        if(n_leaf > 0) {
            // total # of nodes = 2^(log2(N)+1) - 1
            int height = std::ceil(std::log2(n_leaf));
            tree.assign(((1 << (height+1)) - 1), init);
            indices.assign(n_leaf, -1);
        }
    }
    
    /*
     해당 idx에 새 값을 넣는다. 여기서 idx는 실제 트리에서 인덱스가 아니고,
     leaf 모드들 중에서 indx를 의미한다.
     */
    bool update(int idx, T newValue) {
        // out of bound...
        if(idx < 0 || idx >= n)
            return false;
        
        T value;
        int low = 0, high = n-1, cur = 0;
        int parent;
        bool changed;
        
        // real index already found
        if(indices[idx] != -1) {
            cur = indices[idx];
        }
        // not found...
        else {
            while(low <= high) {
                // match
                if(low == high) {
                    // check whether the value must be updated...
                    indices[idx] = cur;
                    break;
                }
                // go left
                if(idx <= (low+high)/2) {
                    cur = cur * 2 + 1;
                    high = (low+high)/2;
                }
                // go right
                else {
                    cur = (cur + 1) * 2;
                    low = (low+high)/2 + 1;
                }
            }
        }
        
        if(tree[cur] != newValue) {
            tree[cur] = newValue;
            changed = true;
        } else {
            changed = false;
        }
        
        while(cur > 0 && changed) {
            parent = (cur - 1)/2;
            value = op(tree[parent*2 + 1], tree[(parent+1)*2]);
            
            // update
            if(tree[parent] != value) {
                tree[parent] = value;
                cur = parent;
            } else {
                changed = false;
            }
        }
        
        return true;
    }
    
    /*
     @param: _low -> 연산에 쓰일 lower bound... recursive이기 때문에 그냥 0으로 두면 된다.
     _high-> 위와 비슷. 그냥 n-1로 두면 된다.
     _cur -> tree에서 cur 위치를 의미한다. 그냥 0으로 시작하면 된다.
     [rangeStart, rangeEnd] -> 찾고자하는 range범위 (둘다 포함한다)
     */
    T query(int _low, int _high, int _cur, int rangeStart, int rangeEnd) {
        // invalid inputs...
        if(rangeEnd < _low || rangeStart > _high || rangeStart > rangeEnd)
            throw;
        
        // terminal condition
        if(rangeStart <= _low && _high <= rangeEnd)
            return tree[_cur];
        
        T left, right;
        bool valid_l;
        
        // left...
        if((valid_l = rangeStart <= (_low+_high)/2))
            left = query(_low, (_low+_high)/2, _cur*2 + 1, rangeStart, rangeEnd);
        // right
        if((_low+_high)/2  < rangeEnd) {
            right = query((_low+_high)/2 + 1, _high, (_cur+1)*2, rangeStart, rangeEnd);
            
            if(!valid_l)
                left = right;
            else
                left = op(left, right);
        }
        return left;
    }
    T query(int rangeStart, int rangeEnd) {
        return query(0, n-1, 0, rangeStart, rangeEnd);
    }
};

int main() {
    auto sum = [](long long a, long long b) {return a + b;};
    std::vector<long long> res;
    int n, m, k;
    int a, b;
    std::cin >> n >> m >> k;
    
    // init
    SegTree<long long> segmentTree(n, 0, sum);
    
    for(int i=0; i<n; ++i) {
        std::cin >> a;
        segmentTree.update(i, a);
    }
    
    while(m>0 || k>0) {
        std::cin >> n >> a >> b;
        // if 1 : change
        if(n == 1) {
            segmentTree.update(a-1, b);
            --m;
            // if 2 : print
        } else {
            res.push_back(segmentTree.query(a-1, b-1));
            --k;
        }
    }
    
    for(auto result : res)
        printf("%lld\n", result);
    
    return 0;
}
