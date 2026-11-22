from pathlib import Path
from html import escape
import json, os, posixpath

# Static pages use relative URLs so the same files work on GitHub Pages and offline.
from content import TOPICS, FACULTY, SCHOLAR, GITHUB, EMAIL
HERE = Path(__file__).resolve().parent
SITE = HERE.parent
PAPERS = json.loads((HERE/'papers.json').read_text(encoding='utf-8'))
PHOTO = 'https://www.pexels.com/photo/414837/'

def generate(lang):
    zh = lang == 'zh'
    def label(cn, en): return cn if zh else en
    prefix = '' if zh else 'en/'
    other = 'en/' if zh else ''
    name = label('刘欣课题组','Xin Liu Research Group')
    faculty = label('北京理工大学机械与车辆学院','School of Mechanical Engineering, Beijing Institute of Technology')
    research = label('研究方向','Research')
    pubs = label('代表论文','Publications')
    team = label('团队与联系','People & contact')
    def paperlist(keys):
        rows = []
        for key in keys:
            p = PAPERS[key]
            authors = ', '.join('<strong>Xin Liu</strong>' if a.lower()=='xin liu' else escape(a) for a in p['authors'])
            rows.append(f'<li class="paper"><span class="year">{p["year"]}</span><div><p class="journal">{escape(p["journal"])}</p><a class="paper-title" href="https://doi.org/{p["doi"]}">{escape(p["title"])} <span aria-hidden="true">↗</span></a><p class="authors">{authors}</p></div></li>')
        return '<ul class="papers">'+''.join(rows)+'</ul>'
    for page in ['index','publications','people']+[t['slug'] for t in TOPICS]:
        filename=page+'.html'
        def url(target): return posixpath.relpath(target,prefix or '.')
        home=url(prefix+'index.html')
        allpapers=url(prefix+'publications.html')
        bio=url(prefix+'people.html')
        asset=url('assets')+'/'
        switch=url(other+filename)
        def navlink(target,text,active):
            attr=' aria-current="page"' if active else ''
            return f'<a href="{target}"{attr}>{text}</a>'
        nav = navlink(home+'#research',research,False)+navlink(allpapers,pubs,page=='publications')+navlink(bio,team,page=='people')
        bilingual = f'<a class="language" href="{switch}" hreflang="{label("en","zh-CN")}" lang="{label("en","zh-CN")}">{label("English","中文")}</a>'
        header=f'<header><div class="bar"><a class="brand" href="{home}"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span>{name}</span></a><nav aria-label="{label("主导航","Main navigation")}">{nav}</nav>{bilingual}</div></header>'
        def action(href,txt,cls='textlink',arrow='→'):
            return f'<a class="{cls}" href="{escape(href,quote=True)}">{txt} <span aria-hidden="true">{arrow}</span></a>'
        if page=='index':
            title=label('工业智能研究','Industrial intelligence research')
            desc=label('北京理工大学刘欣课题组研究工业智能，面向可再生能源、生产制造及工程设计开展预测建模与优化决策研究。','We study predictive modelling and decision-making for renewable energy, manufacturing, and engineering design at Beijing Institute of Technology.')
            kicker=label('北京理工大学 · 机械与车辆学院','Beijing Institute of Technology')
            headline=label('工业智能研究','Industrial intelligence')
            deck=label('从风电场的下一小时，到集装箱码头的下一次派车，我们研究如何从运行数据中作出更好的工程决策。','From the next hour at a wind farm to the next dispatch at a container terminal, we study how operational data can inform engineering decisions.')
            hero=f'<section class="hero"><div class="hero-photo"></div><div class="hero-layout"><div class="hero-copy"><p class="hero-kicker">{kicker}</p><h1>{headline}</h1><p class="deck">{deck}</p>{action("#research",label("探索研究方向","Explore our research"),"button","↓")}</div></div></section>'
            cards=[]
            for t in TOPICS:
                d=t[lang]
                cards.append(f'<li><a class="topic-card" href="{t["slug"]}.html"><p class="category">{d["tag"]}</p><h3>{d["name"]}</h3><p>{d["intro"]}</p><span class="round" aria-hidden="true">↗</span></a></li>')
            research_section=f'<section class="wrap block" id="research"><h2>{research}</h2><ul class="topic-grid">{"".join(cards)}</ul></section>'
            psection=f'<section class="tint"><div class="wrap block"><div class="section-head"><h2>{label("近期代表论文","Recent publications")}</h2>{action(allpapers,label("全部代表论文","All selected papers"))}</div>{paperlist(["design","fault","impute"])}</div></section>'
            people_section=f'<section class="wrap block strip"><div><p class="category">{label("团队与联系","People & contact")}</p><h2>{label("认识刘欣课题组","Meet the group")}</h2><p>{label("我们在北京理工大学开展工业智能研究，也把风电预测和制造决策中的问题带进课堂与学生研究项目。","At Beijing Institute of Technology, our research and teaching connect industrial intelligence with practical problems in energy and manufacturing.")}</p></div>{action(bio,label("负责人及联系方式","Group lead and contact"))}</section>'
            body=hero+research_section+psection+people_section
        elif page=='publications':
            title=pubs
            desc=label('按发表年份浏览课题组的代表性研究，并通过 DOI 阅读论文。','Browse selected research by publication year and follow the DOI links to the papers.')
            keys=sorted(PAPERS,key=lambda k:-PAPERS[k]['year'])
            body=f'<section class="wrap article-top"><p class="category">{name}</p><h1>{title}</h1><p class="lead">{desc}</p>{action(SCHOLAR,label("Google Scholar 完整列表","Full list on Google Scholar"),arrow="↗")}</section><section class="wrap listbody">{paperlist(keys)}</section>'
        elif page=='people':
            title=team
            desc=label('了解刘欣的研究背景、课程教学与学术联系方式。','Learn about Xin Liu’s research, teaching, and academic contact details.')
            role=label('课题组负责人 · 硕士生导师','Group lead · Master’s supervisor')
            person=label('刘欣','Xin Liu')
            bio1=label('刘欣现任北京理工大学机械与车辆学院工业与智能系统工程研究所所长。2016 年于北京理工大学获得工业工程专业学士学位，2021 年于香港城市大学获得数据科学博士学位。','Xin Liu directs the Institute of Industrial and Intelligent Systems Engineering at Beijing Institute of Technology. He earned a bachelor’s degree in industrial engineering from BIT in 2016 and a PhD in data science from City University of Hong Kong in 2021.')
            bio2=label('他的研究从工业系统的运行数据出发，先刻画设备与环境的不确定性，再研究预测信息如何服务于控制与调度。他主持国家自然科学基金青年科学基金项目和面上项目，研究涉及可再生能源场景生成以及群智创新设计。','His research uses operational data to characterise uncertainty in equipment and its environment, and studies how forecasts can inform control and scheduling. He has led Young Scientists Fund and General Program projects funded by the National Natural Science Foundation of China, with work on renewable energy scenarios and collaborative design.')
            teach=label('在《智能制造系统》和《制造系统感知分析与决策》等课程中，刘欣将工程问题引入教学。学生研究课题包括用不完整的观测预测风电出力，以及识别不同运行条件下的旋转设备故障。','Xin Liu teaches courses including Intelligent Manufacturing Systems and Sensing, Analysis and Decision-Making for Manufacturing Systems. Student research has examined how to forecast wind power from incomplete records and recognise faults in rotating machines across operating conditions.')
            body=f'<section class="wrap article-top"><h1>{title}</h1></section><section class="wrap person"><img width="288" height="432" alt="{person}" src="{asset}xin-liu.jpg"><div><p class="category">{role}</p><h2>{person}</h2><p>{bio1}</p><p>{bio2}</p>{action(FACULTY,label("学院教师主页","University profile"),arrow="↗")}</div></section><section class="wrap narrative"><h2>{label("课程与研究训练","Teaching and research training")}</h2><p>{teach}</p><h2>{label("学术联系","Get in touch")}</h2><p>{label("如希望交流研究问题、了解学生课题或讨论合作，欢迎通过学校邮箱联系刘欣。","For questions about research, student projects or collaboration, contact Xin Liu by email.")}</p>{action("mailto:"+EMAIL,EMAIL,arrow="↗")}</section>'
        else:
            topic=next(t for t in TOPICS if t['slug']==page)
            d=topic[lang]
            title=d['name']
            desc=d['intro']
            narrative=''.join(f'<section><h2>{h}</h2><p>{p}</p></section>' for h,p in d['sections'])
            body=f'<div class="topic-intro"><div class="wrap article-top">{action(home+"#research",research,"crumb","↑")}<p class="category">{d["tag"]}</p><h1>{title}</h1><p class="lead">{desc}</p></div></div><div class="wrap narrative">{narrative}</div><section class="tint"><div class="wrap block"><div class="section-head"><h2>{pubs}</h2>{action(allpapers,label("全部代表论文","All selected papers"))}</div>{paperlist(topic["papers"])}</div></section>'
        footer=f'<footer><div class="wrap foot"><div><b>{name}</b><p>{faculty}</p></div><div><a href="{GITHUB}">GitHub ↗</a><a href="mailto:{EMAIL}">{EMAIL}</a></div></div></footer>'
        locale=label('zh-CN','en')
        html=f'''<!doctype html>
<html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{escape(desc,quote=True)}"><link rel="alternate" hreflang="{label('en','zh-CN')}" href="{switch}"><link rel="stylesheet" href="{asset}style.css"><title>{title} | {name}</title></head><body>
<a class="skip" href="#main">{label('跳至正文','Skip to content')}</a>{header}
<main id="main">{body}</main>{footer}
</body></html>'''
        dest=SITE/prefix/filename
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(html,encoding='utf8')
if __name__=='__main__':
    for language in ['zh','en']:
        generate(language)
