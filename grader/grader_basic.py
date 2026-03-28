def compute_score(env):

    total_donations = len(env.donations)

    if total_donations == 0:
        return 0.0

    delivered = 0

    for donation in env.donations:
        if donation.quantity > 0:
            delivered += 1

    score = delivered / total_donations

    return round(score, 2)