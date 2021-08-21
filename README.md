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
* 管理ユーザの設定
  * ユーザ登録
  * 公開鍵登録
* カーネルパラメータの設定
  * ipv6 の無効化
  * Smurf 攻撃対策
  * IP Spoofing 攻撃対策
  * MITM 攻撃対策
  * バッファオーバーフロー対策
* パッケージの設定
  * インストール済みパッケージの最新化
  * 追加パッケージのインストール

## 設定項目

以下の設定項目は上書き可能。

| 項目名                  | デフォルト値 | 説明                                                  |
| ----------------------- | ------------ | ----------------------------------------------------- |
| env_selinux             | disabled     | selinux の適用有無                                    |
| env_timezone            | Asia/Tokyo   | タイムゾーン                                          |
| env_locale              | en_US.UTF-8  | 言語・文字コード                                      |
| env_update_all_packages | yes          | パッケージの最新化                                    |
| env_add_packages        | []           | 追加パッケージ                                        |
| ntp_public_servers      | ntp.nict.jp  | 問合せ先 NTP サーバ（複数可）                         |
| ntp_allow_network       | None         | NTP クライアントからアクセス許可する network アドレス |
| ssh_listen_port         | 22           | ssh のポート番号                                      |
| auth_admin_user         | None         | 管理ユーザ名                                          |
| auth_admin_public_key   | None         | 管理ユーザの公開鍵                                    |
