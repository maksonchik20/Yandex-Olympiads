int(input())
data = list(set(map(int, input().split())))
data.sort()
# k = int(input())
# for el in map(int, input().split()):
#     cnt = 0
#     for nakl in data:
#         if el > nakl:
#             cnt += 1
#         if el <= nakl:
#             break
#     print(cnt)

#include <iostream>
#include <vector>
#include <algorithm>

# int main()
# {
#     int n;
#     std::cin >> n;
#     std::vector<long long> v;
#     for (int i=0; i<n; i++) {
#         long long a;
#         std::cin >> a;
#         bool found = std::find(v.begin(), v.end(), a) != v.end();
#         if (not found) {
#             v.push_back(a);
#         }
#     }
#     sort(v.begin(), v.end());
#     int k;
#     cin >> k;
    
#     for (int i=0; i<k; i++) {
#         long long q;
#         cin >> q;
#         // const int pivot = 4;
#         // auto pos = std::lower_bound(std::begin(v), std::end(v), pivot);
#         // std::cout << std::distance(std::begin(v), pos);
#     }
#     return 0;
# }