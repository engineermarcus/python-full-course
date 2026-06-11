import os

folder = "PROBLEMS"
os.makedirs(folder, exist_ok=True)

existing = {f for f in os.listdir(folder) if f.endswith(".py")}

created = 0
for i in range(1, 1001):
    fname = f"prob{i}.py"
    if fname not in existing:
        open(os.path.join(folder, fname), "a").close()
        created += 1

print(f"Done. Created {created} new files. Total target: 1000.")