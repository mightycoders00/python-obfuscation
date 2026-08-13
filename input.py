import math
import hashlib
import random

def summarize(words):
    total = sum(len(w) for w in words)
    longest = max(words, key=len)
    sig = hashlib.md5("".join(words).encode()).hexdigest()
    return total, longest, sig[:8]

random.seed(42)
words = ["python", "obfuscate", "protect", "deploy"]
count, longest, sig = summarize(words)
print("sorted:", sorted(words))
print("total:", count, "longest:", longest)
print("sig:", sig, "| pi:", round(math.pi, 4), "| pick:", random.choice(words))
