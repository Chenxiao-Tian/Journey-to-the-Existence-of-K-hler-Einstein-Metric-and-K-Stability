#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

path = Path(__file__).with_name('example_library_147_patch.jsonl')
entries = []
for line in path.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    e = json.loads(line)
    data = {k: v for k, v in e.items() if k != 'canonical_hash'}
    payload = json.dumps(data, sort_keys=True, ensure_ascii=False,
                         separators=(',', ':')).encode('utf-8')
    e['canonical_hash'] = hashlib.sha256(payload).hexdigest()[:16]
    entries.append(e)
path.write_text('\n'.join(json.dumps(e, ensure_ascii=False, sort_keys=True)
                          for e in entries) + '\n', encoding='utf-8')
print(f'PATCH_ENTRIES={len(entries)}')
print('PATCH_HASHES_FINALIZED')
