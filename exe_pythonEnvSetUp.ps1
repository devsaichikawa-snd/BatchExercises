<# Python環境の初期セットアップを実行する
※GitHubにリポジトリが存在し、Git Cloneが済んでいること。

1. PowerShell７を起動する
2. プロジェクトルートに移動する。
3. exe_pythonEnvSetUp.ps1をプロジェクトルートに配置する。
3. コマンドを実行する。
    >.\exe_pythonEnvSetUp.ps1
#>

# Venvの生成
python -m venv .venv

# アクティブ化
& .\.venv\Scripts\Activate.ps1

# PIPの更新
python.exe -m pip install --upgrade pip

# setuptoolsの更新
pip install -U setuptools
