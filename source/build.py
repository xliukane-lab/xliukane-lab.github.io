from pathlib import Path
from html import escape
from collections import defaultdict
import json
from content import LAB_ZH, LAB_EN, FACULTY, SCHOLAR, EMAIL, CAREER, TRACKS, WORKS

SOURCE = Path(__file__).resolve().parent
SITE = SOURCE.parent
PAPERS = json.loads((SOURCE/'papers.json').read_text(encoding='utf8'))
STUDENTS = json.loads((SOURCE/'students.json').read_text(encoding='utf8'))
PHOTO_SLOTS = {
    'group': ('课题组合影', 'Group portrait'),
    'seminar': ('研讨交流', 'Seminars and exchanges'),
    'graduation': ('毕业留念', 'Graduation memories'),
}
DESTINATIONS = [
    (('互联网与物流','Technology and logistics'),('美团 · 拼多多 · 百度 · 京东物流 · 字节跳动','Meituan · Pinduoduo · Baidu · JD Logistics · ByteDance')),
    (('汽车与制造','Automotive and manufacturing'),('理想汽车 · 比亚迪 · 蔚来汽车 · 米其林轮胎 · 云南烟草','Li Auto · BYD · NIO · Michelin · Yunnan Tobacco')),
    (('科研与公共部门','Research and public service'),('航天五院 · 适航院 · 政府部门','China Academy of Space Technology · an airworthiness institute · government departments')),
    (('高校深造','Further study'),('香港城市大学 · 哈尔滨工业大学','City University of Hong Kong · Harbin Institute of Technology')),
]
def link(href, label, css=''):
    return f'<a class="{css}" href="{escape(href,quote=True)}">{label}</a>'

class Site:
    def __init__(self, english):
        self.i = int(english)
        self.dir = SITE/'en' if english else SITE
        self.assets = '../assets/' if english else 'assets/'
        self.lang = 'en' if english else 'zh-CN'
        self.other = '../' if english else 'en/'
        self.name = self.t(LAB_ZH, LAB_EN)
        self.nav = {'index':self.t('首页','Home'),'research':self.t('研究','Research'),'publications':self.t('论文','Publications'),'people':self.t('团队','People')}
    def t(self,zh,en):
        return (zh,en)[self.i]
    def pair(self,values):
        return values[self.i]
    def shell(self,page,title,body):
        navigation=''.join(f'<a href="{slug}.html"'+(' aria-current="page"' if slug==page else '')+f'>{label}</a>' for slug,label in self.nav.items())
        language=self.t('English','中文')
        switch=f'<a class="language" lang="{self.t("en","zh-CN")}" href="{self.other}{page}.html">{language}</a>'
        header=f'<header><div class="wrap bar">{link("index.html","<b>ISDO</b><span>"+self.name+"</span>","brand")}<nav aria-label="{self.t("主导航","Main navigation")}">{navigation}</nav>{switch}</div></header>'
        footer=f'<footer><div class="wrap"><div><b>ISDO</b><p lang="en">{LAB_EN}</p><p lang="zh-CN">{LAB_ZH}</p></div><div>{link("mailto:"+EMAIL,EMAIL)}<p>{self.t("北京理工大学机械与车辆学院","School of Mechanical Engineering, Beijing Institute of Technology")}</p></div></div></footer>'
        html=f"""<!doctype html>
<html lang="{self.lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | ISDO</title><link rel="stylesheet" href="{self.assets}style.css"><link rel="alternate" hreflang="{self.t('en','zh-CN')}" href="{self.other}{page}.html"></head>
<body><a class="skip" href="#main">{self.t('跳至正文','Skip to content')}</a>{header}
<main id="main">{body}</main>{footer}</body></html>"""
        self.dir.mkdir(exist_ok=True)
        (self.dir/(page+'.html')).write_bytes((html+'\n').encode('utf8'))
    def photo(self,key):
        label=self.pair(PHOTO_SLOTS[key])
        for ext in ['jpg','jpeg','webp','png']:
            file=f'photos/{key}.{ext}'
            if (SITE/'assets'/file).is_file():
                return f'<figure class="photo-slot"><img src="{self.assets+file}" alt="{label}"><figcaption>{label}</figcaption></figure>'
        if key == 'group':
            caption = self.t('风电研究场景', 'Wind energy research')
            scene = self.t('山地风力发电机组', 'A wind turbine in a mountain landscape')
            return (f'<figure class="photo-slot lab-scene"><img src="{self.assets}wind.webp" alt="{scene}">'
                    f'<figcaption>{link("research.html#energy", caption+" ↗")}</figcaption></figure>')
        return f'<figure class="photo-slot empty"><div class="photo-space"><span>{self.t("照片待补充","Photograph forthcoming")}</span></div><figcaption>{label}</figcaption></figure>'
    def reference(self,key):
        p=PAPERS[key]
        authors=', '.join('<b>'+escape(a)+'</b>' if a.lower()=='xin liu' else escape(a) for a in p['authors'])
        return f'<div class="reference"><span class="venue">{escape(p["journal"])} · {p["year"]}</span><h3>{link("https://doi.org/"+p["doi"],escape(p["title"])+" ↗")}</h3><p>{authors}</p></div>'
    def pi(self):
        person=self.t('刘欣','Xin Liu')
        affiliation=self.t('北京理工大学机械与车辆学院','School of Mechanical Engineering · Beijing Institute of Technology')
        role=self.t('工业与智能系统工程研究所所长','Director, Institute of Industrial and Intelligent Systems Engineering')
        rank=self.t('特别副研究员 / 预聘助理教授 · 硕士生导师','Special Associate Research Fellow / Tenure-track Assistant Professor · Master’s Supervisor')
        summary=self.t('我关注数据能为工程决策提供什么依据。我的研究从设备和环境的观测出发，考察码头车辆该怎样调度、风电场下一小时可能出现哪些风况，以及工程师怎样把模糊需求变成可以比较的设计方案。','My research asks what operational data can tell an engineer before a decision is made. I study how to dispatch vehicles at a container terminal, what winds a farm may experience in the next hour, and how engineers can turn ambiguous requirements into design alternatives they can compare.')
        address=self.t('北京市海淀区 · 北京理工大学中关村校区第一教学楼 344A','Room 344A, Teaching Building 1, Zhongguancun Campus, BIT, Beijing')
        hero=f'<section class="profile"><div class="wrap profile-grid"><div><div class="affiliation">{affiliation}</div><h1>{person}</h1><p class="position">{role}</p><p class="rank">{rank}</p><p class="summary">{summary}</p><div class="contact">{link("mailto:"+EMAIL,EMAIL)} {link(FACULTY,self.t("学院主页","Faculty profile")+" ↗")} {link(SCHOLAR,"Google Scholar ↗")}</div><small>{address}</small></div><figure class="portrait"><img src="{self.assets}xin-liu.jpg" width="460" height="690" alt="{person}"></figure></div></section>'
        timeline = ''.join(f'<li><time>{escape(row[0])}</time><div>{row[1+self.i]}</div></li>' for row in CAREER)
        education = self.t('个人履历','Education and appointments')
        teaching = self.t('课程与研究指导','Teaching and supervision')
        teaching_text = self.t(
            '刘欣为本科生讲授《智能制造系统》和《制造系统感知分析与决策》，并参与研究生《工程管理》课程教学。他指导的学生课题涵盖制造系统调度、风电功率预测和生成式产品概念设计。',
            'Xin Liu teaches undergraduate courses on intelligent manufacturing systems and on sensing, analysis and decision-making in manufacturing. He also teaches engineering management at the graduate level. His students study problems ranging from manufacturing scheduling and wind power forecasting to generative product design.')
        team_link = link('people.html', self.t('查看团队成员与学生课题','Meet the team and explore student projects')+' →')
        biography = (f'<section class="wrap section history"><div><h2>{education}</h2>'
                     f'<ol class="timeline">{timeline}</ol></div><div class="teaching">'
                     f'<h2>{teaching}</h2><p>{teaching_text}</p>{team_link}</div></section>')
        self.shell('pi',person+' · PI',hero+biography)

    def home(self):
        affiliation = self.t('北京理工大学 · 机械与车辆学院',
                             'School of Mechanical Engineering · Beijing Institute of Technology')
        summary = self.t(
            '我们研究如何利用工业数据和工程知识改进系统设计与运行决策。在集装箱码头，我们研究车辆如何响应不断到达的运输任务。在风电场，我们关注来风的不确定性如何影响机组协同控制。在产品设计中，我们探索怎样把用户的需求转化为可供工程师比较的概念方案。',
            'We use industrial data and engineering knowledge to improve how systems are designed and operated. At container terminals, we study how vehicles can respond as new jobs arrive. At wind farms, we investigate how uncertain winds affect coordinated turbine control. In product design, we explore how engineers can turn user needs into concepts they can compare.')
        research_link = link('research.html', self.nav['research']+self.t('介绍',' overview')+' →', 'lab-action')
        team_link = link('people.html', self.t('认识团队','Meet the team')+' →')
        hero = (f'<section class="lab-hero"><div class="wrap lab-grid"><div><p class="affiliation">{affiliation}</p>'
                f'<h1>{self.name}</h1><p class="lab-summary">{summary}</p>'
                f'<div class="lab-links">{research_link}{team_link}</div></div>{self.photo("group")}</div></section>')
        cards=''.join(f'<a class="direction" href="research.html#{tr["id"]}"><h3>{self.pair(tr["name"])} <span>↗</span></h3><p>{self.pair(tr["intro"])}</p></a>' for tr in TRACKS)
        directions=f'<section class="wrap section"><h2>{self.t("研究方向","Research areas")}</h2><div class="cards">{cards}</div></section>'
        spot=[]
        for tr in TRACKS:
            k=tr['works'][0]
            p=PAPERS[k]
            spot.append(f'<article><p class="venue">{escape(p["journal"])} · {p["year"]}</p><h3>{link("research.html#work-"+k,self.pair(WORKS[k][0])+" ↗")}</h3><p>{self.pair(WORKS[k][1])}</p></article>')
        typical=f'<section class="tint"><div class="wrap section"><h2>{self.t("典型论文","Research highlights")}</h2><div class="highlights">{"".join(spot)}</div></div></section>'
        person = self.t('刘欣','Xin Liu')
        role = self.t('课题组负责人（PI）','Principal investigator')
        appointment = self.t('北京理工大学工业与智能系统工程研究所所长，硕士生导师。',
                             'Director of the Institute of Industrial and Intelligent Systems Engineering at BIT and supervisor of master’s students.')
        profile_link = link('pi.html', self.t('查看刘欣的个人资料','View Xin Liu’s profile')+' →')
        pi_card = (f'<section class="wrap section pi-card"><img src="{self.assets}xin-liu.jpg" alt="{person}" width="94" height="118">'
                   f'<div><p class="affiliation">{role}</p><h2>{person}</h2><p>{appointment}</p>'
                   f'<div class="contact">{profile_link}{link("mailto:"+EMAIL,EMAIL)}</div></div></section>')
        self.shell('index',self.name,hero+directions+typical+pi_card)
    def research(self):
        navigation=''.join(link('#'+tr['id'],self.pair(tr['name'])) for tr in TRACKS)
        body=f'<div class="wrap section page-top"><h1>{self.t("研究","Research")}</h1><div class="jump">{navigation}</div></div>'
        sections=[]
        for tr in TRACKS:
            k=tr['figure']
            figlink=self.assets+f'figure-{k}.webp'
            caption=self.pair(tr['fig'])
            fig=f'<figure class="paper-figure"><a href="{figlink}" aria-label="{self.t("放大论文插图","Enlarge figure")}"><img src="{figlink}" alt="{caption}" loading="lazy"></a><figcaption>{caption} {link("https://doi.org/"+PAPERS[k]["doi"],self.t("原文","Source")+" ↗")}</figcaption></figure>'
            left=f'<div><h2>{self.pair(tr["name"])}</h2><p class="intro">{self.pair(tr["intro"])}</p><p>{self.pair(tr["scope"])}</p><p class="project"><b>{self.t("相关项目","Projects")}</b>{self.pair(tr["project"])}</p></div>'
            examples=[]
            for key in tr['works']:
                title,summary=WORKS[key]
                examples.append(f'<article class="study" id="work-{key}"><div><h3>{self.pair(title)}</h3><p>{self.pair(summary)}</p></div>{self.reference(key)}</article>')
            extra=''
            if tr['id']=='energy':
                extra=link('https://doi.org/'+PAPERS['yaw']['doi'],self.t('延伸阅读 · 多机组协同偏航控制','Related work · Coordinated yaw control for a turbine cluster')+' ↗','more')
            sections.append(f'<section class="track wrap" id="{tr["id"]}"><div class="track-head">{left}{fig}</div><h3 class="section-label">{self.t("代表工作","Selected studies")}</h3>{"".join(examples)}{extra}</section>')
        self.shell('research',self.nav['research'],body+''.join(sections))
    def publications(self):
        by_year=defaultdict(list)
        for key,p in PAPERS.items():
            by_year[p['year']].append(key)
        body=f'<section class="wrap section page-top"><h1>{self.t("论文成果","Publications")}</h1><p class="intro">{self.t("本页收录可通过 DOI 查阅的期刊与会议论文。更多成果请见按发表时间排序的学术主页。","Browse journal and conference papers with DOI links. The Google Scholar profile lists additional work by publication date.")}</p>{link(SCHOLAR,"Google Scholar ↗","more")}</section>'
        for year,keys in sorted(by_year.items(),reverse=True):
            refs=''.join(self.reference(k) for k in sorted(keys,key=lambda x:PAPERS[x]['title']))
            body+=f'<section class="wrap pub-year"><h2>{year}</h2><div>{refs}</div></section>'
        self.shell('publications',self.nav['publications'],body)
    def roster(self,students):
        groups=defaultdict(list)
        for s in students:
            groups[s['start'][:4]].append(s)
        rows=''
        for year,group in sorted(groups.items(),reverse=True):
            entries=[]
            for s in group:
                display=s['name'] if not self.i else f'{s["roman"]} <span lang="zh-CN">{s["name"]}</span>'
                entries.append(f'<li><b>{display}</b><div>{escape(self.pair(s["topic"]))}</div></li>')
            rows+=f'<div class="cohort"><h4>{year}</h4><ul>{"".join(entries)}</ul></div>'
        return rows
    def people(self):
        degrees=[s for s in STUDENTS if s['degree']=='M']
        current=self.roster([s for s in degrees if not s['end']])
        alumni=self.roster([s for s in degrees if s['end']])
        undergrad=self.roster([s for s in STUDENTS if s['degree']=='B'])
        person=self.t('刘欣','Xin Liu')
        header=f'<section class="wrap section page-top"><h1>{self.t("团队成员","People")}</h1><div class="people-lead"><img src="{self.assets}xin-liu.jpg" alt="{person}" width="72" height="90"><div><h2>{person}</h2><p>{self.t("课题组负责人（PI）","Principal investigator")} · {link("pi.html",self.t("个人资料","Profile"))}</p></div></div></section>'
        def heading(title,en): return f'<h2>{self.t(title,en)}</h2>'
        body=f'<section class="wrap team-section">{heading("在组硕士生","Master’s students")}<p>{self.t("按入学年份列示。","Grouped by entry year.")}</p>{current}</section>'
        body+=f'<section class="wrap team-section">{heading("历届硕士生","Master’s alumni")}<p>{self.t("按入学年份列示。","Grouped by entry year.")}</p>{alumni}</section>'
        body+=f'<section class="wrap team-section"><details><summary>{self.t("本科毕业设计","Undergraduate thesis projects")}</summary>{undergrad}</details></section>'
        dest=''.join(f'<div><h3>{self.pair(group)}</h3><p>{self.pair(names)}</p></div>' for group,names in DESTINATIONS)
        body+=f'<section class="tint"><div class="wrap section">{heading("毕业生去向","Alumni destinations")}<div class="destinations">{dest}</div></div></section>'
        body+=f'<section class="wrap section">{heading("课题组相册","Group album")}<div class="album">{self.photo("seminar")}{self.photo("graduation")}</div></section>'
        self.shell('people',self.nav['people'],header+body)
    def legacy_links(self):
        for old,anchor in {'operations':'manufacturing','machine-health':'manufacturing','wind-energy':'energy','engineering-design':'design'}.items():
            dest='research.html#'+anchor
            (self.dir/(old+'.html')).write_text(f'<!doctype html><html lang="{self.lang}"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={dest}"><title>{self.nav["research"]} | ISDO</title></head><body>{link(dest,self.nav["research"])}</body></html>',encoding='utf8')

if __name__=='__main__':
    for en in (False,True):
        site=Site(en)
        site.home()
        site.pi()
        site.research()
        site.publications()
        site.people()
        site.legacy_links()
