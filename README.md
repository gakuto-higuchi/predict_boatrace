# ボートレースAI
---
## 機能
- 予測したレースの15分前にレース回、レース場、日にちを入力すると、レーサーの着順を確率で予測する

## 苦労したこと
---
- 特徴量エンジニアリングする際に、時系列を考慮しながらデータ加工しないといけなかった
  - 例えば、現時点までの直近半年の勝率を計算する際に、未来のデータが混ざることがないように計算
- 公式ホームページからスクレイピングしたtxtデータを正規表現で取り出すこと
  - 年によってtxtデータの形式や名前が変わることがあったので、それに合わせて正規表現でデータを取得しなければならなかった
- 計算資源が少なく、全データを扱うことができなかったため、downsamplingしてデータ数を減らした
  - 1-6艇まであるが、予測して欲しいのは1から3着なので、1,2,3着と4着以下といったように4クラスの分類に変換した。
  - 4着以下は4,5,6艇がまとめられているので、学習する際にデータの偏りが考えられたため、1着を基準にdownsamplingした
  - 今思えば、NNでbatchを使用してやれば、気にせずに回せたのかも
- 学習データでは存在するデータが本番データには存在しないため、学習させることができなかった
  - 具体的には、学習データには平均スタート値があるのに、本番データでは平均スタート値がない
  - 本番データとは、予測したいレースの直前に取得してくるデータのこと
- 特徴量の選手名をどのように扱うかを考えた。そのままone-hotエンコーディングで変換
  - まだ考え中

## 成果
テストデータセットではaccuracyで56%という結果となった
本番ではなかなか当たらないものの、三連複(三着以内に選んだ艇、順不同)を当てたこともある。OZ=2.6倍

## 振り返り
AIを作成する上で、データ取得からデータクリーニング、前処理、モデル構築、予測と、自身の力で一通り実装したことで、機械学習に対する自信がついた。
まだ、簡単な特徴量エンジニアリングしかできていないため、継続的に作成していきたい
次のステップとして、儲けることができるようにオッズを加味した上でどこに賭けるか、また賭けるべきかについての閾値を設けることで、
継続して勝てるボートレースAIを作成したいと考える。
