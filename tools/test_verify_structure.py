"""Structural and missing-body regressions; no assertion of scientific validity."""
from pathlib import Path
import re
import unittest
import verify_all as gate

ROOT = Path(__file__).resolve().parents[1]


class StructureRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.main=(ROOT/'社会系统协议学白皮书.md').read_text(encoding='utf-8')
        cls.cheat=(ROOT/'核心概念速查手册_CheatSheet.md').read_text(encoding='utf-8')

    def reject(self,text):
        self.assertTrue(gate.check_rfc_catalog(text))

    def test_current_books(self):
        self.assertEqual([],gate.check_rfc_catalog(self.main))
        self.assertEqual([],gate.check_rfc_catalog(self.cheat,cheatsheet=True))

    def test_chapter_end_marker_cannot_disappear(self):
        errors = gate.check_rfc_catalog(self.main.replace('<!-- SP:END chapter-07 -->', '', 1))
        self.assertTrue(any('block boundaries' in error for error in errors))

    def test_chapter_boundary_pair_must_match(self):
        errors = gate.check_rfc_catalog(self.main.replace('<!-- SP:END chapter-07 -->', '<!-- SP:END chapter-08 -->', 1))
        self.assertTrue(any('block boundaries' in error for error in errors))

    def test_appendix_cannot_hide_missing_body(self):
        text=re.sub(r'^### 4\.2 SP-RFC-009｜.*?(?=^### 4\.3)', '',self.main,flags=re.M|re.S)
        self.reject(text)

    def test_heading_without_normative_body_is_rejected(self):
        start=self.main.index('### 2.1 SP-RFC-001｜')
        stop=self.main.index('### 2.2 SP-RFC-002｜',start)
        text=self.main[:start]+self.main[start:].split('\n',1)[0]+'\n\n'+self.main[stop:]
        self.reject(text)

    def test_duplicate_or_missing_active_id_is_rejected(self):
        self.reject(self.main.replace('SP-RFC-003**','SP-RFC-001**'))

    def test_obsolete_022_cannot_be_active(self):
        self.reject(self.main+'\n| **【有效条款】<br>SP-RFC-022** | wrongly active |\n')

    def test_legacy_target_cannot_change(self):
        alias='<a id="legacy-v11-0-rfc-014"></a>'
        text=self.main.replace(alias,'').replace('<a id="sp-rfc-004"></a>',alias+'\n<a id="sp-rfc-004"></a>')
        self.reject(text)

    def test_wrong_chapter_sequence_is_rejected(self):
        self.reject(self.main.replace('## 第三章：','## 第四章：',1))

    def test_body_cannot_use_wrong_section_number(self):
        self.reject(self.main.replace('### 5.3 SP-RFC-013｜','### 4.5 SP-RFC-013｜'))

    def test_directory_must_cover_every_body(self):
        self.reject(self.main.replace('| SP-RFC-013 | IV |','| SP-RFC-012 | IV |'))

    def test_missing_scope_boundary_is_rejected(self):
        self.reject(self.main.replace('未满足本条条件的一般制度僵化问题不被自动吸收',''))

    def test_static_game_proof_must_have_its_own_body(self):
        self.reject(self.main.replace('**条件推导 IV-1：','**证明位置丢失：',1))

    def test_subsection_sequence_cannot_skip(self):
        self.reject(self.main.replace('#### 6.1.2 UDP','#### 6.1.3 UDP',1))

    def test_cheat_groups_cannot_be_swapped(self):
        lines=self.cheat.splitlines()
        row=next(l for l in lines if l.startswith('*') and 'SP-RFC-003【' in l)
        lines.remove(row)
        pos=next(i for i,l in enumerate(lines) if l.startswith('*') and 'SP-RFC-016【' in l)
        lines.insert(pos+1,row)
        self.assertTrue(gate.check_rfc_catalog('\n'.join(lines),cheatsheet=True))

    def test_retired_material_body_cannot_disappear(self):
        text=re.sub(r'^### 3\.8 候选演化.*?(?=^## 第四章)', '',self.main,flags=re.M|re.S)
        self.reject(text)

    def test_v111_retired_id_cannot_redirect_to_current_same_number(self):
        alias='<a id="legacy-v11-1-rfc-006"></a>'
        text=self.main.replace(alias,'').replace('<a id="sp-rfc-006"></a>',alias+'\n<a id="sp-rfc-006"></a>')
        self.reject(text)

    def test_v111_alias_must_remain_unique(self):
        self.reject(self.main+'\n<a id="legacy-v11-1-rfc-021"></a>\n')

    def test_tooling_spec_cannot_be_catalogued_as_group_vi(self):
        self.reject(self.main.replace('| SP-RFC-019 | 跨组/第八章 |','| SP-RFC-019 | VI |'))

    def test_tooling_spec_must_stay_in_chapter_eight(self):
        self.reject(self.main.replace('### 8.1 SP-RFC-019｜','### 7.4 SP-RFC-019｜'))

    def test_budget_cache_cannot_drop_equal_cost_condition(self):
        text=self.cheat.replace('各分支等成本时才简化','总是简化')
        self.assertTrue(gate.check_rfc_catalog(text,cheatsheet=True))

    def test_accounting_must_not_label_risks_as_derived_laws(self):
        self.reject(self.main.replace('**风险假说A：','**推论一（重构死锁律）：',1))

    def test_message_study_cannot_be_used_as_organization_impossibility(self):
        self.reject(self.main.replace('该研究的测量对象是消息扩散','无连接情绪广播无法沉淀出稳定组织状态机',1))

    def test_game_utility_reference_cannot_drift(self):
        self.reject(self.main.replace('§5.3 的 $Q_i(a_i,a_{-i})$','§4.2 的 $Q_i(a_i,a_{-i})$'))

    def test_directory_section_label_must_match_body(self):
        self.reject(self.main.replace('| [8.1 AI工具控制','| [7.3 AI工具控制',1))

    def test_directory_title_must_match_body_exactly(self):
        self.reject(self.main.replace('[2.2 命名与共同识别]', '[2.2 命名的其他标题]', 1))

    def test_directory_compound_identity_cannot_be_flattened(self):
        self.reject(self.main.replace(
            '| [2.1 物理信道与语义解码](#sp-rfc-001) | 物理结果引用、条件模型与社会桥接 |',
            '| [2.1 物理信道与语义解码](#sp-rfc-001) | 普遍定律 |', 1))

    def test_evidence_card_cannot_disappear(self):
        self.reject(self.main.replace('<a id="rfc-evidence-003"></a>', '', 1))

    def test_evidence_card_identity_must_preserve_normative_role(self):
        self.reject(self.main.replace(
            '**正文与身份**：[SP-RFC-007](#sp-rfc-007)；跨组规范守则。',
            '**正文与身份**：[SP-RFC-007](#sp-rfc-007)；物理定律。', 1))

    def test_necessity_cannot_replace_sufficiency_field(self):
        self.reject(self.main.replace('- **充分性与边界**：', '- **必要性**：', 1))

    def test_body_card_link_is_required(self):
        self.reject(self.main.replace('**生成与证据卡**：[G001](#rfc-evidence-001)。', '', 1))

    def test_gate_detects_reintroduced_local_global_bug(self):
        mutated = self.main.replace(
            'elif (shi < 0.75 or (pbr > 0.65 and pnr < 0.20)',
            'elif (shi < 0.75 or local_lexical_alert or (pbr > 0.65 and pnr < 0.20)', 1)
        errors, _ = gate.test_reference_engine(mutated, 'local/global negative fixture')
        self.assertTrue(any('local/global separation' in error for error in errors))

    def test_gate_detects_inclusive_ratio_threshold(self):
        mutated = self.main.replace(
            'lexical_hit_ratio > self.lexical_alert_ratio_threshold',
            'lexical_hit_ratio >= self.lexical_alert_ratio_threshold', 1)
        errors, _ = gate.test_reference_engine(mutated, 'ratio negative fixture')
        self.assertTrue(any('K=20, hits=3' in error for error in errors))

    def test_gate_detects_missing_pnr_condition(self):
        mutated = self.main.replace('pbr > 0.65 and pnr < 0.20', 'pbr > 0.65', 1)
        errors, _ = gate.test_reference_engine(mutated, 'PNR negative fixture')
        self.assertTrue(any('high PNR excludes' in error for error in errors))

    def test_gate_detects_unearned_provenance_verification(self):
        mutated = self.main.replace(
            'provenance_verified: bool = field(default=False, init=False)',
            'provenance_verified: bool = field(default=True, init=False)', 1)
        errors, _ = gate.test_reference_engine(mutated, 'provenance negative fixture')
        self.assertTrue(any('without automatic verification' in error for error in errors))


if __name__=='__main__':
    unittest.main()
