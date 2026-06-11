import os

bashrc = os.path.expanduser("~/.bashrc")
problems_dir = os.path.join(os.getcwd(), "PROBLEMS")  # absolute path

aliases = []
for i in range(1, 1001):
    alias = f"alias {i}='python3 {problems_dir}/prob{i}.py'"
    aliases.append(alias)

block = "\n# === PROBLEMS aliases (prob1-prob1000) ===\n"
block += "\n".join(aliases)
block += "\n# === END PROBLEMS aliases ===\n"

# Avoid duplicates — remove old block if exists
with open(bashrc, "r") as f:
    content = f.read()

if "# === PROBLEMS aliases" in content:
    start = content.index("# === PROBLEMS aliases")
    end = content.index("# === END PROBLEMS aliases") + len("# === END PROBLEMS aliases") + 1
    content = content[:start] + content[end:]

with open(bashrc, "w") as f:
    f.write(content + block)

print(f"Done! {len(aliases)} aliases written to {bashrc}")
os.system("bash -i -c 'source ~/.bashrc'")
print("Aliases loaded. You're good to go!")