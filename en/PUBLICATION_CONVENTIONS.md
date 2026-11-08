> **Translation record**
> - Chinese source: `docs/发布与目录约定.md` (sha256 `ed176b963ab9d4c340fa65e4a7434fecf77759609a80b5b8d4ab84eb1bc23b8d`, 5863 bytes, 2026-11-08)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-08
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Publication and Directory Conventions

## Public and Local

Public content is governed by the per-file manifest in the root `public-files.json`. The whitepaper and the CheatSheet keep their original paths; `articles/` holds cases and necessary sources, `research/` holds questions ready to be taken up, and `tools/` holds the publication tools.

The internal unabridged edition (not for public distribution), conversation and discussion records, original working drafts, review reports, audit evidence, browser caches, dependency copies, backups of source originals and publication plans remain in their original local locations and are excluded by ignore rules. The brief public revision notes record only article changes; they do not copy internal conversations or the original audit.

`.gitignore` is not a confidentiality system. It prevents ordinary accidental additions but cannot prevent `git add -f`, nor does it affect history objects that already exist. A check of the public manifest must also be run before every release.

## Content Regression, Publication Scope and Export

```powershell
python -m pip install -r tools/requirements.txt
python tools/verify_all.py
python tools/check_public.py
python tools/export_public.py
```

After the dependencies are installed, `verify_all.py` checks the designated structure and textual markers of the public whitepaper, CheatSheet and AGENTS, and runs the embedded reference engine's listed numerical, threshold, missing-value and metadata checks; the actual number of items is whatever the current run reports. The internal edition is not needed by default; the maintainer may follow [AGENTS.md](../AGENTS.md#四-自动化质量门禁verification-gate) to specify a local internal edition explicitly and add the corresponding checks. The script does not depend on the maintainer's old directories or on environment variables for the script's location.

The whitepaper remains a single public main-text file, using nine groups of tags to support chapter-by-chapter reading and editing; for the procedure see [Reading, Previewing and Replacing by Tag](../docs/白皮书分块读取与编辑.md). The automated checks also verify block boundaries; the editing tool previews by default, and writing requires checking the original block hash and preserving anchors. Block regression additionally runs `python tools/test_whitepaper_blocks.py`; backups and intermediate editing drafts are kept in `.local` and are not included in the public export.

`check_public.py` checks the file scope of the current index, whether the public files exist, whether they contain writing markers or local absolute paths, and whether Markdown local links fall within the public manifest. It does not automatically go online to verify external links, nor is it a guarantee of content safety or of the factual correctness of the whole text.

`export_public.py` first runs the same public-scope check, then copies the current working-tree files in the manifest into a new directory and ZIP. It does not copy `.git`, internal materials or old history; it does not commit or push, and it records the SHA-256 of each file. Working-tree text may differ from the committed version, and the export manifest records this explicitly. Export does not automatically run the content-regression gate; in the export directory one may additionally run `python tools/verify_all.py` and `python tools/check_public.py --snapshot`. The latter does not check the Git index.

## The Boundary of Existing History

Before this round of reorganisation, the local Git had already recorded the internal edition and a large amount of review material, and there were several old branches. Untracking does not erase this history; pushing the original working repository's history or backup branches directly may still bring them along.

The public repository initialises an independent Git history from the files in the manifest and does not copy the original working repository's `.git`. The history of the old working repository is kept as a local archive. To keep old commits and yet thoroughly clean their history requires separate planning for all branches, tags and backups.

The project remote is `https://github.com/nuoyazhizhou/socio-protocolics.git`. Configuring the remote and creating a local commit do not mean the work has been pushed or published; whether it is pushed publicly depends on the maintainer's explicit authorisation and the actual execution record.

## Main Text, Annotations and Sources

Public articles retain the limitations readers need to judge the conclusions, including what is unmeasured, provisional interpretations, sample limits and alternative explanations. Private writing strategies stay local. Removing `NOTE` markers does not mean verification is complete; one must not hide "not yet verified at present" in a memo that will be deleted and then go on to tell readers that "everything has been verified".

Public sources give priority to the original author's text, contemporaneous originals, technical standards or the original study, stating separately what they support and what they do not support. Engineering analogies are labelled with their purpose; historical material is not upgraded to causal verification merely because it fits the framework.

## Version and Licence

The release tag for this revision of Whitepaper v11.2 is `v11.2-r20261106`; see the [Revision Record](../docs/修订记录.md). The theoretical version and the revision snapshot are kept separate; existing articles keep their own versions according to purpose.

The unified version of the whitepaper remains v11.2. Case articles and research cards carry their own versions; revising an article is not a claim that the whitepaper's core propositions have completed empirical validation. Article revisions should keep a public summary; working drafts and full diffs may be kept locally.

No unified licence, such as MIT or CC BY, has been chosen on the author's behalf. The scope of use for the publishing platform, contribution licensing and third-party quotations is handled separately.

## Online Reading and Automated Publishing

The site is at the [GitHub Pages reading site](https://nuoyazhizhou.github.io/socio-protocolics/). It is generated from the public manifest by the [site build tool](../tools/build_site.py); the chapter pages come from the SSOT's nine groups of tags and do not write back to or split the authoritative main text. Both the site's input and output live in the ignored `.local` build directory; the working tree is not copied recursively.

Local installation and build:

```powershell
python -m pip install -r tools/requirements-site.txt
python tools/build_site.py
python tools/test_build_site.py
python tools/check_site.py
python -m http.server 8000 --directory .local/site-build
```

The build uses strict mode; vertical bars in Markdown formulas are converted to equivalent LaTeX delimiters only in the derived input, so that they are not read as table columns. On-site chapter links keep the existing anchors leading to the full main text. Math rendering loads a fixed-version MathJax resource from a public CDN, and some charts also require the browser to load rendering resources; when offline these presentations cannot be guaranteed, but the authoritative Markdown can still be downloaded and read.

The [Pages workflow](../.github/workflows/pages.yml) runs the public-content checks, build and deployment when `main` or `codex/public-release` receives a commit, and also supports manual triggering. The repository administrator must first set the GitHub Pages publishing source to GitHub Actions; credentials are kept in the GitHub / local credential system and are not written into the repository. Remote push, Actions success and site reachability are each verified separately; a successful local build is not a substitute for a successful publication.
