# ansible-role-osinit

CentOS 7 の初期設定をおこなう ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名           |デフォルト値|説明
-----------------|------------|----------
osinit_timezone  |Asia/Tokyo  |タイムゾーン
osinit_locale    |ja_JP.UTF-8 |言語・文字コード

## ビルド

以下のいづれかで ansible-playbook と testinfra を実行可能。

1) docker-compose でビルド実行

``` $ ./build.sh ```

2) gitlab-runner でビルド実行

``` $ gitlab-runner exec docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock ansible_build ```
