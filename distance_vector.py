def get_input():
    size = int(input())
    matrix = []
    for i in range(size * size):
        val = input().strip()
        if val == 'f':
            matrix.append(float('inf'))
        else:
            matrix.append(int(val))
    return size, matrix

def make_2d_matrix(size, matrix):
    result = []
    index = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(matrix[index])
            index += 1
        result.append(row)
    return result

def find_shortest_paths(size, graph):
    answer = []
    for start_node in range(size):
        distances = [float('inf')] * size
        distances[start_node] = 0
        answer.append(distances)

    for times in range(size-1):
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if graph[j][k] != float('inf') and answer[i][j] != float('inf'):
                        if answer[i][k] > answer[i][j] + graph[j][k]:
                            answer[i][k] = answer[i][j] + graph[j][k]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                if graph[j][k] != float('inf') and answer[i][j] != float('inf'):
                    if answer[i][k] > answer[i][j] + graph[j][k]:
                        answer[i] = ['None'] * size
                        break
            if 'None' in answer[i]:
                break

    return answer

def print_answer(answer):
    for i in range(len(answer)):
        result = []
        for x in answer[i]:
            if isinstance(x, str):
                result.append(x)
            elif x == float('inf'):
                result.append('None')
            else:
                result.append(str(int(x)))
        print(f"Node {i}: [{', '.join(result)}]")

if __name__ == "__main__":
    n, input_matrix = get_input()
    graph = make_2d_matrix(n, input_matrix)
    shortest_paths = find_shortest_paths(n, graph)
    print_answer(shortest_paths)