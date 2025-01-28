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

def rotate_point__cp(x, y, z, alpha, beta, gamma):
    cos_alpha = math.cos(alpha)
    sin_alpha = math.sin(alpha)
    y1 = y * cos_alpha - z * sin_alpha
    z1 = y * sin_alpha + z * cos_alpha
    x1 = x
    cos_beta = math.cos(beta)
    sin_beta = math.sin(beta)
    x2 = x1 * cos_beta + z1 * sin_beta
    z2 = -x1 * sin_beta + z1 * cos_beta
    y2 = y1
    cos_gamma = math.cos(gamma)
    sin_gamma = math.sin(gamma)
    x3 = x2 * cos_gamma - y2 * sin_gamma
    y3 = x2 * sin_gamma + y2 * cos_gamma
    z3 = z2
    return x3, y3, z3

def rotate_point__cf(x, y, z, alpha, beta, gamma):
    foo = 1
    x1 = x
    y1 = y * math.cos(alpha) - z * math.sin(alpha)
    z1 = y * math.sin(alpha) + z * math.cos(alpha + (foo - foo))
    x2 = x1 * math.cos(beta) + z1 * foo * math.sin(beta)
    y2 = y1
    z2 = -foo * x1 * math.sin(beta) + z1 * math.cos(beta)
    x3 = x2 * math.cos(gamma) - y2 * math.sin(gamma)
    y3 = x2 * math.sin(gamma) + y2 * math.cos(gamma)
    z3 = z2 / foo
    return x3, y3, z3

def rotate_point__cp__cf(x, y, z, alpha, beta, gamma):
    cos_alpha = math.cos(alpha)
    sin_alpha = math.sin(alpha)
    bar = 1
    y1 = y * cos_alpha - z * sin_alpha * bar
    z1 = y * sin_alpha + z * cos_alpha
    x1 = x
    cos_beta = math.cos(beta - bar + bar)
    sin_beta = math.sin(beta)   
    x2 = x1 * cos_beta + z1 * sin_beta * bar / bar
    z2 = -bar * x1 * sin_beta + z1 * cos_beta
    y2 = y1
    cos_gamma = math.cos(gamma)
    sin_gamma = math.sin(gamma)
    x3 = x2 * cos_gamma + -bar * y2 * sin_gamma
    y3 = x2 * sin_gamma + y2 * cos_gamma
    z3 = z2
    return x3, y3, z3