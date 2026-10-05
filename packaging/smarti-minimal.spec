# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

spec_path = Path(globals().get("__file__", Path(SPECPATH) / "smarti-minimal.spec")).resolve()
repo_root = spec_path.parent.parent
app_icon = repo_root / "assets" / "smarti.ico"
app_manifest = repo_root / "packaging" / "smarti.manifest"

datas = [
    (str(repo_root / "assets"), "assets"),
    (str(repo_root / "sitecustomize.py"), "."),
]
for package in ("certifi", "keyring", "truststore"):
    try:
        datas += collect_data_files(package)
    except Exception:
        pass

hiddenimports = []

a = Analysis(
    [str(repo_root / "smarti_core.pyw")],
    pathex=[str(repo_root)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "PyQt6.QtWebEngineCore",
        "PyQt6.QtWebEngineWidgets",
        "fitz",
        "pymupdf",
        "litellm",
        "pytesseract",
        "speech_recognition",
        "pyaudio",
        "edge_tts",
        "gtts",
        "pygame",
    ],
    noarchive=False,
    optimize=1,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SmartiAI-Minimal",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(app_icon),
    manifest=str(app_manifest),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="SmartiAI-Minimal",
)
