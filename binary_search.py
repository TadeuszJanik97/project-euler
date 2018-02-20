def search(l, element):
    if len(l) == 1:
        return l[0] == element
    n = int(len(l)/2)
    return search(l[:n], element) or search(l[n:], element)
