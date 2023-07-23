from collections import deque

s = int(input())

visited = {}
def bfs():
    q = deque()
    q.append((1, 0))  # (screen의 이모티콘 수, 클립보드의 이모티콘 수)
    visited[(1, 0)] = 0
    while q:
        screen, clipboard = q.popleft() 
        if screen == s:
            print(visited[(screen, clipboard)])
            return
        for step in [(screen, screen), (screen + clipboard, clipboard), (screen - 1, clipboard)]:
            i, j = step
            if (i, j) not in visited.keys():
                visited[(i, j)] = visited[(screen, clipboard)] + 1
                q.append((i, j))

bfs()
