sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(sample_list)
chunk_size = length//3
chunk1 = sample_list[:chunk_size]
print("Chunk 1", chunk1)
reversed_list = chunk1[::-1]
print("After reversing it", reversed_list)
chunk2 = sample_list[chunk_size:chunk_size*2]
print("Chunk 2", chunk2)
reversed_list = chunk2[::-1]
print("After reversing it", reversed_list)
chunk3 = sample_list[chunk_size*2:]
print("Chunk 3", chunk3)
reversed_list = chunk3[::-1]
print("After reversing it", reversed_list)