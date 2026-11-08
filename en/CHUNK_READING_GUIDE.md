> **Translation record**
> - Chinese source: `docs/白皮书分块读取与编辑.md` (sha256 `470697b8bce3d723a0f187a87b51779cfbd0ad5531eda80c3afd01daa99f68f9`, 5218 bytes, 2026-11-08)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-08
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Whitepaper Reading and Editing by Tag

Date: 2026-10-27. The main text still takes the [Chinese master source](../社会系统协议学白皮书.md) as its sole public source of definitions; the tags only mark reading and writing boundaries and add no new theoretical tier or RFC.

## Fixed Boundaries

The public main text has nine groups of HTML comment tags. The markers do not appear in the rendered Markdown; the original chapters, RFCs and legacy jump anchors are all retained.

```markdown
<!-- SP:BEGIN chapter-07 -->
<a id="chapter-7"></a>

## 第七章：第六组：迁移核算与试验筛选

……章节内容……
<!-- SP:END chapter-07 -->
```

| ID | Content |
|---|---|
| chapter-01 | Research positioning, primitives, postulates and the boundaries of the six groups |
| chapter-02 | Channel capacity and semantic boundaries |
| chapter-03 | Net intermediary contribution, complexity and normative choice |
| chapter-04 | Intertemporal commitment, record property and execution conditions |
| chapter-05 | Authority, conflict, incentives and exit |
| chapter-06 | Transmission topology and task feedback |
| chapter-07 | Migration accounting and trial screening |
| chapter-08 | Measurement definitions, reference implementations and research boundaries |
| appendix | Navigation of the 19 SP-RFC items, version concordance, and generation and evidence cards |

The start tag sits before the chapter's existing anchor, and the end tag before the next chapter begins. Chapter 8 ends before the closing words; the epigraph, table of contents and closing words are not part of any chapter block. The appendix runs to the end of the file. Separator lines and blank lines inside a chapter are also part of the original text and are not rearranged.

The ID is a machine location marker; it does not change when the title's wording changes. This version requires that the eight chapters plus the appendix each appear once, in the current order, with no nesting or crossing. If the structure is rearranged in future, the checking rules must be adjusted in step; one cannot simply move the tags. For now no separate boundary is added for each SP-RFC item.

## List First, Then Read the Target

The [tool](../tools/whitepaper_blocks.py) depends only on the Python standard library and requires Python 3.10+. The following commands are run in the repository root; the tool's relative input and output paths are all relative to the repository root.

```powershell
python tools/whitepaper_blocks.py list
python tools/whitepaper_blocks.py read chapter-07
python tools/whitepaper_blocks.py read appendix
```

`list` outputs only the nine IDs, titles, sizes and the SHA-256 of each block's raw bytes; add `--json` for structured output. The standard output of `read` contains only the complete original text between the tags, with the tags themselves omitted, and the hash is written to standard error.

The program still reads the file locally, but returns only the specified body text to the terminal or model, reducing context and location burden. For a small change, first search the chapter's specific passage; there is no need to rewrite the whole chapter each time. The tags do not automatically fill in dependencies: when changing a condition or definition, also read the relevant O/P, cross-chapter interfaces and appendix generation cards. To check 018, one may read Chapter 7 first, then supplement with the 017 interface and the corresponding appendix evidence card; one cannot skip necessary background just because only one chapter was read.

## Export, Preview and Explicit Writing

First export the block and keep the hash from that moment; `--out` only creates a new file and refuses to overwrite an existing editing draft:

```powershell
$blockInfo = python tools/whitepaper_blocks.py read chapter-07 --out .local/章节编辑/chapter-07.md | ConvertFrom-Json
```

Edit the exported file. It contains the chapter title and the existing anchors, but not the BEGIN/END tags; save it as UTF-8 without BOM and keep the trailing newline. Across editing sessions the `sha256` read at the time must be kept; do not re-take the hash after editing to bypass the conflict check.

First, only view the diff:

```powershell
python tools/whitepaper_blocks.py replace chapter-07 --from-file .local/章节编辑/chapter-07.md --expect-sha256 $blockInfo.sha256
```

By default it only previews: it does not write the main text and does not create a backup. After checking, use the same parameters and explicitly add `--write`:

```powershell
python tools/whitepaper_blocks.py replace chapter-07 --from-file .local/章节编辑/chapter-07.md --expect-sha256 $blockInfo.sha256 --write
```

The tool checks the target's original hash, the complete tag structure and the existing anchors, and refuses to delete or duplicate existing anchors. When writing, it first saves the complete original to `.local/章节编辑备份/`, replaces the body through a temporary file in the same directory, and preserves every byte outside the block. Changes made to other chapters after the read but before the plan is generated are retained from the latest body text; if a further body-text change is found after the plan is generated, the write is refused. The tool's own writes use a lock file, but this does not substitute for an external editor's concurrency control or for version management.

When there is no diff, it does not write and does not back up. Empty content, a missing trailing newline, a BOM, missing / duplicated / nested / crossed tags, wrong chapter assignment, lost anchors, a hash mismatch or an existing tool write lock all cause the operation to be refused. Tag examples inside fenced code blocks do not count as real boundaries.

The block editor only checks reading/writing boundaries and anchors; it does not substitute for review of the body text, formulas or code. After an actual change, still run the content-regression and public-scope checks according to [AGENTS.md](../AGENTS.md#四-自动化质量门禁verification-gate).

## The Internal Edition and Verification

The local internal edition uses the same tag format, but is read and modified independently; it is not overwritten chapter by chapter from the public edition. Specify the target explicitly with `--file`; the default is always the public main text. The internal edition and backups do not enter the public manifest.

```powershell
python tools/test_whitepaper_blocks.py
python tools/verify_all.py
python tools/test_verify_structure.py
python tools/check_public.py
```

The routine automated checks already verify the nine groups of boundaries; for the chunking tool's negative and write tests see the [regression script](../tools/test_whitepaper_blocks.py). When the maintainer changes the internal edition or a shared convention, the checks with `--internal` must still be run explicitly as AGENTS requires. Passing only shows that the designated structure and reference implementations have been checked; it does not mean that full-text empirical validation or mathematical proof is complete.
