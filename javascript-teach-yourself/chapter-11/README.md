## chapter-11

### exercise 11-1

- 11-1.htmlに記載

### exercise 11-2

- 11-2.htmlに記載

### exercise 11-3

- 11-3.htmlに記載

### exercise 11-4

- 11-4.htmlに記載

### 理解度チェック

[1] chapter-11-check-01.htmlに記載

[2] chapter-11-check-02.htmlに記載

[3] WeakMapとMapの違い
- Mapの場合はすべてのデータ型をキーとして利用できるが、WeakMapの場合はオブジェクトしかキーとして利用できない
- Mapの場合はfor...of文などを使用した反復処理が可能だが、WeakMapではできない
- キーとして利用したオブジェクトが参照不可になった場合、Mapではキーと値のペアが残り続けるため、メモリリークのリスクが発生する
- 一方でWeakMapはキーオブジェクトが参照不可になるとコレクション内のペアも削除対象となる、この性質を弱参照と呼ぶ

