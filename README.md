# 智能系统设计与优化实验室 | ISDO

Intelligent System Design and Optimization Lab, Beijing Institute of Technology.

网页通过 GitHub Pages 发布。首页介绍刘欣的研究方向、教育和工作经历；`pi.html` 另列课程，指导学生页展示学生信息、毕业生和去向。各页均可切换中英文。

## 更新草稿

在 `source/content.py` 中更新双语简介、经历、课程及研究内容，在 `source/papers.json` 中维护论文，在 `source/students.json` 中维护成员和课题。毕业状态使用 `status: "graduated"`，或保留原有的毕业时间 `end`。

首页生活照保存在 `assets/xin-liu-life.jpg`。页脚使用北欧风 ISDO 标志 `assets/isdo-nordic.svg`。研究页所用的三幅论文插图分别来自 AGV 调度论文图 2、GAPGAN 论文图 4 和 KnowLoop 论文图 1。

在仓库根目录运行 `python source/build.py`，即可根据内容与照片重新生成本地网页。生成脚本只需 Python 标准库。
