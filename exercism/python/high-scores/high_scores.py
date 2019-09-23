def latest(scores: [int]) -> int:
    return scores[-1]


def personal_best(scores: [int]) -> int:
    return sorted(scores)[-1]


def personal_top_three(scores: [int]) -> [int]:
    return sorted(scores, reverse=True)[:3]
