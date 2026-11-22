# 刘欣课题组 · Xin Liu Research Group

北京理工大学刘欣课题组的中英双语研究主页。打开 `index.html` 即可在本地浏览。英文入口为 `en/index.html`。

## 更新内容

双语研究介绍在 `source/content.py`，两个版本的论文清单共同读取 `source/papers.json`。主页简介、个人简介及页面模板在 `source/build.py`，样式在 `assets/style.css`。

编辑后，从仓库根目录运行以下命令。脚本使用 Python 3 标准库，无需安装依赖。

```sh
python source/build.py
```

将源文件和生成的 HTML 一并提交到 `main`。GitHub Pages 的发布来源为 `main` 分支的根目录。

## 资料来源

个人介绍与学术联系信息来自[北京理工大学教师主页](https://me.bit.edu.cn/szdw/jsml/zzgcx/gygcyjs/gygcyjsqnjs/127ba53935674ff2b9f8f99c90305632.htm)。论文链接使用各文章的 DOI。首页风机照片来自 [Pexels](https://www.pexels.com/photo/414837/)，遵循 [Pexels License](https://www.pexels.com/license/)。照片用于说明研究场景。
