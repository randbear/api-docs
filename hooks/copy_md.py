import mimetypes
import shutil
from pathlib import Path

# 让 dev server 以正确的 charset 提供 .md 和 .txt 文件
mimetypes.add_type("text/plain; charset=utf-8", ".md")
mimetypes.add_type("text/plain; charset=utf-8", ".txt")


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    for md_file in docs_dir.rglob("*.md"):
        rel = md_file.relative_to(docs_dir)
        dest = site_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, dest)
