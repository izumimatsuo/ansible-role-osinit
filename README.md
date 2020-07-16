# ansible-role-osinit [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-osinit.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-osinit)

CentOS 7 の初期設定をおこなう ansible role です。

* selinux の設定
  * disabled
* locale の設定
  * ja_JP.UTF-8
* timezone and ntp の設定
  * Asia/Tokyo
  * ntp クライアントからの接続可否
* sshd の設定
  * 認証の猶予時間や認証回数
  * rootユーザでのログイン拒否
  * 公開鍵認証（パスワード認証拒否）
  * 二段階認証のサポート
  * 指定ユーザや IP アドレスからの接続可否
* カーネルパラメータの設定
  * ipv6 の無効化
  * Smurf 攻撃対策
  * IP Spoofing 攻撃対策
  * MITM 攻撃対策
  * バッファオーバーフロー対策

## 設定項目

以下の設定項目は上書き可能。

項目名                |デフォルト値|説明
----------------------|------------|-----------------------------------------------------
env_timezone          |Asia/Tokyo  |タイムゾーン
env_locale            |ja_JP.UTF-8 |言語・文字コード
ntp_public_servers    |ntp.nict.jp |問合せ先 NTP サーバ（複数可）
ntp_allow_network     |NULL        |NTP クライアントからアクセス許可する network アドレス
ssh_listen_port       |22          |ssh のポート番号
ssh_twofactor_auth    |no          |二段階認証可否
ssh_allow_users       |NULL        |ssh ログインを許可するユーザや IP アドレスを指定
