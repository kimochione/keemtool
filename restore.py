import shutil
from pathlib import Path
print("RESTORING SOFTWARE...")
SITE = Path("/usr/local/lib/python3.12/dist-packages")
BACKUP = Path(__file__).parent
for pkg in ["unsloth", "unsloth_zoo", "transformers", "trl", "peft", "accelerate", "datasets", "safetensors", "sentencepiece", "huggingface_hub"]:
    src = BACKUP / pkg
    dst = SITE / pkg
    if src.exists():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"Restored: {pkg}")
for info in BACKUP.glob("*.dist-info"):
    dst = SITE / info.name
    shutil.copytree(info, dst, dirs_exist_ok=True)
    print(f"Restored: {info.name}")
print("✅ ALL SOFTWARE RESTORED!")
