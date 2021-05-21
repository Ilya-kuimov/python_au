# Graph

+ [ Course Schedule II](#course-schedule-ii)
+ [ Number of Islands](#number-of-islands)
+ [ Is Graph Bipartite](#is-graph-bipartite)
+ [ Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [ Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [ Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

##  Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
```python
class Solution:
 def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
 sortedorder = []
 if numCourses <= 0:
 return False
 inDegree = {i : 0 for i in range(numCourses)}
 graph = {i : [] for i in range(numCourses)}
 
 for child, parent in prerequisites:
 graph[parent].append(child)
 inDegree[child] += 1

 sources = deque()
 
 for key in inDegree:
 if inDegree[key] == 0:
 sources.append(key)
 #visited = 0 
 while sources:
 vertex = sources.popleft()
 #visited += 1
 sortedorder.append(vertex)
 for child in graph[vertex]:
 inDegree[child] -= 1
 if inDegree[child] == 0:
 sources.append(child)
 
 if len(sortedorder) != numCourses:
 return []
 return sortedorder
```
##  Number of Islands
```python
class Solution {

    boolean isSafe(char[][] grid, int[][] visited, int i, int j)
    {
        int n = grid.length;
        int m = grid[0].length;

        if((i<0 || i>n-1) || (j<0 || j>m-1))
            return false;

        return visited[i][j] == 0 && grid[i][j] == '1';
    }

    void DFS(char[][] grid, int[][] visited, int i, int j)
    {
        visited[i][j] = 1; //marked visited

        int[] row = {-1, 0, 1, 0};
        int[] column = {0, 1, 0, -1};

        for(int k = 0; k<4; k++)
        {
            if(isSafe(grid, visited, i+row[k], j+column[k]))
            {
                DFS(grid, visited, i+row[k], j+column[k]);
            }
        }
    }

    int DFSUtil(char[][] grid)
    {
        int count = 0;

        if(grid == null || grid.length == 0)
            return count;

        int n = grid.length; //rows
        int m = grid[0].length; //columns

        int[][] visited = new int[n][m];

        for(int i = 0; i<n; i++)
            for(int j = 0; j<m; j++)
            {
                if(grid[i][j]=='1' && visited[i][j] == 0)
                {
                    DFS(grid, visited, i, j);
                    count++;
                }
            }

        return count;
    }

    public int numIslands(char[][] grid) {

        int result = DFSUtil(grid);

        return result;
    }
}
```
## Is Graph Bipartite
```python
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];
        Arrays.fill(colors, -1);   
    
        for (int i = 0; i < n; i++) {              //This graph might be a disconnected graph. So check each unvisited node.
            if (colors[i] == -1 && !validColor(graph, colors, 0, i)) {
                return false;
            }
        }
        return true;
    }
    
    public boolean validColor(int[][] graph, int[] colors, int color, int node) {
        if (colors[node] != -1) {
            return colors[node] == color;
        }       
        colors[node] = color;       
        for (int next : graph[node]) {
            if (!validColor(graph, colors, 1 - color, next)) {
                return false;
            }
        }
        return true;
    }
```
## Cheapest Flights Within K Stops
```python
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        
        for (int[] f : flights) {
            map.computeIfAbsent(f[0], x -> new HashMap<>()).put(f[1], f[2]);
        }
        
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        pq.add(new int[] {src, 0, K+1});
        
        while (!pq.isEmpty()) {
            int[] current = pq.remove();
            int city = current[0], price = current[1], stops = current[2];
            if (city == dst) {
                return price;
            }
            if (stops > 0) {
                Map<Integer, Integer> adj = map.getOrDefault(city, new HashMap<>());
                for (int a : adj.keySet()) {
                    pq.add(new int[] {a, price + adj.get(a), stops - 1});
                }
            }
        }
        return -1;
    }
}
```
## Shortest Path in Binary Matrix
```python
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid[0][0] == 1) return -1;
        int res = 0, n = grid.size();
        set<vector<int>> visited;
        visited.insert({0, 0});
        queue<vector<int>> q;
        q.push({0, 0});
        vector<vector<int>> dirs{{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
        while (!q.empty()) {
            ++res;
            for (int i = q.size(); i > 0; --i) {
                auto t = q.front(); q.pop();
                if (t[0] == n - 1 && t[1] == n - 1) return res;
                for (auto dir : dirs) {
                    int x = t[0] + dir[0], y = t[1] + dir[1];
                    if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] == 1 || visited.count({x, y})) continue;
                    visited.insert({x, y});
                    q.push({x, y});
                }
            }
        }
        return -1;
    }
};
```
## Maximum Depth of N-ary Tree
```python
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:        
        self.max_depth = 0
        
        self.traverse(root, 1)
        
        return self.max_depth
    
    def traverse(self, root, depth):
        if not root:
            return
        
        self.max_depth = max(self.max_depth, depth)
        
        for child in root.children:
            self.traverse(child, depth + 1)
```