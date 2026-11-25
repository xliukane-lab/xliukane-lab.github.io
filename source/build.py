from pathlib import Path
from html import escape
from collections import defaultdict
import json
from content import LAB_ZH, LAB_EN, FACULTY, SCHOLAR, EMAIL, BIO, EDUCATION, APPOINTMENTS, COURSES, TRACKS, WORKS

SOURCE = Path(__file__).resolve().parent
SITE = SOURCE.parent
PAPERS = json.loads((SOURCE/'papers.json').read_text(encoding='utf8'))
STUDENTS = json.loads((SOURCE/'students.json').read_text(encoding='utf8'))
DESTINATIONS = [
    (('互联网与物流','Technology and logistics'),('美团 · 拼多多 · 百度 · 京东物流 · 字节跳动','Meituan · Pinduoduo · Baidu · JD Logistics · ByteDance')),
    (('汽车与制造','Automotive and manufacturing'),('比亚迪 · 蔚来汽车 · 米其林轮胎 · 中国烟草','BYD · NIO · Michelin · China Tobacco')),
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
        self.name = self.t('刘欣', 'Xin Liu')
        self.nav = {'index':self.t('首页','Home'),'research':self.t('研究','Research'),'publications':self.t('论文','Publications'),'people':self.t('指导学生','Students')}
    def t(self,zh,en):
        return (zh,en)[self.i]
    def pair(self,values):
        return values[self.i]
    def shell(self,page,title,body):
        navigation=''.join(f'<a href="{slug}.html"'+(' aria-current="page"' if slug==page else '')+f'>{label}</a>' for slug,label in self.nav.items())
        language=self.t('English','中文')
        switch=f'<a class="language" lang="{self.t("en","zh-CN")}" href="{self.other}{page}.html">{language}</a>'
        brand_name=self.t('刘  欣', 'Xin Liu')
        header=f'<header><div class="wrap bar">{link("index.html","<b>"+brand_name+"</b>","brand")}<nav aria-label="{self.t("主导航","Main navigation")}">{navigation}</nav>{switch}</div></header>'
        footer=f'<footer><div class="wrap"><div><img class="footer-logo" src="{self.assets}isdo-nordic.svg" alt="ISDO"><p lang="en">{LAB_EN}</p><p lang="zh-CN">{LAB_ZH}</p></div><div>{link("mailto:"+EMAIL,EMAIL)}<p>{self.t("北京理工大学机械与车辆学院","School of Mechanical Engineering, Beijing Institute of Technology")}</p></div></div></footer>'
        html=f"""<!doctype html>
<html lang="{self.lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | ISDO</title><link rel="stylesheet" href="{self.assets}style.css"><link rel="alternate" hreflang="{self.t('en','zh-CN')}" href="{self.other}{page}.html"></head>
<body><a class="skip" href="#main">{self.t('跳至正文','Skip to content')}</a>{header}
<main id="main">{body}</main>{footer}</body></html>"""
        self.dir.mkdir(exist_ok=True)
        (self.dir/(page+'.html')).write_bytes((html+'\n').encode('utf8'))
    def reference(self,key):
        p=PAPERS[key]
        authors=', '.join('<b>'+escape(a)+'</b>' if a.lower()=='xin liu' else escape(a) for a in p['authors'])
        return f'<div class="reference"><span class="venue">{escape(p["journal"])} · {p["year"]}</span><h3>{link("https://doi.org/"+p["doi"],escape(p["title"])+" ↗")}</h3><p>{authors}</p></div>'
    def experiences(self):
        columns = []
        for title, entries in [(self.t('个人经历', 'Education'), EDUCATION),
                               (self.t('工作经历', 'Appointments'), APPOINTMENTS)]:
            rows = []
            for date, institution, discipline, qualification in entries:
                when = date.replace('至今', 'present') if self.i else date
                rows.append(f'<li><time>{when}</time><div>{self.pair(institution)}</div><div>{self.pair(discipline)}</div><div>{self.pair(qualification)}</div></li>')
            columns.append(f'<section><h2>{title}</h2><ul class="timeline structured">{"".join(rows)}</ul></section>')
        return '<div class="wrap section experience-grid">'+''.join(columns)+'</div>'

    def courses(self):
        head = self.t(('课程','专业 / 对象','课程性质'), ('Course','Programme / audience','Course type'))
        headings = ''.join(f'<th scope="col">{column}</th>' for column in head)
        rows = ''.join('<tr>'+''.join(f'<td>{escape(self.pair(value))}</td>' for value in course)+'</tr>' for course in COURSES)
        return (f'<section class="wrap section teaching"><h2>{self.t("课程与研究指导", "Teaching")}</h2>'
                f'<div class="table-scroll"><table class="courses"><thead><tr>{headings}</tr></thead>'
                f'<tbody>{rows}</tbody></table></div></section>')
    def pi(self):
        person=self.t('刘欣','Xin Liu')
        affiliation=self.t('北京理工大学机械与车辆学院','School of Mechanical Engineering · Beijing Institute of Technology')
        role=self.t('工业与智能系统工程研究所所长','Director, Institute of Industrial and Intelligent Systems Engineering')
        rank=self.t('特别副研究员 / 预聘助理教授 · 硕士生导师','Special Associate Research Fellow / Tenure-track Assistant Professor · Master’s Supervisor')
        summary=self.pair(BIO)
        hero=f'<section class="profile"><div class="wrap profile-grid"><div><div class="affiliation">{affiliation}</div><h1 class="person-name">{self.t("刘  欣",person)}</h1><p class="position">{role}</p><p class="rank">{rank}</p><p class="summary">{summary}</p><div class="contact">{link("mailto:"+EMAIL,EMAIL)} {link(FACULTY,self.t("学院主页","Faculty profile")+" ↗")} {link(SCHOLAR,"Google Scholar ↗")}</div></div><figure class="portrait"><img src="{self.assets}xin-liu.jpg" width="460" height="690" alt="{person}"></figure></div></section>'
        self.shell('pi',person,hero+self.experiences()+self.courses())

    def home(self):
        affiliation = self.t('北京理工大学机械与车辆学院',
                             'School of Mechanical Engineering · Beijing Institute of Technology')
        role = self.t('工业与智能系统工程研究所所长',
                      'Director, Institute of Industrial and Intelligent Systems Engineering')
        rank = self.t('特别副研究员 / 预聘助理教授 · 硕士生导师',
                      'Special Associate Research Fellow / Tenure-track Assistant Professor · Master’s Supervisor')
        summary = self.pair(BIO)
        faculty_link = link(FACULTY, self.t('学院教师主页', 'Faculty profile')+' ↗')
        scholar_link = link(SCHOLAR, 'Google Scholar ↗')
        profile_link = link('pi.html', self.t('个人资料', 'Profile')+' →')
        hero = (
            f'<section class="profile profile-home"><div class="wrap home-grid">'
            f'<figure class="home-photo"><img class="home-photo-image" src="{self.assets}xin-liu-life.jpg" '
            f'alt="{self.t("刘欣在罗马斗兽场参观时的生活照", "Xin Liu visiting the Colosseum in Rome")}"></figure>'
            f'<div class="home-copy"><p class="affiliation">{affiliation}</p><h1 class="person-name">{self.t("刘  欣",self.name)}</h1>'
            f'<p class="position">{role}</p><p class="rank">{rank}</p><p class="summary">{summary}</p>'
            f'<div class="contact">{link("mailto:"+EMAIL,EMAIL)} {faculty_link} {scholar_link}</div>'
            f'<p class="profile-more">{profile_link}</p></div></div></section>')
        cards=''.join(f'<a class="direction" href="research.html#{tr["id"]}"><h3>{self.pair(tr["name"])} <span>↗</span></h3><p>{self.pair(tr["intro"])}</p><p class="project-label">{self.pair(tr["project"])}</p></a>' for tr in TRACKS)
        directions=f'<section class="wrap section"><h2>{self.t("研究方向","Research areas")}</h2><div class="cards">{cards}</div></section>'
        spot=[]
        for tr in TRACKS:
            k=tr['works'][0]
            spot.append(f'<article><h3>{link("research.html#work-"+k,self.pair(WORKS[k][0])+" ↗")}</h3><p>{self.pair(WORKS[k][1])}</p></article>')
        typical=f'<section class="tint"><div class="wrap section"><h2>{self.t("典型论文","Research highlights")}</h2><div class="highlights">{"".join(spot)}</div></div></section>'
        typical=typical.replace(self.t('典型论文','Research highlights'),self.t('代表性论文','Selected publications'))
        self.shell('index',self.name,hero+self.experiences()+directions+typical)
    def research(self):
        navigation=''.join(link('#'+tr['id'],self.pair(tr['name'])) for tr in TRACKS)
        body=f'<div class="wrap section page-top"><h1>{self.t("研究","Research")}</h1><div class="jump">{navigation}</div></div>'
        sections=[]
        for tr in TRACKS:
            k=tr['figure']
            figlink=self.assets+f'figure-{k}.webp'
            caption=self.pair(tr['fig'])
            fig=f'<figure class="paper-figure"><a href="{figlink}" aria-label="{self.t("放大论文插图","Enlarge figure")}"><img src="{figlink}" alt="{caption}" loading="lazy"></a><figcaption>{caption}</figcaption></figure>'
            left=f'<div><h2>{self.pair(tr["name"])}</h2><p class="intro">{self.pair(tr["intro"])}</p><p class="keywords"><b>{self.t("研究关键词：","Keywords: ")}</b>{self.pair(tr["keywords"])}</p><p class="project-label">{self.pair(tr["project"])}</p></div>'
            examples=[]
            for key in tr['works']:
                title,summary=WORKS[key]
                examples.append(f'<article class="study" id="work-{key}"><div><h3>{self.pair(title)}</h3><p>{self.pair(summary)}</p></div>{self.reference(key)}</article>')
            sections.append(f'<section class="track wrap" id="{tr["id"]}"><div class="track-head">{left}{fig}</div><h3 class="section-label">{self.t("代表工作","Selected studies")}</h3>{"".join(examples)}</section>')
        self.shell('research',self.nav['research'],body+''.join(sections))
    def publications(self):
        by_year=defaultdict(list)
        for key,p in PAPERS.items():
            by_year[p['year']].append(key)
        body=f'<section class="wrap section page-top"><h1>{self.t("论文成果","Publications")}</h1>{link(SCHOLAR,"Google Scholar ↗","more")}</section>'
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
                display_name='  '.join(s['name']) if len(s['name'])==2 else s['name']
                display=display_name if not self.i else f'{s["roman"]} <span lang="zh-CN">{display_name}</span>'
                topics = [s['topic']] + ([s['topic_extra']] if s.get('topic_extra') else [])
                topic_text = '；'.join(escape(self.pair(topic)) for topic in topics) if not self.i else '; '.join(escape(self.pair(topic)) for topic in topics)
                cotutor = ''
                if s.get('coadvisor'):
                    mode=s.get('coadvisor_mode','协同')
                    verb='Assisted by' if mode=='协助' else 'Co-supervised by'
                    cotutor=f'<span class="coadvisor">{self.t("（"+mode, " ("+verb+" ")}{escape(self.pair(s["coadvisor"]))}{self.t("指导）", ")")}</span>'
                entries.append(
                    f'<li class="student" data-name="{escape(s["name"], quote=True)}" '
                    f'data-degree="{s["degree"]}" data-year="{year}"><div class="student-heading">'
                    f'<b>{display}</b></div>'
                    f'<div class="student-topics">{topic_text}{cotutor}</div></li>')
            rows+=f'<div class="cohort"><h4>{year}</h4><ul>{"".join(entries)}</ul></div>'
        return rows

    def alumni_table(self,students):
        entries=[]
        for student in sorted(students,key=lambda s:(s.get('end','9999'),s['name'])):
            graduation=student.get('end','')
            year=graduation[:4] if graduation else self.t('未注明','Not listed')
            display_name='  '.join(student['name']) if len(student['name'])==2 else student['name']
            if self.i:
                name=f'{student["roman"]} <span lang="zh-CN">{display_name}</span>'
            else:
                name=display_name
            topics=[student['topic']]+([student['topic_extra']] if student.get('topic_extra') else [])
            topic_text='；'.join(escape(self.pair(topic)) for topic in topics) if not self.i else '; '.join(escape(self.pair(topic)) for topic in topics)
            cotutor=''
            if student.get('coadvisor'):
                mode=student.get('coadvisor_mode','协同')
                verb='Assisted by' if mode=='协助' else 'Co-supervised by'
                cotutor=f'<span class="coadvisor">{self.t("（"+mode, " ("+verb+" ")}{escape(self.pair(student["coadvisor"]))}{self.t("指导）", ")")}</span>'
            entries.append(f'<tr class="student alumnus" data-name="{escape(student["name"],quote=True)}" data-degree="M" data-year="{year}"><td>{year}</td><td>{name}</td><td>{topic_text}{cotutor}</td></tr>')
        return (f'<div class="table-scroll"><table class="alumni-table"><thead><tr>'
                f'<th scope="col">{self.t("毕业时间","Graduation year")}</th>'
                f'<th scope="col">{self.t("姓名","Name")}</th>'
                f'<th scope="col">{self.t("研究内容","Research")}</th>'
                f'</tr></thead><tbody>{"".join(entries)}</tbody></table></div>')
    def people(self):
        degrees=[s for s in STUDENTS if s['degree']=='M']
        doctorate=[s for s in STUDENTS if s['degree']=='D' and not s.get('end')]
        current=self.roster([s for s in degrees if not s.get('end') and s.get('status') != 'graduated'])
        alumni=self.alumni_table([s for s in degrees if s.get('end') or s.get('status') == 'graduated'])
        doctoral=self.roster(doctorate)
        undergrad=self.roster([s for s in STUDENTS if s['degree']=='B'])
        person=self.t('刘欣','Xin Liu')
        header=f'<section class="wrap section page-top"><h1>{self.t("指导学生","Students")}</h1></section>'
        def heading(title,en): return f'<h2>{self.t(title,en)}</h2>'
        body=f'<section class="wrap team-section doctoral-section">{heading("博士研究生","Doctoral students")}{doctoral}</section>'
        body+=f'<section class="wrap team-section current-section">{heading("硕士研究生","Master’s students")}{current}</section>'
        body+=f'<section class="wrap team-section alumni-section">{heading("课题组毕业生","Lab alumni")}{alumni}</section>'
        body+=f'<section class="wrap team-section undergraduate-section"><details><summary>{self.t("本科毕业设计","Undergraduate thesis projects")}</summary>{undergrad}</details></section>'
        dest=''.join(f'<div><h3>{self.pair(group)}</h3><p>{self.pair(names)}</p></div>' for group,names in DESTINATIONS)
        body+=f'<section class="tint"><div class="wrap section">{heading("毕业生去向","Alumni destinations")}<div class="destinations">{dest}</div></div></section>'
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
