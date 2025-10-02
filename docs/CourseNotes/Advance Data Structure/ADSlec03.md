## 倒排索引

- [NoughtQ 的笔记本-倒排索引](https://note.noughtq.top/algorithms/ads/3)
- [Isshiki 修's Notebook-倒排索引](https://note.isshikih.top/cour_note/D2CX_AdvancedDataStructure/Lec03/)

**倒排索引**（inverted file index）是一种常见的文本检索技术，用于快速查找包含特定单词或短语的文档。它通过将单词或短语作为关键字，并将它们出现在文档中的位置记录在一个索引中，从而支持快速的文本检索。在搜索过程中，系统可以快速地定位包含指定单词或短语的文档，并返回它们的相关信息。倒排索引广泛应用于搜索引擎、数据库系统和信息检索等领域。

**压缩：**

数字太大，存储相邻两个位置的差分
