# ansible-role-env

CentOS 7 の初期設定をおこなう ansible role です。

* selinux の設定
  * disabled
* locale の設定
  * ja_JP.UTF-8
* timezone and ntp の設定
  * Asia/Tokyo
  * ntp クライアントからの接続可否
* sshd の設定
  * ed25519の鍵だけを許可
  * 認証の猶予時間や認証回数
  * 指定ユーザや IP アドレスからの接続可否
* firewall の設定
  * ssh(22/tcp) のみを公開
  * データを持たないパケットの接続を破棄
  * SYN flood 攻撃と思われる接続を破棄
  * ステルススキャンと思われる接続を破棄
* カーネルパラメータの設定
  * ipv6 の無効化
  * SYN flood 攻撃対策
  * Smurf 攻撃対策
  * IP Spoofing 攻撃対策
  * MITM 攻撃対策

## 設定項目

以下の設定項目は上書き可能。

項目名                |デフォルト値|説明
----------------------|------------|-----------------------------------------------------
env_timezone          |Asia/Tokyo  |タイムゾーン
env_locale            |ja_JP.UTF-8 |言語・文字コード
ntp_public_servers    |ntp.nict.jp |問合せ先 NTP サーバ（複数可）
ntp_allow_network     |NULL        |NTP クライアントからアクセス許可する network アドレス
ssh_listen_port       |22          |ssh のポート番号
ssh_root_login        |'yes'       |root ユーザでの ssh ログイン可否
ssh_passwd_auth       |'yes'       |パスワードでの ssh ログイン可否
ssh_allow_users       |NULL        |ssh ログインを許可するユーザや IP アドレスを指定
firewall_enabled_ports|22/tcp      |公開するポート番号（複数可）
