# ladder
## 使用言語/フレームワーク
python 3.6.4

django-crispy-forms==1.7.2

django-extensions==2.0.7

django-filter==1.1.0

django-filters==0.2.1

djangorestframework==3.8.2

djangorestframework-jwt==1.11.0

## 環境構築
### 前提
1. `node`の最新バージョンが入っていること
    * brewもしくはサイトからインストールして
2. python3.6.4を使用していること
    * venvとpyenvとかも使うと楽チン
3. エラー解決の根気があること

_時間があったら手順URLを載せます！_

### フロントサイド
1. 必要パッケージのインストール
    > cd ladder
    >
    > npm install

2. 起動
    > npm run start

3. `localhost:8081` でwebpack開発サーバーが立ち上がればOK

### バックサイド
1. 'python manege.py migrate' しようとすると色々怒られる
2. 必要なパッケージがない場合は　各々をインストール
    > pip install [package-name]

3. 全部インストールし終わったらまた怒られる
    > pip install Pillow

4. マイグレーションファイルを作成
    > python manage.py makemigrations
5. DBをマイグレーションする
    > python manage.py migrate
6. `localhost:8000` でDjango開発サーバが立ち上がればOK

