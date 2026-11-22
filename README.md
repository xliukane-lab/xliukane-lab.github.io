# 智能系统设计与优化组 | ISDO

Intelligent System Design and Optimization Lab, Beijing Institute of Technology.

私有草稿可直接打开 `index.html` 或 `en/index.html` 浏览。首页介绍课题组，首页及团队页的 PI 卡片链接至独立个人资料页 `pi.html`。各页均可切换中英文。

## 更新草稿

在 `source/content.py` 中更新双语研究介绍和履历，在 `source/papers.json` 中维护论文，在 `source/students.json` 中维护成员和课题。三幅研究图分别来自 AGV 调度论文图 2、GAPGAN 论文图 4 和 KnowLoop 论文图 1，研究页图注附有 DOI 来源。

课题组照片放入 `assets/photos/` 文件夹。首页合影使用文件名 `group.jpg`，添加合影前显示[风电场景配图](https://www.pexels.com/photo/414837/)。团队页的研讨照片和毕业留念分别使用 `seminar.jpg` 和 `graduation.jpg`。也支持同名的 WebP 或 PNG 文件。

在仓库根目录运行 `python source/build.py`，即可根据内容与照片重新生成本地网页。生成脚本只需 Python 标准库。
