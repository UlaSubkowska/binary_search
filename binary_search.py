def binary_search(T,n,p):
    p_index = 0
    while True:
        middle_index=int(n/2)       #jeśli nieparzysta liczba elementów dokładnie środkowy, jeśli parzysta index wyższy z 2 środkowych
        if middle_index > 0 or len(T)==1:
            if T[middle_index]==p:
                p_index+= middle_index
                break
            elif T[middle_index]>p:
                T=T[:middle_index]
                n = len(T)
            elif T[middle_index]<p:
                T=T[middle_index+1:]
                p_index+=(n-len(T))
                n = len(T)
        else: p_index=-1; break
    return p_index



