# Positive Characteristic Resolution Example Library v4.4 — compositional manifest

The canonical Round-147 library is defined by

```text
v4.4 = positive_characteristic_resolution_example_library_v4_3.jsonl
     + example_library_147_patch.jsonl
```

- Base version: v4.3
- Base entries: 274
- Round-147 delta entries: 10
- Expected merged entries: 284
- New positive IDs: EX-POS-165--171
- New pathology IDs: EX-PATH-103--105
- Merge/validation command:

```bash
python merge_example_library_147.py \
  positive_characteristic_resolution_example_library_v4_3.jsonl \
  positive_characteristic_resolution_example_library_v4_4.jsonl
```

The merger rejects a base with a count other than 274, duplicate IDs, duplicate canonical hashes, or a malformed Round-147 hash. This compositional manifest is used because the immutable v4.3 base already exists in the persistent Example Library; Round 147 stores only the audited delta rather than duplicating 274 unchanged records.
