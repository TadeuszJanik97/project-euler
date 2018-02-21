# only to be used with a list sorted in ascending order
def search(l, element):
    if len(l) == 1:
        return l[0] == element
    n = int(len(l)/2)
    if l[n] == element:
        return True
    elif l[n] > element:
        return search(l[:n], element)
    else:
        return search(l[n+1:], element)
