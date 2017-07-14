def binary_search (T,n,p,p_index=0):
    if n==0:
        p_index=-1
        return p_index
    else:
        mid_ind=int(n/2)
        if T[mid_ind]==p:
            p_index+=mid_ind
            return p_index
        elif T[mid_ind]>p:
            T=T[:mid_ind]
            return binary_search(T,len(T),p,p_index)
        elif T[mid_ind]<p:
            T = T[mid_ind +1:]
            p_index+=mid_ind+1
            return binary_search(T,len(T),p,p_index)