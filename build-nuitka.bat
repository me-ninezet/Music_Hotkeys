python -m nuitka ^
    --onefile ^
    --standalone ^
    --enable-plugin=tk-inter ^
    --include-package=flet ^
    --include-package=packaging ^
    --include-data-dir=flet_resources=flet_resources ^
    --include-data-file=config.txt=config.txt ^
    --output-dir=dist ^
    --remove-output ^
    --windows-console-mode=disable ^
    --follow-imports ^
    --assume-yes-for-downloads ^
    main.py