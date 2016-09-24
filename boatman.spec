# -*- mode: python -*-

block_cipher = None


a = Analysis(['boatman\\boatman.py'],
             pathex=['boatman', '.\\boatman'],
             binaries=None,
             datas=[('boatman\*.rst', '.'), ('boatman\pyenv.cfg', '.'),
                    ('boatman\doc\*.*', 'doc'),
                    ('boatman\doc\_modules\*.*', 'doc\_modules'),
                    ('boatman\doc\_sources\*.*', 'doc\_sources'),
                    ('boatman\doc\_static\*.*', 'doc\_static'),],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='boatman',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='boatman')
