# 智能系统设计与优化实验室 | ISDO

Intelligent System Design and Optimization Lab, Beijing Institute of Technology.

私有草稿可直接打开 `index.html` 或 `en/index.html` 浏览。首页包含个人简介、学习和工作经历，并展示研究方向和典型论文；个人资料页 `pi.html` 另列课程。People 页面展示学生、已毕业校友和毕业去向。各页均可切换中英文。

## 更新草稿

在 `source/content.py` 中更新双语简介、经历、课程及研究内容，在 `source/papers.json` 中维护论文，在 `source/students.json` 中维护成员和课题。毕业状态使用 `status: "graduated"`，或保留原有的毕业时间 `end`。

首页生活照保存在 `assets/xin-liu-life.jpg`。研究页所用的三幅论文插图分别来自 AGV 调度论文图 2、GAPGAN 论文图 4 和 KnowLoop 论文图 1。

在仓库根目录运行 `python source/build.py`，即可根据内容与照片重新生成本地网页。生成脚本只需 Python 标准库。
