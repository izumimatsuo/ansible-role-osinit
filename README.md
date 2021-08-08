# ansible-role-osinit [![Build Status](https://travis-ci.com/izumimatsuo/ansible-role-osinit.svg?branch=master)](https://travis-ci.com/izumimatsuo/ansible-role-osinit)

CentOS 7 の初期設定をおこなう ansible role です。

* selinux の設定
  * disabled
* locale の設定
  * en_US.UTF-8
* timezone and ntp の設定
  * Asia/Tokyo
  * ntp クライアントからの接続可否
* sshd の設定
  * rootユーザでのログイン拒否
  * 公開鍵認証（パスワード認証拒否）
* カーネルパラメータの設定
  * ipv6 の無効化
  * Smurf 攻撃対策
  * IP Spoofing 攻撃対策
  * MITM 攻撃対策
  * バッファオーバーフロー対策
* パッケージの設定
  * 追加パッケージのインストール
  * インストール済みパッケージの最新化

## 設定項目

以下の設定項目は上書き可能。

項目名                |デフォルト値|説明
----------------------|------------|-----------------------------------------------------
env_timezone          |Asia/Tokyo  |タイムゾーン
env_locale            |en_US.UTF-8 |言語・文字コード
env_add_packages      | NULL       |追加パッケージ
env_update_all_packages | yes      |パッケージの最新化
ntp_public_servers    |ntp.nict.jp |問合せ先 NTP サーバ（複数可）
ntp_allow_network     |NULL        |NTP クライアントからアクセス許可する network アドレス
ssh_listen_port       |22          |ssh のポート番号
