# easymdm





```
PS D:\mygit\easymdm> uv init --package

to test
go under src/easymdm >
PS D:\mygit\easymdm\src\easymdm> uv run -m cli --source file --name 123.csv 
or
PS D:\mygit\easymdm\src> uv run -m easymdm.cli --source file --name ./easymdm/123.csv --config D:\\mygit\\easymdm\\config.yaml
                         uv run -m easymdm.cli --source file --name D:\\mygit\\easymdm\\src\\easymdm\\123.csv --config D:\\mygit\\easymdm\\config.yaml
or for sqlite
uv run -m easymdm.cli --source sqlite --table main.slvr_personal_info --config D:\mygit\easymdm\config.yaml --outpath out/
```

### BUILD

```
PS D:\mygit\easymdm> uv build                          
Building source distribution...
Building wheel from source distribution...
Successfully built dist\easymdm-0.1.0.tar.gz
Successfully built dist\easymdm-0.1.0-py3-none-any.whl

```

Warnings

```
D:\mygit\easymdm\.venv\Lib\site-packages\fuzzywuzzy\fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning
  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')

```