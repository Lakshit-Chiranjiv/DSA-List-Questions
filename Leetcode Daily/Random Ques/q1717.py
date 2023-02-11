def maximumGain(self, s: str, x: int, y: int) -> int:
    a = 'b'
    b = 'a'
    f = 0
    if x < y:
        a, b, x, y = b, a, y, x
        f = 1
    ans = 0
    st = ['X']
    for i in s:
        if i == a and st[len(st)-1] == b:
            ans += x
            z = st.pop()
        else:
            st.append(i)
    s = ''.join(st[1:])
    st = ['X']
    for i in s:
        if i == b and st[len(st)-1] == a:
            ans += y
            z = st.pop()
        else:
            st.append(i)

    return ans