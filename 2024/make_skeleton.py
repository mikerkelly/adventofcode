import sys
from pathlib import Path
import shutil

target_dir = Path(sys.argv[1])
target_dir.mkdir(parents=True, exist_ok=True)

template_file = Path("template.py")
shutil.copy(template_file, target_dir / "solve.py")

(target_dir / "example.txt").touch()
(target_dir / "input.txt").touch()
