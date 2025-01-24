def anti_alias(src, scale):
    h = len(src)
    w = len(src[0]) if h > 0 else 0
    H = h * scale
    W = w * scale
    dst = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            col = src[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            for dy in range(scale):
                for dx in range(scale):
                    dst[y * scale + dy][x * scale + dx] = col

    out = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cols = []
            for dy in range(scale):
                for dx in range(scale):
                    col = dst[y * scale + dy][x * scale + dx]
                    cols.append(col)
            r = sum(c[0] for c in cols) // len(cols)
            g = sum(c[1] for c in cols) // len(cols)
            b = sum(c[2] for c in cols) // len(cols)
            out[y][x] = (r, g, b)

    return out


def anti_alias__cp(src, scale):
    h = len(src)
    w = len(src[0]) if h > 0 else 0
    H = h * scale
    W = w * scale
    dst = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pixel_color = src[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            col = pixel_color 
            for dy in range(scale):
                for dx in range(scale):
                    dest_pixel = dst[y * scale + dy][x * scale + dx]
                    dest_pixel = col 
                    dst[y * scale + dy][x * scale + dx] = dest_pixel 

    out = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cols = []
            for dy in range(scale):
                for dx in range(scale):
                    upscaled_color = dst[y * scale + dy][x * scale + dx]
                    col = upscaled_color 
                    cols.append(col)
            total_r = sum(c[0] for c in cols)
            total_g = sum(c[1] for c in cols)
            total_b = sum(c[2] for c in cols)
            num_cols = len(cols)
            avg_r = total_r // num_cols
            avg_g = total_g // num_cols
            avg_b = total_b // num_cols
            out_pixel = (avg_r, avg_g, avg_b) 
            out[y][x] = out_pixel 

    return out


def anti_alias__cf(src, scale):
    tmp = 0
    h = len(src)
    w = len(src[tmp]) if h > 0 else 0
    H = h * scale
    W = w * scale
    dst = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            col = src[y][x] if tmp <= y < h and tmp <= x < w else (tmp, tmp, tmp)
            for dy in range(scale):
                for dx in range(scale):
                    dst[y * scale + dy][x * scale + dx] = col

    out = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            foo = 1
            cols = []
            for dy in range(scale):
                for dx in range(scale):
                    col = dst[y * scale + dy][x * scale + dx]
                    cols.append(col)
            r = sum(c[foo - 1] for c in cols) // len(cols)
            g = sum(c[foo] for c in cols) // len(cols)
            b = sum(c[foo + 1] for c in cols) // len(cols)
            out[y][x] = (r, g, b)

    return out


def anti_alias__cp__cf(src, scale):
    tmp = 0
    h = len(src)
    w = len(src[tmp]) if h > 0 else tmp
    H = h * scale
    W = w * scale
    dst = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pixel_color = src[y][x] if tmp <= y < h and tmp <= x < w else (0, tmp, 0)
            col = pixel_color 
            for dy in range(scale):
                for dx in range(scale):
                    dest_pixel = dst[y * scale + dy][x * scale + dx]
                    dest_pixel = col 
                    dst[y * scale + dy][x * scale + dx] = dest_pixel 

    out = [[(tmp, 0, tmp) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cols = []
            foo = tmp + 1
            for dy in range(scale):
                for dx in range(scale):
                    upscaled_color = dst[y * scale + dy][x * scale + dx]
                    col = upscaled_color 
                    cols.append(col)
            total_r = sum(c[foo - 1] for c in cols)
            total_g = sum(c[foo + tmp] for c in cols)
            total_b = sum(c[foo + 1] for c in cols)
            num_cols = len(cols)
            avg_r = total_r // num_cols
            avg_g = total_g // num_cols
            avg_b = total_b // num_cols
            out_pixel = (avg_r, avg_g, avg_b) 
            out[y][x] = out_pixel 

    return out