# Github使い方
    - https://techacademy.jp/magazine/6235
    
1. ユーザ名とメアド登録
    - $ git config --global user.name <usr>
    - $ git config --global user.email <mail>
    - 確認 $ git config --list

2. ローカルリポジトリの作成
    - $ git init
    - $ git add hoge.hoge
    - $ git commit -m "ExtendSymRel"

3. 確認
    - $ git status

4. リモートリポジトリの情報を追加
    - $ git remote add origin https://github.com/bigwing0827/ExtendSymRel.git
        - `fatal: remote origin already exists.`のとき[参考](https://qiita.com/yu-ki0718/items/3c8aae2c81ca3f82f522)

5. ローカルリポジトリをプッシュしてリモートリポジトリへ反映させる（git push）
    - $ git push origin master
    - $ git push -u origin master
    - `error: src refspec master does not match any`のとき[参考](https://qiita.com/kenkono/items/c488ec9559f6cca34313)

6. 
