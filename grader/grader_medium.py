def grade_medium(env):

    total = len(env.donations)

    if total == 0:
        return 0.0

    # Medium: based on quantity matching demand
    matched = 0

    for d in env.donations:
        for n in env.ngos:
            if abs(d.quantity - n.demand) <= 5:
                matched += 1
                break

    score = matched / total

    return round(score, 2)
