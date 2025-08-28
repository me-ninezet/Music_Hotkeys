# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],  # главный файл вашего приложения
    pathex=[],  # пути к дополнительным модулям
    binaries=[],
    datas=[
        ('config.txt', '.'),
        ('flet_resources/*', 'flet_resources'),
        ('flet_resources/assets/*', 'flet_resources/assets'),
        ('*.log', '.')
    ],
    hiddenimports=[
        'pystray',
        'PIL',
        'keyboard',
        'pyautogui',
        'flet',
        'logging',
        'threading',
        'time',
        'os',
        'sys',
        'gc',
        'pathlib'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MusicHotkeys',  # имя исполняемого файла
    debug=False,  # отладка
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # сжатие
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # FALSE - скрыть консоль, TRUE - показать
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)