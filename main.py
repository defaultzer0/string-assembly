with open("reads.fasta", "r") as f:
	reads = [i.rstrip("\n") for i in f]
	reads = [i for i in reads[1::2]]
	reads = list(set(reads))
n = len(reads)
kmers = []

for read in reads:
	kmers.append([read[:-1], read[1:]])

# for i in range(n):
# 	print(f"{reads[i]}:\n\t{kmers[i]}")

graph = [[] for i in range(n)]

visited = [0 for i in range(n)]

for i in range(n):
	read_root = reads[i]
	l_root, r_root = kmers[i]

	# print(f"{i} root is {read_root}")

	for j in range(i + 1, n):
		if i == j:
			continue

		#print(f"\tchecking {reads[j]}")
		read = reads[j]
		l, r = kmers[j]
		if l == r_root: 
			# print(f"\t\tpair {read_root} and {read}")
			# print(f"\t\t{i} {j}")
			graph[i].append(j)
			
			visited[j] -= 1
			visited[i] += 1

		if r == l_root:
			# print(f"\t\tpair {read} and {read_root}")
			# print(f"\t\t{j} {i}")
			graph[j].append(i)

			visited[i] -= 1
			visited[j] += 1

# for index, v in enumerate(graph):
# 	print(index, v)

stack = []
stack.append(visited.index(1))
path = []

while stack:
	curr_v = stack[-1]
	if not graph[curr_v]:
		path.append(curr_v)
		stack.pop()
	else:
		v = graph[curr_v].pop(-1)
		stack.append(v)

path = list(reversed(path))
#print(path)
s = reads[path[0]]

for p in path[1:]:
	s += reads[p][-1]

print(s)

