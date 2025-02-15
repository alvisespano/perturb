import math

def rotate_point(x, y, z, alpha, beta, gamma):
    x1 = x
    y1 = y * math.cos(alpha) - z * math.sin(alpha)
    z1 = y * math.sin(alpha) + z * math.cos(alpha)
    x2 = x1 * math.cos(beta) + z1 * math.sin(beta)
    y2 = y1
    z2 = -x1 * math.sin(beta) + z1 * math.cos(beta)
    x3 = x2 * math.cos(gamma) - y2 * math.sin(gamma)
    y3 = x2 * math.sin(gamma) + y2 * math.cos(gamma)
    z3 = z2
    return x3, y3, z3


def texture_mapping(src, dst_w, dst_h, alpha, beta, gamma):
    dst = [[(0, 0, 0) for _ in range(dst_w)] for _ in range(dst_h)]
    src_w = len(src)
    src_h = len(src[0]) if src_w > 0 else 0
    vxs = [(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)]
    coords = [(0, 0), (1, 0), (1, 1), (0, 1)]
    rot_vxs = [rotate_point(x, y, z, alpha, beta, gamma) for x, y, z in vxs]

    def project(x, y, z):
        screen_x = int((x + 1) * 0.5 * (dst_w - 1))
        screen_y = int((1 - y) * 0.5 * (dst_h - 1))
        return screen_x, screen_y

    def rasterize(v0, v1, v2, uv0, uv1, uv2):
        min_x = min(v0[0], v1[0], v2[0])
        max_x = max(v0[0], v1[0], v2[0])
        min_y = min(v0[1], v1[1], v2[1])
        max_y = max(v0[1], v1[1], v2[1])

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                def point_in_triangle(px, py, v0, v1, v2):
                    def Xprod(a, b):
                        return a[0] * b[1] - a[1] * b[0]

                    def sign(p1, p2, p3):
                        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

                    d1 = sign((px, py), v0, v1)
                    d2 = sign((px, py), v1, v2)
                    d3 = sign((px, py), v2, v0)

                    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
                    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

                    return not (has_neg and has_pos)

                if point_in_triangle(x, y, v0, v1, v2):
                    def barycentric_coords(px, py, v0, v1, v2):
                        def area(a, b, c):
                            return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0)

                        area_total = area(v0, v1, v2)
                        area1 = area((px, py), v1, v2)
                        area2 = area(v0, (px, py), v2)
                        area3 = area(v0, v1, (px, py))
                        alpha = area1 / area_total
                        beta = area2 / area_total
                        gamma = area3 / area_total
                        return alpha, beta, gamma

                    alpha, beta, gamma = barycentric_coords(x, y, v0, v1, v2)

                    u = alpha * uv0[0] + beta * uv1[0] + gamma * uv2[0]
                    v = alpha * uv0[1] + beta * uv1[1] + gamma * uv2[1]

                    tex_x = int(u * (src_h - 1))
                    tex_y = int(v * (src_w - 1))

                    if 0 <= tex_x < src_h and 0 <= tex_y < src_w:
                        dst[y][x] = src[tex_y][tex_x]

    prj_vxs = [project(x, y, z) for x, y, z in rot_vxs]
    rasterize(prj_vxs[0], prj_vxs[1], prj_vxs[2], coords[0], coords[1], coords[2])
    rasterize(prj_vxs[0], prj_vxs[2], prj_vxs[3], coords[0], coords[2], coords[3])

    return dst


