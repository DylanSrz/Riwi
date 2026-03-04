
import sys
import time


def progress_bar(progress, total, length=40):
    percent = progress / total
    filled = int(length * percent)

    bar = "\033[32m" + "█" * filled + "\033[0m"
    bar += "-" * (length - filled)

    sys.stdout.write(f"\r|{bar}| {percent:.1%}")
    sys.stdout.flush()


total = 100
for i in range(total + 1):
    progress_bar(i, total)
    time.sleep(0.02)

print()


