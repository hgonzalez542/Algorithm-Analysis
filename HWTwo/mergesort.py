def merge_sort(S):
    # Printing the test data unsorted before sorting
    print(f"Unsorted S {S}")
    if len(S) > 1:
        mid = len(S) // 2
        U = S[:mid]
        V = S[mid:]
        
        print(f"U {U}")
        print(f"V {V}")
        
        merge_sort(U)
        merge_sort(V)
        
        i = j = k = 0
        
        while i < len(U) and j < len(V):
            if U[i] < V[j]:
                S[k] = U[i]
                i += 1
            else:
                S[k] = V[j]
                j += 1
            k += 1
            
        while i < len(U):
            S[k] = U[i]
            i += 1
            k += 1
            
        while j < len(V):
            S[k] = V[j]
            j += 1
            k += 1
        
        print(f"Merged: {S}")

# Test input
S = [27, 10, 12, 20, 25, 13, 15, 22]
merge_sort(S)
print(f"Sorted S {S}")
