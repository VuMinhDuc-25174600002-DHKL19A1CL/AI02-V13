"""Bootstrap the packaged AI02 V13 app for Streamlit Community Cloud."""
from pathlib import Path
import sys
import tempfile
import zipfile

REPO = Path(__file__).resolve().parent
ARCHIVE = REPO / "AI02_V13_submission.zip"
if not ARCHIVE.is_file():
    raise FileNotFoundError("AI02_V13_submission.zip is missing from the repository root")

info = ARCHIVE.stat()
source_root = Path(tempfile.gettempdir()) / f"ai02_v13_{info.st_size}_{info.st_mtime_ns}"
marker = source_root / ".extracted"
if not marker.is_file():
    source_root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE) as package:
        root = source_root.resolve()
        for item in package.infolist():
            target = (source_root / item.filename).resolve()
            if not target.is_relative_to(root):
                raise ValueError("Unsafe path in AI02 V13 archive")
        package.extractall(source_root)
    marker.write_text("ok", encoding="utf-8")

app_file = source_root / "app.py"
if not app_file.is_file():
    raise FileNotFoundError("The archive does not contain app.py")
sys.path.insert(0, str(source_root))
original_file = __file__
try:
    __file__ = str(app_file)
    exec(compile(app_file.read_text(encoding="utf-8"), str(app_file), "exec"), globals())
finally:
    __file__ = original_file
