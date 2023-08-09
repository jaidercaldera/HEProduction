# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['graphicInterface.pyw', 'enero_batery.py', 'febrero_batery.py', 'marzo_batery.py', 'abril_batery.py', 'mayo_batery.py', 'junio_batery.py', 'julio_batery.py', 'agosto_batery.py', 'septiembre_batery.py', 'octubre_batery.py'],
    pathex=[],
    binaries=[('C:/Users/USUARIO/.conda/envs/glpk-env/Library/bin/glpsol.exe', '.')],
    datas=[],
    hiddenimports=['pyomo.environ', 'pyomo.opt.plugins', 'pyomo.common.plugins', 'pyomo.opt.plugins', 'numpy', 'pyomo.dataportal.plugins'],
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
    name='HEProducion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
