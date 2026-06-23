from pathlib import Path



def is_safe(levels)->bool:

    diffs = [
    levels[i + 1] - levels[i]
    for i in range(len(levels) - 1)
    ]

    return (
        all(1 <= diff <= 3 for diff in diffs)
        or
        all(-3 <= diff <= -1 for diff in diffs)
    )

    ...


def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        shortened = levels[:i] + levels[i + 1:]

        if is_safe(shortened):
            return True

    return False


def count_safe(reports):
    
    safe_reports = sum(is_safe_with_dampener(levels) for levels in reports)

    return safe_reports
    

if __name__ == "__main__":
    text = Path("data/input.txt").read_text()

    reports = [
        list(map(int, line.split()))
        for line in text.splitlines()
        if line.strip()
    ]

    answer = count_safe(reports)

    print(f'{answer} of {len(reports)} reports are safe!')
    ...