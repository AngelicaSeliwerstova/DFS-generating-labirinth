import random
import pygame

matrix=[[1 for _ in range(21)] for _ in range(21)]
start=(1,1)
size=21
cell=20
search_start = (0, 1)
finish = (size - 1, size - 2)
width=size*cell
height=size*cell
stack=[start]
visited={start}
matrix[start[0]][start[1]] = 0
clock = pygame.time.Clock()
generating=True
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running=True
path_set = set()
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if generating:
        if stack:
            i, j = stack[-1]
            neibhours = []

            if i+2<len(matrix) and (i+2,j) not in visited:
                neibhours.append((i+2,j))
            if j+2<len(matrix) and (i,j+2) not in visited:
                neibhours.append((i,j+2))
            if i-2>=0 and (i-2,j) not in visited:
                neibhours.append((i-2,j))
            if j-2>=0 and (i,j-2) not in visited:
                neibhours.append((i,j-2))
            if neibhours:
                ni,nj=random.choice(neibhours)
                wall_i=(i+ni)//2
                wall_j=(j+nj)//2
                matrix[wall_i][wall_j] = 0
                matrix[ni][nj] = 0
                visited.add((ni, nj))
                stack.append((ni, nj))
            else:
                stack.pop()
        else:
            generating=False
            matrix[0][1] = 0
            matrix[size - 1][size - 2] = 0
            stack = [search_start]
            visited = {search_start}
            parent = {search_start: None}
            found = None

            while stack:
                i, j = stack.pop()
                if (i, j) == finish:
                    found = (i, j)
                    break

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < size and 0 <= nj < size:
                        if matrix[ni][nj] == 0 and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            parent[(ni, nj)] = (i, j)
                            stack.append((ni, nj))
            path = []
            if found is not None:
                cur = found
                while cur is not None:
                    path.append(cur)
                    cur = parent[cur]
                path.reverse()
                path_set = set(path)
    screen.fill((255, 255, 255))
    for i in range(size):
        for j in range(size):
            x=j*cell
            y=i*cell
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j * 20, i * 20, 20, 20))
            elif (i,j) in path_set:
                pygame.draw.rect(screen, (0, 200, 0), (j * 20, i * 20, 20, 20))

    pygame.display.flip()
pygame.quit()





