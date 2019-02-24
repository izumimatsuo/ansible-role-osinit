# ansible-role-osinit

CentOS 7 の初期設定をおこなう ansible role です。

* selinux の設定
  * disabled
* locale の設定
  * ja_JP.UTF-8
* timezone and ntp の設定
  * Asia/Tokyo
* sshd の設定
  * ed25519の鍵だけを許可
* firewall の設定
  * データを持たないパケットの接続を破棄
  * SYN flood 攻撃と思われる接続を破棄
  * ステルススキャンと思われる接続を破棄
* カーネルパラメータの設定
  * ipv6 の無効化
  * SYN flood 攻撃対策
  * Smurf 攻撃対策

## 設定項目

以下の設定項目は上書き可能。

項目名           |デフォルト値|説明
-----------------|------------|----------
osinit_timezone  |Asia/Tokyo  |タイムゾーン
osinit_locale    |ja_JP.UTF-8 |言語・文字コード
