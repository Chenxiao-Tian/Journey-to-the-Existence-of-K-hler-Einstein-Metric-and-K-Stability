#!/usr/bin/env python3
"""Merge the canonical Round-146 v4.3 library with the Round-147 delta.

Usage:
  python merge_example_library_147.py BASE_V4_3.jsonl OUTPUT_V4_4.jsonl
"""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit(__doc__)
base, out = map(Path, sys.argv[1:])
patch = Path(__file__).with_name('example_library_147_patch.jsonl')

def load(p):
    return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]

def ch(e):
    data={k:v for k,v in e.items() if k!='canonical_hash'}
    raw=json.dumps(data,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()[:16]

old=load(base); new=load(patch); all_entries=old+new
if len(old)!=274:
    raise SystemExit(f'expected 274 base entries, got {len(old)}')
ids=[e['id'] for e in all_entries]; hashes=[e['canonical_hash'] for e in all_entries]
if len(ids)!=len(set(ids)): raise SystemExit('duplicate IDs')
if len(hashes)!=len(set(hashes)): raise SystemExit('duplicate canonical hashes')
for e in new:
    if e['canonical_hash']!=ch(e): raise SystemExit(f"bad patch hash {e['id']}")
out.write_text('\n'.join(json.dumps(e,ensure_ascii=False,sort_keys=True) for e in all_entries)+'\n',encoding='utf-8')
print(f'BASE_ENTRIES={len(old)}')
print(f'PATCH_ENTRIES={len(new)}')
print(f'MERGED_ENTRIES={len(all_entries)}')
print('UNIQUE_IDS=yes')
print('UNIQUE_HASHES=yes')
