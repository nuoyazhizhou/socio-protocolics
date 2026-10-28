# -*- coding: utf-8 -*-
"""
Automated Verification Gate for Socio-Protocolics v11.2
Validates:
1. Selected structural and textual markers across whitepaper, cheatsheet, and AGENTS.md; the internal edition is opt-in.
2. Orthogonal Axiomatic Hierarchy:
   - 3 First-Order Postulates (P1-P3) with non-zero impedance and Anti-Happy Path.
   - P1 tautology prevention (no duplicate debt formula in P1).
   - 6 Core Proposition Groups (I to VI).
   - 19 consecutive RFCs, each with an independent body section and role/conditions.
   - Six groups index 18 entries; the cross-group tooling spec is in chapter 8.
   - Version-qualified redirects preserve two retired, nonnumbered materials.
   - Section 1.6 Academic Cross-Radar & Meta-Compiler.
3. Selected Socio-Radar reference behaviours and illustrative arithmetic:
   - SDI normalization bounded in [0, 1] (opposite vectors -> 1.0, not 2.0).
   - SIR decoupling (zero distance + 100% rejection -> 0.50, not shielded to 0).
   - Research review flags, local/global boundaries, and PBR/PNR thresholds.
   - Complete hypothetical inputs, missingness and research-only metadata.
4. Selected textual regression guards and scope markers; no citation fact-check or empirical validation.
"""

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from whitepaper_blocks import check_document_blocks

try:
    import numpy as np
except ImportError:
    sys.stderr.write("Missing NumPy. Install with: python -m pip install -r tools/requirements.txt\n")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]

ACTIVE_RFC_IDS = {f'{i:03}' for i in range(1, 20)}
GROUP_RFC_IDS = [
    ['001', '002', '003'], ['004', '005', '006', '007'],
    ['008', '009', '010'], ['011', '012', '013', '014', '015'],
    ['016'], ['017', '018'],
]
CROSS_GROUP_RFC_IDS = ['019']
CATALOG_ORDER = [item for group in GROUP_RFC_IDS for item in group] + CROSS_GROUP_RFC_IDS
LEGACY_V11_1_DESTINATIONS = {
    f'{i:03}': ('research-process-pattern' if i == 6 else
                'application-policy-expectations' if i == 10 else
                f'{i - (i > 6) - (i > 10):03}')
    for i in range(1,22)
}
V11_0_TO_V11_1 = dict(zip(
    [f'{i:03}' for i in range(1,23)],
    ['001','002','004','005','008','006','009','010','013','014','011',
     '015','016','005','017','007','012','018','003','021','019','020']))
LEGACY_TO_CURRENT = {old: LEGACY_V11_1_DESTINATIONS[mid] for old, mid in V11_0_TO_V11_1.items()}
RETIRED_SECTIONS = {'research-process-pattern': '3.8', 'application-policy-expectations': '4.4'}
RFC_SECTIONS = dict(zip(CATALOG_ORDER,
    ['2.1','2.2','2.3','3.1','3.2','3.3','3.4','4.1','4.2','4.3',
     '5.1','5.2','5.3','5.4','5.5','6.1','7.1','7.2','8.1']))


def check_rfc_catalog(text, *, cheatsheet=False):
    """Check real body coverage and continuous numbering, not scientific validity."""
    errors = []
    if cheatsheet:
        entries = re.findall(r'^\*\s+\*\*【[^\n]*?SP-RFC-(\d{3})', text, re.M)
        catalog = text.split('## 二、', 1)[-1].split('\n## 三、', 1)[0]
        groups = re.split(r'^### [1-7]\. ', catalog, flags=re.M)[1:8]
        actual = [re.findall(r'^\*\s+\*\*【[^\n]*?SP-RFC-(\d{3})', g, re.M) for g in groups]
        if actual != GROUP_RFC_IDS + [CROSS_GROUP_RFC_IDS]:
            errors.append('CheatSheet group order/membership mismatch')
        if '19 Active SP-RFC Entries' not in text:
            errors.append('19 active RFC header missing')
        for material in RETIRED_SECTIONS:
            if '#'+material not in text:
                errors.append('CheatSheet nonnumbered material link missing: '+material)
        if r'\sum_{k=1}^{K}\text{Cost}_k' not in text or '各分支等成本时才简化' not in text:
            errors.append('CheatSheet general budget/equal-cost condition missing')
    else:
        errors.extend(check_document_blocks(text.encode('utf-8')))
        entries = re.findall(r'^\| \*\*【[^\n]*?SP-RFC-(\d{3})\*\*', text, re.M)
        anchors = re.findall(r'<a id="sp-rfc-(\d{3})"></a>', text)
        if Counter(anchors) != Counter(ACTIVE_RFC_IDS):
            errors.append('canonical RFC anchors must be unique 001-019')
        for version, destinations in [('11-0', LEGACY_TO_CURRENT), ('11-1', LEGACY_V11_1_DESTINATIONS)]:
            pattern=r'<a id="legacy-v'+version+r'-rfc-(\d{3})"></a>'
            legacy=re.findall(pattern,text)
            if Counter(legacy)!=Counter(list(destinations)):
                errors.append('version-qualified legacy anchors incomplete/duplicate: v'+version)
            for alias in re.finditer(pattern,text):
                target=re.search(r'^### (\d+\.\d+) ([^\n]+)',text[alias.end():],re.M)
                dest=destinations.get(alias[1])
                if target is None:
                    errors.append('legacy target has no body: '+alias[1]); continue
                if dest in RETIRED_SECTIONS:
                    valid=target[1]==RETIRED_SECTIONS[dest] and 'SP-RFC-' not in target[2]
                else:
                    valid=bool(dest and target[2].startswith('SP-RFC-'+dest+'｜'))
                if not valid:errors.append('version-qualified legacy target mismatch: v'+version+'/'+alias[1])
        for anchor, section in RETIRED_SECTIONS.items():
            marker='<a id="'+anchor+'"></a>'
            if text.count(marker)!=1:
                errors.append('nonnumbered material anchor missing/duplicate: '+anchor); continue
            rest=text.split(marker,1)[1]
            start=re.search(r'^### '+re.escape(section)+r' ([^\n]+)',rest,re.M)
            if start is None:
                errors.append('nonnumbered material is in wrong section: '+anchor); continue
            following=rest[start.end():];stop=re.search(r'^#{2,3} ',following,re.M)
            block=following[:stop.start()] if stop else following
            if '非编号' not in block or len(block.strip())<150:
                errors.append('nonnumbered material body/role missing: '+anchor)
        matches=list(re.finditer(r'^### (\d+\.\d+) SP-RFC-(\d{3})｜[^\n]+',text,re.M))
        ids=[m[2] for m in matches]
        if ids != CATALOG_ORDER:
            errors.append('independent body RFC sections must cover 001-019 in order')
        for m in matches:
            if RFC_SECTIONS.get(m[2]) != m[1]:
                errors.append('RFC section/chapter mismatch: '+m[2])
            rest=text[m.end():]
            stop=re.search(r'^#{2,3} ',rest,re.M)
            block=rest[:stop.start()] if stop else rest
            for marker in ['**主张身份**','**依赖与附加条件**','【规范条文 / Normative Spec】']:
                if marker not in block:
                    errors.append('RFC '+m[2]+': missing body field '+marker)
            proof = {'008':'条件推导 III-1', '013':'条件推导 IV-1'}.get(m[2])
            if proof and proof not in block:
                errors.append('RFC '+m[2]+': local proof is missing or in the wrong section')
            norm=block.split('【规范条文 / Normative Spec】',1)[-1]
            if len(norm.strip())<80:
                errors.append('RFC '+m[2]+': normative body missing or too short')
            if m[2]=='017':
                for marker in ['不由上述核算定义单独推出','风险假说A','风险假说B','认识论自约束','工程实施建议','沙盒试验用于取得证据']:
                    if marker not in block:errors.append('RFC-017 J01 role boundary missing: '+marker)
                if re.search(r'\*\*推论[一二三四]',block):
                    errors.append('RFC-017 accounting must not promote risks/guidelines to derived laws')
            if m[2]=='016':
                if '无连接情绪广播无法沉淀出稳定组织状态机' in block or '该研究的测量对象是消息扩散' not in block:
                    errors.append('RFC-016 J02 message/organization evidence boundary missing')
        if '§5.3 的 $Q_i(a_i,a_{-i})$' not in text:
            errors.append('J04 game utility scope must point to section 5.3')
        directory=text.split('### 19项RFC正文入口',1)[-1].split('旧版编号',1)[0]
        directory_ids=re.findall(r'^\| SP-RFC-(\d{3}) \|',directory,re.M)
        if directory_ids!=CATALOG_ORDER:
            errors.append('RFC directory must link every body section once')
        for row in directory.splitlines():
            m=re.match(r'^\| SP-RFC-(\d{3}) \| ([^|]+) \| \[([\d.]+) [^\]]+\]\(#sp-rfc-(\d{3})\)',row)
            if not m:continue
            expected=next((g for g, ids in zip(['I','II','III','IV','V','VI'],GROUP_RFC_IDS) if m[1] in ids),'跨组/第八章')
            if m[2].strip()!=expected or m[3]!=RFC_SECTIONS.get(m[1]) or m[4]!=m[1]:
                errors.append('RFC directory role/section/link mismatch: '+m[1])
        chapter_numbers=re.findall(r'^## 第([一二三四五六七八]+)章：',text,re.M)
        if chapter_numbers!=list('一二三四五六七八'):
            errors.append('chapter numbering must be consecutive 1-8')
        headings=re.findall(r'^### (\d+\.\d+) ',text,re.M)
        if headings != sorted(set(headings),key=lambda x:tuple(map(int,x.split('.')))):
            errors.append('section numbering must be unique and increasing')
        seen = set()
        siblings = {}
        for heading in re.finditer(r'^#{3,4} (\d+(?:\.\d+)+) ',text,re.M):
            number=heading[1];parent,child=number.rsplit('.',1)
            if '.' in parent and parent not in seen:
                errors.append('subsection parent is missing: '+number)
            if int(child) != siblings.get(parent,0)+1:
                errors.append('section/subsection sequence skips or repeats: '+number)
            siblings[parent]=int(child);seen.add(number)
        for marker in ['未满足本条条件的一般制度僵化问题不被自动吸收',
                       '候选过程模式', '不是VI组演绎定理']:
            if marker not in text:errors.append('scope/role marker missing: '+marker)
    if Counter(entries)!=Counter(ACTIVE_RFC_IDS):
        errors.append('active RFC set/count mismatch: expected consecutive 001-019')
    if entries!=CATALOG_ORDER:
        errors.append('active RFC navigation order mismatch')
    if not cheatsheet:
        errors.extend(check_evidence_cards(text))
    return errors

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def test_reference_engine(md_text, label):
    """Execute the selected edition; expected boundaries do not duplicate its classifier."""
    errors = []
    cases = 0

    def check(ok, name):
        nonlocal cases
        cases += 1
        if not ok:
            errors.append(label + ': ' + name)

    def rejects(call, name):
        try:
            call()
        except ValueError:
            check(True, name)
        else:
            check(False, name)

    blocks = re.findall(r'```python\s*\n(.*?)```', md_text, re.S)
    source = next(b for b in blocks if 'class SocioRadarEngine:' in b)
    ns = {'__name__': '_socio_gate_reference_engine'}
    exec(compile(source, label, 'exec'), ns)
    Engine = ns['SocioRadarEngine']
    unit = np.array([[1., 0.]])
    engine = Engine(['x'], ['pad'])
    sdi, accel = engine.compute_semantic_drift(unit, unit)
    check(np.isclose(sdi, 0.) and accel is None, 'SDI identical and warm-up missingness')
    sdi, accel = engine.compute_semantic_drift(unit, -unit)
    check(np.isclose(sdi, 1.) and accel is None, 'SDI opposite normalization')
    check(np.isclose(engine.compute_syscall_impedance(unit, unit, 1.), .5),
          'SIR must not mask full rejection at zero distance')
    pbr, pnr = engine.compute_padding_bloat(['pad', 'word'])
    check(np.isclose(pbr, .5) and np.isclose(pnr, .5 / (.5 + 1e-6)),
          'PBR/PNR entropy and epsilon contract')
    pbr, pnr = engine.compute_padding_bloat(['clean-a', 'clean-b'])
    check(pbr == 0. and np.isclose(pnr, 1e6),
          'zero padding and maximal entropy reaches the finite unnormalized PNR bound')
    pbr, pnr = engine.compute_padding_bloat(['clean-a', 'clean-a'])
    check(pbr == 0. and pnr == 0.,
          'zero padding with zero entropy is zero PNR, not automatically the upper bound')
    rejects(lambda: engine.compute_padding_bloat([]), 'empty text is missing, not zero risk')
    rejects(lambda: engine.compute_semantic_drift(unit, np.zeros_like(unit)),
            'zero-norm vector is missing, not zero drift')

    def evaluate(**changes):
        values = dict(sdi=0., a_drift=None, pbr=0., pnr=1., sir=0., mpm=0., timestamp=0.)
        values.update(changes)
        return engine.evaluate_research_flags(**values)

    high = evaluate(pbr=.9)
    check(high.research_zone.startswith('RED'), 'high PBR review overrides composite score')
    check(evaluate(pbr=.66, pnr=.19).research_zone.startswith('YELLOW'),
          'yellow padding requires low PNR')
    check(evaluate(pbr=.66, pnr=.21).research_zone.startswith('GREEN'),
          'high PNR excludes padding-only yellow')
    check(not evaluate(pbr=.85, pnr=.19).research_zone.startswith('RED'),
          'PBR red threshold is strict')
    check(not evaluate().drift_acceleration_ready, 'unknown acceleration remains unknown')
    rejects(lambda: evaluate(sdi=float('nan')), 'missing numeric input cannot produce a score')
    rejects(lambda: evaluate(word_reviews=('x', 'x')), 'duplicate words cannot inflate hit ratio')
    rejects(lambda: evaluate(word_reviews=('outside',)), 'review words must belong to bound lexicon')

    for size, hits, expected in [(100, 1, 'GREEN'), (20, 3, 'GREEN'), (20, 4, 'RED')]:
        words = [f'w{i}' for i in range(size)]
        observed = Engine(words, [])
        baseline = np.tile([1., 0.], (size, 1))
        observed.compute_semantic_drift(baseline, baseline)
        observed.compute_semantic_drift(baseline, baseline)
        current = baseline.copy()
        current[:hits] *= -1
        mean, acceleration = observed.compute_semantic_drift(baseline, current)
        snapshot = observed.evaluate_research_flags(mean, acceleration, 0., 1., 0., 0., 2.,
                                                    word_reviews=observed.latest_word_reviews)
        check(snapshot.local_lexical_alert and len(snapshot.semantic_review_words) == hits
              and snapshot.research_zone.startswith(expected),
              f'local/global separation K={size}, hits={hits}, expected {expected}')
        fresh = observed.evaluate_research_flags(0., None, 0., 1., 0., 0., 3.)
        check(not fresh.local_lexical_alert and fresh.research_zone.startswith('GREEN'),
              f'no implicit reuse of prior word flags K={size}, hits={hits}')

    pre = evaluate(sdi=.55, pbr=.75, pnr=0., sir=.85, mpm=.65)
    post = evaluate(sdi=.10, pbr=.15, pnr=1., sir=.20, mpm=.30)
    check(np.isclose(pre.research_score, .2738850187392208) and pre.research_zone.startswith('RED'),
          'complete hypothetical pre-inputs yield 0.27/red')
    check(np.isclose(post.research_score, .8337581892923576) and post.research_zone.startswith('GREEN'),
          'complete hypothetical post-inputs yield 0.83/green')
    check(evaluate().missing_metadata == ('model_version', 'measurement_profile_id',
          'SDI_source', 'PBR_source', 'SIR_source', 'MPM_source'),
          'missing metadata remains explicit')
    sources = tuple((name, 'fixture:' + name) for name in ('SDI', 'PBR', 'SIR', 'MPM'))
    declared = evaluate(model_version='fixture-model-v1', measurement_profile_id='fixture-profile-v1',
                        input_provenance=sources)
    check(not declared.missing_metadata and declared.input_provenance == sources
          and declared.research_only and declared.calibration_status == 'uncalibrated'
          and not declared.provenance_verified,
          'declared metadata is preserved without automatic verification or calibration')
    rejects(lambda: evaluate(input_provenance=(('SDI', 'a'), ('SDI', 'b'))),
            'duplicate provenance cannot hide ambiguous sources')
    legacy = engine.evaluate_system_health(0., None, 0., 1., 0., 0., 0.)
    check(legacy == evaluate(), 'legacy method delegates to identical research-only output')
    try:
        declared.research_only = False
    except AttributeError:
        check(True, 'snapshot status is read-only')
    else:
        check(False, 'snapshot status is read-only')
    return errors, cases


def check_evidence_cards(text):
    """Check the declared traceability contract, not truth or empirical adequacy."""
    errors = []
    anchors = re.findall(r'<a id="rfc-evidence-(\d{3})"></a>', text)
    if Counter(anchors) != Counter(ACTIVE_RFC_IDS):
        errors.append('evidence cards must cover unique 001-019')
    bodies = re.findall(r'^### [\d.]+ SP-RFC-(\d{3})｜([^\n]+)\n\n'
                        r'\*\*主张身份\*\*：([^\n]+)', text, re.M)
    for ident, title, role in bodies:
        marker = '<a id="rfc-evidence-' + ident + '"></a>'
        if marker not in text:
            continue
        card = text.split(marker, 1)[1].split('<a id="rfc-evidence-', 1)[0]
        if '#### G' + ident + '｜' + title.strip() not in card:
            errors.append('evidence card title mismatch: ' + ident)
        identity = '**正文与身份**：[SP-RFC-' + ident + '](#sp-rfc-' + ident + ')；' + role.strip().rstrip('。') + '。'
        if identity not in card:
            errors.append('evidence card identity mismatch: ' + ident)
        for field_name in ['基础与附加条件', '困境与反事实', '必要性', '充分性与边界',
                           '替代与最小性', '证据与拒绝条件', '当前状态']:
            if '**' + field_name + '**：' not in card:
                errors.append('evidence card missing ' + field_name + ': ' + ident)
        basis = next((line for line in card.splitlines() if line.startswith('- **基础与附加条件**：')), '')
        if not re.search(r'O[1-5]', basis) or not re.search(r'P[123]', basis):
            errors.append('evidence card P/O declaration missing: ' + ident)
        body = re.split(r'^### ', text.split('SP-RFC-' + ident + '｜', 1)[1], maxsplit=1, flags=re.M)[0]
        if '[G' + ident + '](#rfc-evidence-' + ident + ')' not in body:
            errors.append('RFC body evidence card link missing: ' + ident)
    directory = text.split('### 19项RFC正文入口', 1)[-1].split('旧版编号', 1)[0]
    rows = re.findall(r'^\| SP-RFC-(\d{3}) \| [^|]+ \| \[[\d.]+ ([^\]]+)\]'
                      r'\(#sp-rfc-\d{3}\) \| ([^|\n]+) \|', directory, re.M)
    expected = {i: (title.strip(), role.strip().rstrip('。')) for i, title, role in bodies}
    for ident, title, role in rows:
        if expected.get(ident) != (title.strip(), role.strip().rstrip('。')):
            errors.append('directory title/identity mismatch: ' + ident)
    return errors


def test_current_text_guards(pub, raw, cs, ag):
    """Finite structural/text checks, not automated semantic or scientific proof."""
    import re
    from collections import Counter
    errors = []
    def require(ok, label):
        if not ok:
            errors.append(label)
    docs = [('SSOT', pub), ('CheatSheet', cs), ('AGENTS', ag)]
    main_docs = [('SSOT', pub)]
    if raw is not None:
        docs.append(('Internal', raw))
        main_docs.append(('Internal', raw))
    for name, text in docs:
        require('v11.2' in text, name + ': version marker missing')
        for group_title in ['信道容量与语义边界', '中介寄生与兼容层衰减', '跨期终局性与预期信誉',
                            '特权环隔离与脑裂传染', '传输拓扑与任务反馈', '技术债核算与演化筛选']:
            require(group_title in text, name + ': renamed proposition group missing: ' + group_title)
        require('六组核心命题' in text, name + ': six core proposition group label missing')
        for old_name in ['六大核心基本定律', '六大定律', '技术债守恒与演化赛马律', '传输拓扑与动员相变']:
            require(old_name not in text, name + ': stale group label: ' + old_name)

        ids = re.findall(r'^\* \*\*SP-POSTULATE-([123])', text, re.M)
        require(Counter(ids) == Counter('123'), name + ': 3 unique primary Postulate definitions required')
        require(r'\mu_{i,t}(A)=\Pr_i' in text, name + ': O3 subjective probability definition missing')
        require('非实测' in text or '不将其解释为已测得' in text, name + ': exception slogan scope missing')
        require('社会' in text and '桥接' in text, name + ': physical/social bridge distinction missing')
        require('预测增益' in text, name + ': comparative gain criterion missing')
        for stale in ['主观概率分布 $\\mathbb{E}', '严格逻辑演绎推导', '严格数学与博弈推导',
                      '新范式必须跨越特权环合入内核', '唯靠边缘赛马PDCA幸存', '遭遇真实世界 99% 异常',
                      '唯一一个真正把“数万亿', '无熵受控世界', '永远由其底层信息协议',
                      '在香农公式中表现为单纯增加白噪声', '必须先消耗 70%',
                      '新协议从来不是全知架构师', '反例判定公理', '国家级系统调用强制推行']:
            require(stale not in text, name + ': stale claim: ' + stale)
    o4 = next((line for line in ag.splitlines() if line.startswith('* **O4:')), '')
    o5 = next((line for line in ag.splitlines() if line.startswith('* **O5:')), '')
    require(all(term in o4 for term in ['终端 Agent', '可行替代机制', '排他控制', '非生产性租金']), 'AGENTS: selected O4 boundary markers missing')
    require(all(term in o5 for term in ['可行域', '不可逆时间', '规律本身']), 'AGENTS: selected O5 boundary markers missing')
    require('历史案例统一注明' not in ag, 'AGENTS: sourced history must not all be labelled simulation')
    require('python tools/verify_all.py' in ag and '--internal' in ag, 'AGENTS: portable/public and optional internal commands missing')
    require('SOCIO_PROTOCOLICS_VERIFY_ALL' not in ag, 'AGENTS: stale external gate environment dependency')
    require('001至019连续编号' in ag and '新旧同号' in ag,
            'AGENTS: current version/continuous-numbering rules missing')
    agent_navigation = re.findall(r'^  [1-6]\. (.+)$', ag, re.M)
    agent_groups = [re.findall(r'\d{3}', line.split('；历史', 1)[0]) for line in agent_navigation]
    require(agent_groups == GROUP_RFC_IDS, 'AGENTS: group navigation disagrees with active catalog')
    for name, text in main_docs:
        errors.extend(name + ': ' + err for err in check_rfc_catalog(text))
        law_rows = [l for l in text.splitlines() if l.startswith('| **第') and 'Proposition Group)' in l]
        require(len(law_rows)==6, name + ': 6 law matrix rows required')
        for i, row in enumerate(law_rows):
            require(len(row.split(' | '))==6 and row.endswith(' |'), name + ': law table cell structure')
            require(re.findall(r'\d{3}', row.split(' | ')[1])==GROUP_RFC_IDS[i], name + ': group RFC navigation mismatch')
        require('关联守则: RFC-007' in text and '跨组工具/研究规范' in text and '### 8.1 SP-RFC-019' in text,
                name + ': normative/application roles must not be treated as derived theorems')
        for marker in ['候选社会模型', '不保证趋近 1', '需要国家授权的制度化分支', '不代表从三条公设已完成全部严格证明']:
            require(marker in text, name + ': regression scope marker missing: ' + marker)
        # Every row reporting a numeric SHI in the simulation table needs four inputs.
        if '### 8.6' not in text:
            errors.append(name + ': simulation section missing')
            continue
        sim = re.split(r'^## ', text.split('### 8.6',1)[1], maxsplit=1, flags=re.M)[0]
        rows=[l for l in sim.splitlines() if l.startswith('|') and len(l.split(' | '))==4
              and re.search(r'[+-]?(?:\d+(?:\.\d+)?|\.\d+)',l.split(' | ')[2])]
        require(bool(rows), name + ': no numeric SHI simulation rows checked')
        for row in rows:
            inputs=row.split(' | ')[1]
            phases=inputs.split('<br>') if '改革前' in inputs and '改革后' in inputs else [inputs]
            for phase in phases:
                for inp in ['SDI', 'PBR', 'SIR', 'MPM']:
                    require(re.search(r'\\text\{'+inp+r'\}\s*=\s*(?:0(?:\.\d+)?|1(?:\.0+)?)(?![\d.])',phase) is not None,
                            name + ': numeric SHI phase lacks ' + inp)
    require('缺 PBR、SIR' in pub and '输入不全，未计算 SHI' in pub, 'SSOT: incomplete DEI inputs must not report numeric SHI')
    errors.extend('CheatSheet: ' + err for err in check_rfc_catalog(cs, cheatsheet=True))
    expected = {ident: (title.strip(), role.strip().rstrip('。'))
                for ident, title, role in re.findall(
                    r'^### [\d.]+ SP-RFC-(\d{3})｜([^\n]+)\n\n\*\*主张身份\*\*：([^\n]+)', pub, re.M)}
    for role, ident, title in re.findall(r'^\* \*\*【([^】]+)】SP-RFC-(\d{3})【([^】]+)】', cs, re.M):
        require(expected.get(ident) == (title.strip(), role.strip()),
                'CheatSheet: body title/identity mismatch: ' + ident)

    # Shared normative sections are checked only when an internal edition was supplied.
    for a,b in [('### 1.5','### 1.6'),('### 1.6','### 1.7')]:
        def section(t):
            if a not in t or b not in t[t.find(a)+len(a):]:
                raise ValueError('shared section delimiter missing: ' + a + ' / ' + b)
            return t[t.index(a):t.index(b,t.index(a)+len(a))].strip()
        if raw is not None:
            require(section(pub)==section(raw), 'SSOT/Internal: selected shared section mismatch: '+a)
    return errors

def audit(internal_path=None):
    errors = []
    documents = {}
    paths = {
        'cs': ROOT / '核心概念速查手册_CheatSheet.md',
        'pub': ROOT / '社会系统协议学白皮书.md',
        'ag': ROOT / 'AGENTS.md',
    }
    if internal_path is not None:
        paths['raw'] = internal_path
    for key, path in paths.items():
        try:
            documents[key] = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'Cannot read {key}: {path}: {exc}')
    if errors:
        for error in errors:
            print('FAIL: ' + error)
        return 1
    pub, cs, ag = (documents[key] for key in ('pub', 'cs', 'ag'))
    raw = documents.get('raw')

    reference_cases = 0

    # Check CheatSheet
    if 'v11.2' not in cs:
        errors.append('CheatSheet version missing v11.2')
    if '三大公理' in cs[cs.find('## 零、'):cs.find('## 一、')]:
        errors.append('CheatSheet section 0 contains stale "三大公理"')
    if '19 Active SP-RFC Entries' not in cs:
        errors.append('CheatSheet missing 19 active RFC header')
    if '三大正交第一性公设' not in cs or 'SP-POSTULATE-1' not in cs or 'SP-POSTULATE-3' not in cs:
        errors.append('CheatSheet section 0.1 missing 3 Postulates')
    if '六组核心命题' not in cs or '第一组核心命题' not in cs or '第六组核心命题' not in cs:
        errors.append('CheatSheet section 0.1 missing 6 Core Proposition Groups')
    if 'SP-RFC-017' not in cs or 'SP-RFC-018' not in cs:
        errors.append('CheatSheet missing migration accounting or trial selection entries')
    if '未校准研究指标声明' not in cs:
        errors.append('CheatSheet missing uncalibrated indicator disclaimer in section 4.2')

    # Check Public Whitepaper
    if 'v11.2' not in pub:
        errors.append('Public whitepaper version missing v11.2')
    if '### 1.1 白话文运动宣言' not in pub:
        errors.append('Public whitepaper missing § 0.0')
    if '三大正交第一性公设' not in pub[pub.find('### 1.1'):pub.find('### 1.2')]:
        errors.append('Public whitepaper § 0.0 missing "三大正交第一性公设"')
    if '### 1.4 碳硅本体边界与内生博弈层' not in pub:
        errors.append('Public whitepaper missing § 0.3')
    if '### 1.5 协议学核心对象模型与公理体系' not in pub:
        errors.append('Public whitepaper missing § 0.4')
    if '三大第一性公设' not in pub:
        errors.append('Public whitepaper missing 3 Postulates header')
    if '三层正交金字塔' not in pub:
        errors.append('Public whitepaper missing 3-tier pyramid architecture in § 0.4')
    if '### 1.6 跨学科学术雷达对齐与“计算系统工程”大一统元编译器' not in pub:
        errors.append('Public whitepaper missing § 0.5 Academic Cross-Radar')
    if '第一组核心命题：信道容量与语义边界' not in pub or '第六组核心命题：技术债核算与演化筛选' not in pub:
        errors.append('Public whitepaper missing 6 Core Proposition Groups')
    if 'Bazaar Maintainer' not in pub:
        errors.append('Public whitepaper missing Bazaar Maintainer concept')
    if '### 7.2 SP-RFC-018' not in pub:
        errors.append('Public whitepaper missing trial selection §7.2 / RFC-018')
    if '【可证伪边界与反例对消判定 / Falsifiability Boundary】' not in pub:
        errors.append('Public whitepaper missing Falsifiability Boundary in § 1.3')
    if '### 7.1 SP-RFC-017' not in pub:
        errors.append('Public whitepaper missing migration accounting §7.1 / RFC-017')
    if '【方法论声明与未来实证研究议程 / Methodological Disclaimer & Empirical Research Agenda】' not in pub:
        errors.append('Public whitepaper missing Methodological Disclaimer in § 10.3')
    if 'gain_k: float = 5.0' not in pub:
        errors.append('Public whitepaper missing gain_k in SocioRadarEngine')
    if 'critical_review_trigger' not in pub:
        errors.append('Public whitepaper missing critical review trigger in SocioRadarEngine')
    if '### 8.5 经验测量协议与三大定量算子' not in pub:
        errors.append('Public whitepaper missing § 10.5')
    if '### 8.6 历史案例指标解释方法与模拟示例' not in pub:
        errors.append('Public whitepaper missing § 10.6')

    if raw is not None:
        # Check Internal Whitepaper
        if 'v11.2' not in raw:
            errors.append('Internal whitepaper version missing v11.2')
        if '三大正交第一性公设' not in raw[raw.find('### 1.1'):raw.find('### 1.2')]:
            errors.append('Internal whitepaper § 0.0 missing "三大正交第一性公设"')
        if '### 1.6 跨学科学术雷达对齐与“计算系统工程”大一统元编译器' not in raw:
            errors.append('Internal whitepaper missing § 0.5')
        if 'SP-RFC-018' not in raw:
            errors.append('Internal whitepaper missing trial selection RFC-018')
        if 'gain_k: float = 5.0' not in raw:
            errors.append('Internal whitepaper missing gain_k in SocioRadarEngine')
        if 'critical_review_trigger' not in raw:
            errors.append('Internal whitepaper missing critical review trigger in SocioRadarEngine')

    # Check the repository-level AGENTS.md.
    try:
        if 'v11.2' not in ag:
            errors.append('Dedicated AGENTS.md missing v11.2 update')
        if '三层正交金字塔' not in ag:
            errors.append('Dedicated AGENTS.md missing 3-tier pyramid red line')
        if '大一统元编译器' not in ag and '大一统' not in ag:
            errors.append('Dedicated AGENTS.md missing meta-compiler reference')
    except Exception as e:
        errors.append(f'Failed to check AGENTS.md: {e}')

    try:
        errors.extend(test_current_text_guards(pub, raw, cs, ag))
    except (ValueError, IndexError) as exc:
        errors.append('Text guard could not complete: ' + str(exc))

    # Execute only the actual reference block from each explicitly selected edition.
    engine_docs = [('SSOT', pub)]
    if raw is not None:
        engine_docs.append(('Internal', raw))
    for label, document in engine_docs:
        try:
            failures, count = test_reference_engine(document, label)
            errors.extend(failures)
            reference_cases += count
        except Exception as exc:
            errors.append(f'{label}: reference engine checks could not complete: {exc}')

    print('Mode: ' + ('public + explicit internal edition' if raw is not None else 'public only'))
    print(f'Documents read: {len(paths)}; expected per main edition: 8 chapters, 6 groups, 19 consecutive RFC body sections and 2 nonnumbered materials')
    print('Checks: 9 paired chapter/appendix blocks; versions/postulates; RFC catalog and evidence-card identities/fields; selected scope markers; simulation input completeness.')
    print(f'Reference engine checks executed: {reference_cases}; actual embedded code, including numeric, threshold, missingness, local/global and metadata boundaries.')
    print('AGENTS: selected O4/O5 definition boundaries; simulation distinction; portable gate commands.')
    if raw is None:
        print('NOT CHECKED: internal edition and public/internal shared-section equality (use --internal PATH).')
    else:
        print('Internal scope: same structural/engine checks; exact shared sections 1.5 and 1.6. Other edition differences are not compared.')
    print('LIMITS: no whole-text semantic proof, source fact-check, full code coverage, mathematical proof or empirical social validation.')
    if errors:
        print(f'AUDIT FAILED: {len(errors)} failure(s)')
        for error in errors:
            print('  - ' + error)
        return 1
    print('ALL LISTED CHECKS PASSED')
    return 0


def main():
    parser = argparse.ArgumentParser(description='Portable structural, textual and reference-code gate; not empirical validation.')
    parser.add_argument('--internal', type=Path, metavar='PATH', help='Opt-in local internal edition. Relative paths are resolved against repository root; missing files fail.')
    args = parser.parse_args()
    internal_path = args.internal
    if internal_path is not None and not internal_path.is_absolute():
        internal_path = ROOT / internal_path
    return audit(internal_path)


if __name__ == '__main__':
    raise SystemExit(main())
