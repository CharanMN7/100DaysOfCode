import os

for i in range(1, 101):
  os.system(f"mkdir \"Day {i}\"")
  os.system(f"touch \"Day {i}/README.md\"")
  os.system(f"echo # Day {i} >> \"Day {i}/README.md\"")
