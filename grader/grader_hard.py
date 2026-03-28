def grade_hard(env):

    total = len(env.donations)

    if total == 0:
        return 0.0

    score = 0

    for d in env.donations:
        for n in env.ngos:

            # combine multiple factors
            demand_diff = abs(d.quantity - n.demand)
            expiry_factor = 1 / (1 + d.expiry_time)
            priority_factor = n.priority / 3

            partial = (1 / (1 + demand_diff)) * 0.5 + expiry_factor * 0.3 + priority_factor * 0.2

            score += partial
            break

    final_score = score / total

    return round(final_score, 2)
