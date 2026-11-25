# 智能系统设计与优化组 | ISDO

Intelligent System Design and Optimization Lab, Beijing Institute of Technology.

私有草稿可直接打开 `index.html` 或 `en/index.html` 浏览。首页以刘欣个人介绍为主，使用生活照；完整履历和教学信息在 `pi.html` 中。People 页面展示培养学生、研究方向和毕业去向。各页均可切换中英文。

## 更新草稿

在 `source/content.py` 中更新双语研究介绍和履历，在 `source/papers.json` 中维护论文，在 `source/students.json` 中维护成员和课题。三幅研究图分别来自 AGV 调度论文图 2、GAPGAN 论文图 4 和 KnowLoop 论文图 1，研究页图注附有 DOI 来源。

首页生活照保存在 `assets/xin-liu-life.jpg`。研究页所用的三幅论文插图分别来自 AGV 调度论文图 2、GAPGAN 论文图 4 和 KnowLoop 论文图 1。

在仓库根目录运行 `python source/build.py`，即可根据内容与照片重新生成本地网页。生成脚本只需 Python 标准库。
