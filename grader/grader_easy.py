def grade_easy(env):

    if len(env.donations) == 0:
        return 0.0

    # Easy: just check if at least one donation handled
    return 1.0 if len(env.donations) >= 1 else 0.0
