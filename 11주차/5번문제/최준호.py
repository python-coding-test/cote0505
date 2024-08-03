def compress(s, length):
    compress_string = ""
    prev = s[:length]
    cnt = 1

    for i in range(length, len(s), length):
        if s[i:i+length] == prev:
            cnt += 1
        else:
            compress_string += ((str(cnt) + prev)) if cnt > 1 else prev
            prev = s[i:i+length]
            cnt = 1
    compress_string += ((str(cnt) + prev)) if cnt > 1 else prev

    return len(compress_string)

def solution(s):
    min_compress = len(s)
    if min_compress == 1:
        return 1

    for length in range(1, len(s) // 2 + 1):
        compressByLength = compress(s,length)
        min_compress = min(min_compress, compressByLength)

    return min_compress