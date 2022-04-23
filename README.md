# ansible-role-osinit [![Build Status](https://travis-ci.com/izumimatsuo/ansible-role-osinit.svg?branch=master)](https://travis-ci.com/izumimatsuo/ansible-role-osinit)

CentOS 7 の初期設定をおこなう ansible role です。

- selinuxの設定
- localeの設定
- timezoneの設定
- time serverの設定
- sshd の設定（公開鍵認証）
- 管理ユーザの設定
  - ユーザ登録
  - 公開鍵登録
- パッケージの設定
  - パッケージの最新化
  - 追加パッケージのインストール

## 設定項目

以下の設定項目は上書き可能。

| 項目名                  | デフォルト値 | 説明                                                  |
| ----------------------- | ------------ | ----------------------------------------------------- |
| env_selinux_enabled     | no           | selinux の適用有無                                    |
| env_yum_update          | yes          | パッケージの最新化                                    |
| env_add_packages        | bash-completion | 追加パッケージ                                        |
| env_locale              | en_US.UTF-8  | 言語・文字コード                                      |
| env_timezone            | Asia/Tokyo   | タイムゾーン                                          |
| env_time_servers        | ntp1.jst.mfeed.ad.jp<br>ntp2.jst.mfeed.ad.jp<br>ntp3.jst.mfeed.ad.jp | 問合せ先 NTP サーバ（複数設定推奨）                         |
| auth_admin_user         | None         | 管理ユーザ名                                          |
| auth_admin_public_key   | None         | 管理ユーザの公開鍵                                    |
