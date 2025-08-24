import subprocess, sys, os

def test_hello_output():
    # リポジトリ直下の hello.py を実行して標準出力を検証
    result = subprocess.run([sys.executable, os.path.join(os.getcwd(), "hello.py")],
                            capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "Hello Codex!"

